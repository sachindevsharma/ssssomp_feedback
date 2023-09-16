from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
import plotly.graph_objs as go


def build_stats_page():
    yes_bar = go.Bar(name="Yes", marker={"color": "green"})
    no_bar = go.Bar(name="No", marker={"color": "red"})

    daily_stats_fig = go.Figure()
    daily_stats_fig.add_traces([yes_bar, no_bar])
    daily_stats_fig.update_layout(
        title="Daily Response Count",
        showlegend=False,
    )

    monthly_stats_fig = go.Figure()
    monthly_stats_fig.add_traces([yes_bar, no_bar])
    monthly_stats_fig.update_layout(
        title="Monthly Response Count",
        showlegend=False,
        xaxis={"tickformat": "%b %Y"}
    )

    return html.Div(id="stats_div", children=[
        dbc.Row([
            dbc.Col(html.H3("Today's Counter"), width="auto"),
            dbc.Col(
                daq.LEDDisplay(value=0, id='stats_yes_led', label="YES"), 
                width="auto"
            ),
            dbc.Col(
                daq.LEDDisplay(value=0, id='stats_no_led', label="NO"),
                width="auto")
        ]),
        dbc.Col([
            dcc.Graph(id="daily_response_fig", 
                      figure=daily_stats_fig, 
                      config={"displayModeBar": False})
        ]),
        dbc.Col([
            dcc.Graph(id="monthly_response_fig", 
                      figure=monthly_stats_fig,
                      config={"displayModeBar": False})
        ]),
        dcc.Store(id="daily_response_data"),
        dcc.Store(id="monthly_response_data"),
        dcc.Store(id="yearly_response_data"),
        dcc.Interval(id="stats_interval", interval=10000),
    ])