import dash
from dash import html, dcc, Input, State, Output, ctx
from mongo_connector import MongoConnector

client = MongoConnector()
collection = client.get_collection("feedback", "sewa_feedback")

def update_mongo_count(categ):
    collection.update_one({"type": categ.upper()}, {"$inc": {"count": 1}})
    
def _get_nav_link(page):
    return dash.page_registry[page]["relative_path"]


def Callbacks():
    @dash.callback([Output("yes_button", "href"),
                    Output("no_button", "href")],
                   Input("home_page_div", "n_clicks"))
    def update_yes_button_href(n):
        ctx = dash.ctx.triggered_id 
        if ctx is None:
            print("setting href")
            return [_get_nav_link("happy"), _get_nav_link("sad")]
        else:
            dash.no_update

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
