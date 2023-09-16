import dash
from dash import html
import dash_bootstrap_components as dbc


from .home_page_layout import build_home_page, build_happy_div, build_sad_div
from .stats_layout import build_stats_page
from .not_found_404 import not_found_404

def Layout():
     return dbc.Container([
		build_banner(),
		html.Br(),
		html.Div(id='second_div', children=[
            dash.page_container
        # END OF 2nd Division   
        ]),
		# html.Footer("Footer")
	])


def register_app_pages():
    page_values = [
		# id , name, path, layout
		["home", "Home", '/', build_home_page()],
		["happy", "Happy", '/happy', build_happy_div()],
		["sad", "Sad", '/sad', build_sad_div()],
        ["admin", "Admin", '/sairamadmin', build_stats_page()],
	]       
    for order, (module , name, path, layout) in enumerate(page_values):
        dash.register_page(module, name=name, path=path, layout=layout, order=order)
        
    dash.register_page("not_found_404", layout=not_found_404())
    

def build_banner():
    return  dbc.Row([
        dbc.Col(xs=12, sm=12, md=12, lg=12, xl=12, class_name="h-15vh", children=[
            html.Img(className="w-100 h-100", src=dash.get_asset_url("title.jpeg")),
			]),
		])


