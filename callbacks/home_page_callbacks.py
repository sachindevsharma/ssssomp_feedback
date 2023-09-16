import dash
from dash import html, dcc, Input, State, Output, ctx
from datetime import datetime
import pytz
from mongo_connector import MongoConnector

client = MongoConnector()
collection = client.get_collection("feedback", "sewa_feedback")

def home_page_callbacks():
    @dash.callback([Output("yes_button", "href"),
                    Output("no_button", "href")],
                   Input("home_page_div", "n_clicks"))
    def update_yes_button_href(n):
        ctx = dash.ctx.triggered_id 
        if ctx is None:
            return [_get_nav_link("happy"), _get_nav_link("sad")]
        else:
            dash.no_update

    @dash.callback(Output("home_page_div", "n_clicks"),
                  Input("yes_button", "n_clicks"),
                  Input("no_button", "n_clicks"),
                  prevent_initial_call=True)
    def update_counts(n1, n2):
        button_id = ctx.triggered_id if not None else 'No clicks yet'
        if button_id == "yes_button":
            update_mongo_count("yes")
            dash.no_update
        elif button_id == "no_button":
            update_mongo_count("no")
            dash.no_update
        else: 
            dash.no_update


def update_mongo_count(categ):
    date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d")
    results = collection.find_one({"date": date})
    if results is None:
        collection.insert_one({"date": date, "yes": 0, "no": 0})

    collection.update_one({"date": date}, {"$inc": {categ.lower(): 1}})
    

def _get_nav_link(page):
    return dash.page_registry[page]["relative_path"]


