import dash
from layout import Layout
from callbacks import Callbacks
import dash_bootstrap_components as dbc
import os
import json

print("Sachin", os.environ.get("username"))

# Read the secrets from the file
with open('etc/secrets/credentials', 'r') as file:
    secrets = json.load(file)

print("Sachin", secrets)

app = dash.Dash(__name__,
                title="SSSSO MP",
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      'https://use.fontawesome.com/releases/v5.8.1/css/all.css'], 
                suppress_callback_exceptions=True)
server = app.server


app.layout = Layout(app)
Callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=9999)