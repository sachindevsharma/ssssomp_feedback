import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import pytz
from datetime import datetime
from mongo_connector import MongoConnector
from flask_caching import Cache

CACHE = Cache(dash.get_app().server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

client = MongoConnector()
collection = client.get_collection("feedback", "sewa_feedback")


@CACHE.memoize(timeout=86400) 
def collect_historical_data(today):
    this_month = today[:7] + "-01"

    results = list(collection.find({}))
    df = pd.DataFrame(results).drop(["_id"], axis=1).sort_values("date")
    df["month"] = [i[:7] + "-01" for i in df["date"]]
    daily_df = df[df["date"] < today][df["month"] == this_month]

    df["year"] = [i[:4] + "-01-01" for i in df["date"]]
    month_df = df[df["month"] < this_month]\
        .groupby("month").agg({"yes": "sum", "no": "sum"}).fillna(0).reset_index()

    return daily_df.drop("month", axis=1), month_df


def get_today_data():
    today = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d")
    results = collection.find_one({"date": today})
    return results, today


def stats_callbacks():

    @dash.callback(Output("daily_response_data", "data"),
                   Output("monthly_response_data", "data"),
                   Input("stats_interval", "n_interval"),
                  )
    def update_stats_once_a_day(n):
        today = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d")
        daily_df, month_df = collect_historical_data(today)
        daily_data = {"dates": daily_df["date"].tolist(),
                      "yes_cnt": daily_df["yes"].tolist(),
                      "no_cnt": daily_df["no"].tolist()}
        
        month_data = {"dates": month_df["month"].tolist(),
                      "yes_cnt": month_df["yes"].tolist(),
                      "no_cnt": month_df["no"].tolist()}
        return [daily_data, month_data]


    @dash.callback(Output("daily_response_fig", "figure"),
                   Output("stats_yes_led", "value"),
                   Output("stats_no_led", "value"),
                   Input("daily_response_data", "data"),
                   prevent_initial_call=True
                  )
    def update_figure(data):
        today_data, today = get_today_data()
        data["dates"].append(today)
        if today_data:
            yes, no = today_data["yes"], today_data["no"]
        else:
            yes, no = 0, 0

        data["yes_cnt"].append(yes)
        data["no_cnt"].append(no)

        fig = dash.Patch()    # Partial update of graph
        fig["data"][0]["x"], fig["data"][0]["y"] = data["dates"], data["yes_cnt"]
        fig["data"][1]["x"], fig["data"][1]["y"] = data["dates"], data["no_cnt"]
        return [fig, yes, no]
    

    @dash.callback(Output("monthly_response_fig", "figure"),
                   Input("monthly_response_data", "data"),
                   prevent_initial_call=True
                  )
    def update_figure(data):
        today_data, today = get_today_data()
        daily_df, _ = collect_historical_data(today)
        data["dates"].append(today[:7] + "-01")

        yes = daily_df["yes"].sum()
        no = daily_df["no"].sum()

        if today_data:
            yes += today_data["yes"]
            no += today_data["no"]

        data["yes_cnt"].append(yes)
        data["no_cnt"].append(no)

        fig = dash.Patch()    # Partial update of graph
        fig["data"][0]["x"], fig["data"][0]["y"] = data["dates"], data["yes_cnt"]
        fig["data"][1]["x"], fig["data"][1]["y"] = data["dates"], data["no_cnt"]
        return fig
    
