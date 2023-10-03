import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask_caching import Cache
from mongo_connector import MongoConnector
from config import Config

CONFIG = Config()

CACHE = Cache(dash.get_app().server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

client = MongoConnector()
collection = client.get_collection(CONFIG.DATABASE_NAME, CONFIG.QUESTIONS_COLLECTION)
questions = list(collection.find({"type": {"$ne": "old_questions"}}))
questions = [(i["type"], i["question"]) for i in questions]

button_width = {"xs": 12, "sm": 12, "md": 6, "lg": 6, "xl": 6}


def build_home_page():
    return html.Div(id="home_page_div", children=[
            html.Br(),
            dbc.Alert("कृपया सभी प्रश्नों के उत्तर दें !",
                id="home_page_alert", is_open=False, duration=4000),
            _add_note(),
            _generate_questions(),
            html.Br(),
            dbc.Col(dbc.Button("SUBMIT", id="submit_button", color="primary"),
                       **width_dict_same(12)),
            html.Br(),
            dcc.Location(id="url_results", refresh=False)
        ])


def _add_note():
    return html.Div([
        html.H6('निर्देश :-'),
        html.H6('★ यह साधना आपको (स्वयं) अनिवार्य रूप से करना है।'),
        html.H6('★ आप यह साधना आपके समयानुसार कर सकते हैं एवं अपने परिवार के सदस्यों को इसमें सम्मिलित कर सकते हैं।'),
    ])

def _generate_questions():
    questions_elem = [
        dbc.Col(generate_card(f"q{n + 1}", ques, "narayan_sewa_sq.jpg"),
                **width_dict_multi(12, 6, 6))
        for  n, (q_type, ques) in enumerate(questions)
    ]
    return dbc.Row(questions_elem)
    


def generate_card(suffix, question, image):
    return dbc.Row([
        dbc.Card(className="cards",  color="light", children=[
            dbc.CardImg(src=dash.get_asset_url(image), className="card-img"),
            dbc.CardImgOverlay(
                dbc.CardBody([
                    html.H2(question, className="card_question"),
                    dbc.Row([
                        dbc.Col(html.I(id=f"thumbs_up_{suffix}"), className="text-center"),
                        dbc.Col(html.I(id=f"thumbs_down_{suffix}"), className="text-center"),
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col("हाँ, आज हमने व्यक्तिगत साधना की है", className="yes_message"),
                        dbc.Col("नही, आज हम व्यक्तिगत साधना नही कर सके", className="no_message"),
                    ]),
                ]),
            )
        ])		
    ])

def build_happy_div():
    return html.Div(id="happy_div", children=[
# 			html.P("बहुत अच्छे, ऐसे ही नियमित व्यक्तिगत साधना करते रहना।  साई राम।✨"),
            dbc.Col(_happy_video(), 
                       xs=12, sm=12, md=12, lg=6, xl=6, class_name="text-center",
                    ),
        ])

def build_sad_div():
    return html.Div(id="sad_div", children=[
            html.P('''"यह कभी मत सोचो कि तुम और भगवान अलग हो। हमेशा सोचो, 
                         "भगवान मेरे साथ है; वह मेरे अंदर है; वह मेरे आसपास है। सब कुछ है, ईश्वर है। 
                      मैं खुद भगवान हूं। मैं अनंत हूं, शाश्वत हूं। मैं दो नहीं हूँ; मैं एक हूँ, केवल एक। मेरे अलावा और कोई नहीं है। 
                         मैं और ईश्वर एक ही हैं।" इस एकता को महसूस करने के लिए, पहला कदम है आत्मविश्वास विकसित करना। 
                      यह तब आता है जब आपको पता चलता है कि ईश्वर आपके बाहर नहीं है।" - भगवान बाबा'''),
            dbc.Col(_sad_image(),
                    xs=12, sm=12, md=12, lg=12, xl=12, class_name="text-center"),
        ])

@CACHE.memoize(timeout=86400) 
def _happy_video():
    return html.Video(id="video_tag", src=dash.get_asset_url("HAPPY.mp4"), 
                    controls=True, autoPlay=True, width="100%", preload="auto")

@CACHE.memoize(timeout=86400) 
def _sad_image():
    return html.Img(src=dash.get_asset_url("swami_angry.jpeg"))

def width_dict_same(width):
    size = ["xs", "sm", "md", "lg", "xl"]
    data = {i: width for i in size}
    return data

def width_dict_multi(small, medium, large):
    return {"xs": small, "sm": small, "md": medium, "lg": large, "xl": large}
                