import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                title="SSSSO MP",
                use_pages=True, 
                pages_folder="",
                update_title=None,
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      'https://use.fontawesome.com/releases/v6.4.2/css/all.css'], 
                suppress_callback_exceptions=True)
server = app.server

from layouts import Layout, register_app_pages
from callbacks import Callbacks

register_app_pages()
app.layout = Layout()
Callbacks()


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=9999)