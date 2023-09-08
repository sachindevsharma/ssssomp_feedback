import dash
from dash import html
import dash_bootstrap_components as dbc


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


def build_banner():
    return  dbc.Row([
        dbc.Col(xs=12, sm=12, md=12, lg=12, xl=12, class_name="h-15vh", children=[
            html.Img(className="w-100 h-100", src=dash.get_asset_url("title.jpeg")),
			]),
		])


def build_home_page():
    return html.Div(id="home_page_div", children=[
			# html.H3("✨आध्यात्मिक विभाग के अंतर्गत व्यक्तिगत साधना का फीडबैक फॉर्म।✨", className="text-center",),
			# html.Br(),
			html.H6('निर्देश :-'),
			html.H6('★ यह साधना आपको (स्वयं) अनिवार्य रूप से करना है।'),
			html.H6('★ आप यह साधना आपके समयनुसार कर सकते हैं एवं अपने परिवार के सदस्यों को इसमें सम्मलित कर सकते हैं।'),
			html.Br(),
			html.H1("क्या आपने आज भगवान द्वारा निर्देशित किसी भी गतिविधी में व्यक्तिगत साधना की है ?", className="text-center text-primary"),
			html.Br(),
			dbc.Row(children=[
				dbc.Col(dbc.Button("हाँ, आज हमने व्यक्तिगत साधना की है", color="success", id="yes_button")),
				dbc.Col(dbc.Button("नही, आज हम व्यक्तिगत साधना नही कर सके", color="danger", id="no_button"))
				]),
		])
          
def build_happy_div():
    return html.Div(id="happy_div", children=[
# 			html.P("बहुत अच्छे, ऐसे ही नियमित व्यक्तिगत साधना करते रहना।  साई राम।✨"),
			dbc.Col(xs=12, sm=12, md=12, lg=6, xl=6, class_name="text-center", children=[
				# html.Img(src=app.get_asset_url("swami_happy.jpeg")),
				html.Video(id="video_tag", src=dash.get_asset_url("HAPPY.mp4"), 
               				controls=True, autoPlay=True, width="100%", preload="auto")
				]),
	    ])

def build_sad_div():
    return html.Div(id="sad_div", children=[
			html.P('''"यह कभी मत सोचो कि तुम और भगवान अलग हो। हमेशा सोचो, 
           			  "भगवान मेरे साथ है; वह मेरे अंदर है; वह मेरे आसपास है। सब कुछ है, ईश्वर है। 
                	  मैं खुद भगवान हूं। मैं अनंत हूं, शाश्वत हूं। मैं दो नहीं हूँ; मैं एक हूँ, केवल एक। मेरे अलावा और कोई नहीं है। 
                   	  मैं और ईश्वर एक ही हैं।" इस एकता को महसूस करने के लिए, पहला कदम है आत्मविश्वास विकसित करना। 
                      यह तब आता है जब आपको पता चलता है कि ईश्वर आपके बाहर नहीं है।" - भगवान बाबा'''),
			dbc.Col(xs=12, sm=12, md=12, lg=12, xl=12, class_name="text-center", children=[
				html.Img(src=dash.get_asset_url("swami_angry.jpeg")),
				]),
	    ])


def register_app_pages():
    page_values = [
		# id , name, path, layout
		["home", "Home", '/', build_home_page()],
		["happy", "Happy", '/happy', build_happy_div()],
		["sad", "Sad", '/sad', build_sad_div()],
	]       
    for order, (module , name, path, layout) in enumerate(page_values):
        dash.register_page(module, name=name, path=path, layout=layout, order=order)