import pandas as pd
import plotly

import dash  # pip install dash
import dash_html_components as html
from dash_extensions import BeforeAfter  # pip install dash-extensions==0.0.47 or higher
import dash_bootstrap_components as dbc  # dash-bootstrap-components
import dash_core_components as dcc

import wave
import time
from playsound import playsound

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("My album of London", style={'textAlign': 'center', 'color': 'black'})
        ], width=12)
    ), html.Audio(src='assets/streets-of-London.wav', controls=True),
    html.H6("Streets of London", style={'fontSize': '16px'}),

    html.Hr(),
    dbc.Row([

        dbc.Col([
            html.H2("Regent Street"),
            html.H6("2020.12.02 ", style={'fontSize': '12px'}),
            html.H6("The lights are beautiful!"),
            BeforeAfter(before="assets/After_Regentstreet.png", after="assets/Regentstreet.JPG", width=512,
                        height=412, defaultProgress=0.5),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🌟', 'value': 'love2'},
                    {'label': '    👼🏼', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6),

        dbc.Col([
            html.H2("City of London"),
            html.H6("2020.12.12 ", style={'fontSize': '12px'}),
            html.H6("Seems back home."),
            BeforeAfter(before="assets/Londoncity2.png", after="assets/CityofLondon.JPG", width=512, height=412,
                        defaultProgress=0.5),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🛥', 'value': 'love2'},
                    {'label': '    🌆', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6)

    ]),
    # html.Button('❤', id='submit-val', style={'background-color': 'white', 'color': 'black', 'border': '2px solid #e7e7e7'}),

    html.Hr(),
    dbc.Row([

        dbc.Col([
            html.H2("London Eye"),
            html.H6("2021.01.01 ", style={'fontSize': '12px'}),
            html.H6("New Year's night!"),
            BeforeAfter(before="assets/AfterLE_2.png", after="assets/Londoneye.JPG", width=512, height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🎡', 'value': 'love2'},
                    {'label': '    🎆', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6),

        dbc.Col([
            html.H2("Hampstead Health"),
            html.H6("2021.01.23 ", style={'fontSize': '12px'}),
            html.H6("Clouds unforgettable that day."),
            BeforeAfter(before="assets/cloudOut.JPG", after="assets/cloud.JPG", width=512, height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🌤️', 'value': 'love2'},
                    {'label': '    ⛰', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6)

    ]),

    html.Hr(),
    dbc.Row([

        dbc.Col([
            html.H2("Tower Bridge"),
            html.H6("2021.02.10 ", style={'fontSize': '12px'}),
            html.H6("Must-visit place in London."),
            BeforeAfter(before="assets/Figure_towerbridge.jpg", after="assets/Towerbridge.JPG", width=512,
                        height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🍻', 'value': 'love2'},
                    {'label': '    🕶', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),

        ], width=6),

        dbc.Col([
            html.H2("St.Paul's Cathedral"),
            html.H6("2021.02.10 ", style={'fontSize': '12px'}),
            html.H6("Caught you！"),
            BeforeAfter(before="assets/St02.png", after="assets/StPaul.JPG",
                        width=512, height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🤳', 'value': 'love2'},
                    {'label': '    🕌', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),

        ], width=6),

    ]),

    html.Hr(),
    dbc.Row([

        dbc.Col([
            html.H2("London Bridge"),
            html.H6("2021.02.10 ", style={'fontSize': '12px'}),
            html.H6("The Shard seen from the bridge hole."),
            BeforeAfter(before="assets/LondonBridgeOut.JPG", after="assets/LondonBridge.JPG", width=512, height=412,
                        defaultProgress=0.5),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🕳', 'value': 'love2'},
                    {'label': '    ⛲️', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6),

        dbc.Col([
            html.H2("Hyde Park"),
            html.H6("2021.02.27 ", style={'fontSize': '12px'}),
            html.H6("The swans seems like lovers."),
            BeforeAfter(before="assets/HydeparkswanOut.JPG", after="assets/Hydeparkswan.JPG", width=512, height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🦢', 'value': 'love2'},
                    {'label': '    💋', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6)

    ]),

    html.Hr(),
    dbc.Row([

        dbc.Col([
            html.H2("Richmond"),
            html.H6("2021.03.06 ", style={'fontSize': '12px'}),
            html.H6(" I saw a herd of deer, they looked at me too!"),
            BeforeAfter(before="assets/Figure_Richmond.jpg", after="assets/Richmond.JPG", width=512, height=412,
                        defaultProgress=0.5),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🦌', 'value': 'love2'},
                    {'label': '    🌳', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6),

        dbc.Col([
            html.H2("Mudchute Park and Farm"),
            html.H6("2021.03.30 ", style={'fontSize': '12px'}),
            html.H6("The lambs are so cute!"),
            BeforeAfter(before="assets/Figure_1.jpg", after="assets/sheep.jpg", width=512, height=412),
            dcc.RadioItems(
                options=[
                    {'label': '    ❤', 'value': 'love1'},
                    {'label': '    🐑', 'value': 'love2'},
                    {'label': '    🥬', 'value': 'love3'}
                ],
                value='MTL',
                labelStyle={'display': 'inline-block', 'top': '10px', 'margin-top': '10px', 'margin-right': '20px'}
            ),
        ], width=6)
    ]),
]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8002)