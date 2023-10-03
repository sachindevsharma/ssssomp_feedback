import os
import dash
from dash import html, dcc, Input, State, Output, ctx
from datetime import datetime
import pytz
from mongo_connector import MongoConnector
from flask_caching import Cache
from config import Config

CONFIG = Config()

CACHE = Cache(dash.get_app().server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

n_questions = 1

sm_up_icon = "fa fa-regular fa-thumbs-up fa-4x"
lg_up_icon = "fa fa-regular fa-thumbs-up fa-6x"

sm_down_icon = "fa fa-regular fa-thumbs-down fa-4x"
lg_down_icon = "fa fa-regular fa-thumbs-down fa-6x"

client = MongoConnector()
collection = client.get_collection(CONFIG.DATABASE_NAME, CONFIG.FEEDBACK_COLLECTION)

def home_page_callbacks():
    @dash.callback([Output("yes_button", "href"),
                   Output("no_button", "href")],
                   Input("stats_interval", "n_interval"),
                   State("stats_interval", "n_interval"),
                   State("stats_interval", "n_interval"))
    def update_yes_button_href(n):
        ctx = dash.ctx.triggered_id 
        if ctx is None:
            return [_get_nav_link("happy"), _get_nav_link("sad")]
        else:
            dash.no_update

    # @dash.callback(
    #     Output("home_page_alert", "is_open"),
    #     Input("alert-toggle-auto", "n_clicks"),
    #     State("home_page_alert", "is_open"),
    # )
    # def toggle_alert(n, is_open):
    #     if n:
    #         return not is_open
    #     return is_open
    
    for n in range(1, n_questions + 1):
        @CACHE.memoize(timeout=86400)
        @dash.callback(Output(f"thumbs_up_q{n}", "className"),
                    Output(f"thumbs_down_q{n}", "className"),
                    Input(f"thumbs_up_q{n}", "n_clicks"),
                    Input(f"thumbs_down_q{n}", "n_clicks"),
                    State(f"thumbs_up_q{n}", "className"),
                    State(f"thumbs_down_q{n}", "className"))
        def change_thumbs_up(n1, n2, cl_up, cl_down):

            if ctx.triggered[0]["value"] is None:
                return sm_up_icon, sm_down_icon
             
            if ctx.triggered[0]["prop_id"].split(".")[0].startswith("thumbs_up"):
                if cl_up == sm_up_icon:
                    return lg_up_icon, sm_down_icon
                else:
                    return sm_up_icon, sm_down_icon
                
            if ctx.triggered[0]["prop_id"].split(".")[0].startswith("thumbs_down"):
                if cl_down == sm_down_icon:
                    return sm_up_icon, lg_down_icon
                else:
                    return sm_up_icon, sm_down_icon

    ques_yes_div = [State(f"thumbs_up_q{n}", "className") for n in range(1, n_questions + 1)]
    ques_no_div = [State(f"thumbs_down_q{n}", "className") for n in range(1, n_questions + 1)]

    @CACHE.memoize(timeout=86400)
    @dash.callback(
        # Output("home_page_alert", "is_open"),
        Output("url_results", "pathname"),
        Output("url_results", "refresh"),
        Input("submit_button", "n_clicks"),
        State("home_page_alert", "is_open"),
        *ques_yes_div, *ques_no_div,
        prevent_initial_call=True)
    def open_page(n, is_open, *args):
        # if lg_up_icon in args or lg_down_icon in args:
            # print("Error")
        if lg_up_icon in args:
            return _get_nav_link("happy"), True
        else:
            return _get_nav_link("sad"), True
        # else:
        #     return True, dash.no_update, dash.no_update
  

    @dash.callback(
        Output("home_page_div", "n_clicks"),
        Input("submit_button", "n_clicks"),
        *ques_yes_div, 
        *ques_no_div, 
        prevent_initial_call=True)
    def update_counts(n, *args):
        if lg_up_icon in args or lg_down_icon in args:
            count_dict = {}
            for n_ques in range(n_questions):
                if args[n_ques] == lg_up_icon:
                    count_dict[f"q{n_ques + 1}"] = {"yes" : 1, "no": 0}
                else:
                    count_dict[f"q{n_ques + 1}"] = {"yes" : 0, "no": 1}
            update_mongo_count(count_dict)
            dash.no_update
        else:
            dash.no_update


def update_mongo_count(count_dict):
    date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d")
    results = collection.find_one({"date": date})
    if results is None:
        collection.insert_one({"date": date, 
                               "narayan_sewa": {"yes": 0, "no": 0},
                               "mahila_sadhna": {"yes": 0, "no": 0}} )

    collection.update_one({"date": date}, {"$inc": {"narayan_sewa.yes": count_dict["q1"]["yes"]}})
    collection.update_one({"date": date}, {"$inc": {"narayan_sewa.no": count_dict["q1"]["no"]}})
    # collection.update_one({"date": date}, {"$inc": {"mahila_sadhna.yes": count_dict["q2"]["yes"]}})
    # collection.update_one({"date": date}, {"$inc": {"mahila_sadhna.no": count_dict["q2"]["no"]}})
    

def _get_nav_link(page):
    return dash.page_registry[page]["relative_path"]


