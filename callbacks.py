import dash
from dash import html, dcc, Input, State, Output, ctx
from dash.exceptions import PreventUpdate
from mongo_connector import MongoConnector

client = MongoConnector()
collection = client.get_collection("feedback", "sewa_feedback")

def update_mongo_count(categ):
    collection.update_one({"type": categ.upper()}, {"$inc": {"count": 1}})
    

def Callbacks(app):
    
    @app.callback(Output("home_page_div", "style"),
                  Output("happy_div", "style"),
                  Output("sad_div", "style"),
                  Output("video_tag", "autoPlay"),
                  Input("yes_button", "n_clicks"),
                  Input("no_button", "n_clicks"),
                  prevent_initial_call=True)
    def get_click_count(n1, n2):
        button_id = ctx.triggered_id if not None else 'No clicks yet'
        print(button_id)
        if button_id == "yes_button":
            return  {"display": "None"}, {"display": "block"}, {"display": "None"}, True
        elif button_id == "no_button":
            return {"display": "None"}, {"display": "None"}, {"display": "block"}, False
        else: 
            PreventUpdate

    # @app.callback(Output("home_page_div", "n_clicks"),
    #               Input("yes_button", "n_clicks"),
    #               Input("no_button", "n_clicks"),
    #               prevent_initial_call=True)
    # def update_counts(n1, n2):
    #     button_id = ctx.triggered_id if not None else 'No clicks yet'
    #     if button_id == "yes_button":
    #         update_mongo_count("YES")
    #         print(1)
    #         PreventUpdate
    #     elif button_id == "no_button":
    #         update_mongo_count("NO")
    #         PreventUpdate
    #     else: 
    #         PreventUpdate
