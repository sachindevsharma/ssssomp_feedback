import dash
from dash import html, dcc

# --- Configuration ---
# You can easily change these values to customize the app.

# URL for the background image. I've selected a high-quality, relevant image from Pexels.
# For best results, replace this with the URL of the 4K image we generated.
BACKGROUND_IMAGE_URL = "https://images.pexels.com/photos/3183172/pexels-photo-3183172.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# The main text content
COMPANY_NAME = "Beyonders.ai"
MAIN_HEADLINE = "EMPOWERING YOUR BUSINESS WITH AI SOLUTIONS"
BUTTON_TEXT = "GET IN TOUCH"
NAV_LINKS = ["Home", "About", "Services", "Contact"]

# --- Dash App Initialization ---
app = dash.Dash(__name__)
server = app.server

# --- Custom App Index String for CSS Reset ---
# This injects CSS into the page head to remove default browser margins
# and enable smooth scrolling for the navigation links.
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body { margin: 0; padding: 0; scroll-behavior: smooth; }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

# --- Helper Function for Styling ---
# This function generates the style dictionary for our main hero section.
def create_hero_style(image_url):
    """Generates the style dictionary for the main hero container."""
    return {
        'backgroundImage': f'url({image_url})',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center center',
        'height': '100vh', # Make hero section full screen height
        'display': 'flex',
        'flexDirection': 'column',
        'position': 'relative', # Required for the overlay to work correctly
    }


# --- App Layout ---
app.layout = html.Div(
    style={
        'height': '100%',
        'width': '100%',
        'fontFamily': "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
        'margin': 0,
        'padding': 0, # Ensure no padding on the main container
        'backgroundColor': '#020c1b',
    },
    children=[
        # The header section with logo and navigation tabs.
        html.Header(
            style={
                'width': '100%',
                'padding': '20px 5%',
                'boxSizing': 'border-box',
                'position': 'sticky', # Make the header sticky
                'top': 0, # Stick to the top of the viewport
                'zIndex': 10,
                'display': 'flex',
                'justifyContent': 'space-between',
                'alignItems': 'center',
                'background': 'rgba(2, 12, 27, 0.8)', # Semi-transparent background
                'backdropFilter': 'blur(10px)', # Frosted glass effect
                'borderBottom': '1px solid rgba(255, 255, 255, 0.1)',
            },
            children=[
                # Company Name / Logo
                html.H2(
                    COMPANY_NAME,
                    style={
                        'color': 'white',
                        'margin': 0,
                        'fontSize': '28px',
                        'fontWeight': 'bold',
                    }
                ),
                # Navigation Tabs
                html.Nav(
                    children=[
                        html.A(
                            link,
                            href=f"#{link.lower().replace(' ', '-')}",
                            style={
                                'color': '#E0E0E0',
                                'margin': '0 15px',
                                'textDecoration': 'none',
                                'fontWeight': '500',
                                'fontSize': '16px',
                                'padding': '8px 0',
                                'borderBottom': '2px solid transparent',
                                'transition': 'all 0.3s ease',
                            }
                        ) for link in NAV_LINKS
                    ]
                )
            ]
        ),
        # The main container div that holds the background image and all content.
        html.Div(
            id='home', # ID for the "Home" navigation link
            style=create_hero_style(BACKGROUND_IMAGE_URL),
            children=[
                # A semi-transparent overlay to darken the background image,
                # ensuring the white text is readable and stands out.
                html.Div(
                    style={
                        'position': 'absolute',
                        'top': 0,
                        'left': 0,
                        'right': 0,
                        'bottom': 0,
                        'backgroundColor': 'rgba(2, 12, 27, 0.65)', # Dark blue overlay
                    }
                ),

                # The main content area for the headline and button.
                html.Main(
                    style={
                        'flex': 1,
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'textAlign': 'center',
                        'color': 'white',
                        'position': 'relative',
                        'zIndex': 2, # Ensures content is above the overlay
                        'padding': '0 20px',
                    },
                    children=[
                        html.Div([
                            html.H1(
                                MAIN_HEADLINE,
                                style={
                                    'fontSize': 'clamp(32px, 5vw, 60px)',
                                    'fontWeight': '900',
                                    'maxWidth': '900px',
                                    'lineHeight': '1.2',
                                    'marginBottom': '40px',
                                    'textShadow': '2px 2px 10px rgba(0,0,0,0.8)',
                                }
                            ),
                            html.A(
                                BUTTON_TEXT,
                                href="#contact",
                                style={
                                    'display': 'inline-block',
                                    'backgroundColor': 'rgba(45, 212, 191, 0.9)',
                                    'color': 'white',
                                    'border': '1px solid #2DD4BF',
                                    'padding': '15px 40px',
                                    'fontSize': '16px',
                                    'fontWeight': 'bold',
                                    'cursor': 'pointer',
                                    'borderRadius': '6px',
                                    'textDecoration': 'none',
                                    'transition': 'all 0.3s ease',
                                }
                            )
                        ])
                    ]
                ),
            ]
        ),

        # --- About Section ---
        html.Div(
            id='about',
            style={'padding': '80px 10%', 'backgroundColor': 'white', 'color': '#333'},
            children=[
                html.H2("About Beyonders.ai", style={'textAlign': 'center', 'color': '#0a192f', 'marginBottom': '40px', 'fontSize': '36px'}),
                html.P(
                    "We are a team of passionate data scientists, engineers, and strategists dedicated to unlocking the power of artificial intelligence. Our mission is to build intelligent systems that solve complex business problems, drive innovation, and create a more efficient future.",
                    style={'maxWidth': '800px', 'margin': '0 auto', 'textAlign': 'center', 'lineHeight': '1.8', 'fontSize': '18px', 'color': '#555'}
                )
            ]
        ),

        # --- Services Section ---
        html.Div(
            id='services',
            style={'padding': '80px 10%', 'backgroundColor': '#020c1b', 'color': '#ccd6f6'},
            children=[
                # Section Title
                html.H2("Our Offerings", style={'textAlign': 'center', 'color': 'white', 'marginBottom': '10px', 'fontSize': '36px', 'fontWeight': '300'}),
                html.Hr(style={'width': '70px', 'borderColor': '#ccd6f6', 'borderWidth': '1px', 'margin': '0 auto 50px auto'}),

                # Grid container for service cards
                html.Div(
                    style={'display': 'grid', 'gridTemplateColumns': 'repeat(auto-fit, minmax(300px, 1fr))', 'gap': '40px'},
                    children=[
                        # Service Card 1
                        html.Div(
                            style={'textAlign': 'center', 'padding': '20px'},
                            children=[
                                html.Img(
                                    src='https://images.pexels.com/photos/3861958/pexels-photo-3861958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                                    style={'borderRadius': '50%', 'width': '150px', 'height': '150px', 'objectFit': 'cover', 'marginBottom': '25px', 'boxShadow': '0px 10px 30px rgba(0,0,0,0.5)'}
                                ),
                                html.H3("SAR Agent", style={'color': 'white', 'marginBottom': '10px', 'fontWeight': '400'}),
                                html.Hr(style={'width': '50px', 'borderColor': '#1e2d4a', 'borderWidth': '1px', 'margin': '0 auto 15px auto'}),
                                html.P(
                                    "Search And Recommendation agent is an AI powered search engine which converts.",
                                    style={'fontSize': '16px', 'lineHeight': '1.7', 'color': '#8892b0'}
                                )
                            ]
                        ),
                        # Service Card 2
                        html.Div(
                            style={'textAlign': 'center', 'padding': '20px'},
                            children=[
                                html.Img(
                                    src='https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                                    style={'borderRadius': '50%', 'width': '150px', 'height': '150px', 'objectFit': 'cover', 'marginBottom': '25px', 'boxShadow': '0px 10px 30px rgba(0,0,0,0.5)'}
                                ),
                                html.H3("SEM Agent", style={'color': 'white', 'marginBottom': '10px', 'fontWeight': '400'}),
                                html.Hr(style={'width': '50px', 'borderColor': '#1e2d4a', 'borderWidth': '1px', 'margin': '0 auto 15px auto'}),
                                html.P(
                                    "Our team is made up of highly skilled and experienced professionals who are passionate about IT.",
                                    style={'fontSize': '16px', 'lineHeight': '1.7', 'color': '#8892b0'}
                                )
                            ]
                        ),
                        # Service Card 3
                        html.Div(
                            style={'textAlign': 'center', 'padding': '20px'},
                            children=[
                                html.Img(
                                    src='https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                                    style={'borderRadius': '50%', 'width': '150px', 'height': '150px', 'objectFit': 'cover', 'marginBottom': '25px', 'boxShadow': '0px 10px 30px rgba(0,0,0,0.5)'}
                                ),
                                html.H3("AI Services", style={'color': 'white', 'marginBottom': '10px', 'fontWeight': '400'}),
                                html.Hr(style={'width': '50px', 'borderColor': '#1e2d4a', 'borderWidth': '1px', 'margin': '0 auto 15px auto'}),
                                html.P(
                                    "We offer a wide range of IT services, including software development, web design, and cloud computing.",
                                    style={'fontSize': '16px', 'lineHeight': '1.7', 'color': '#8892b0'}
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # --- Contact Section ---
        html.Div(
            id='contact',
            style={'padding': '80px 10%', 'backgroundColor': 'white', 'color': '#333', 'textAlign': 'center'},
            children=[
                html.H2("CONTACT Us", style={'fontSize': '36px', 'marginBottom': '10px', 'color': '#4a4a4a', 'fontWeight': '300', 'letterSpacing': '1px'}),
                html.Hr(style={'width': '50px', 'borderColor': '#ccc', 'borderWidth': '1px', 'margin': '0 auto 50px auto'}),
                html.Div(
                    style={'maxWidth': '600px', 'margin': '0 auto', 'textAlign': 'left'},
                    children=[
                        dcc.Input(placeholder="Name*", style={'width': '100%', 'padding': '12px', 'marginBottom': '20px', 'borderRadius': '4px', 'border': '1px solid #ccc', 'boxSizing': 'border-box'}),
                        dcc.Input(placeholder="Email*", type='email', style={'width': '100%', 'padding': '12px', 'marginBottom': '20px', 'borderRadius': '4px', 'border': '1px solid #ccc', 'boxSizing': 'border-box'}),
                        dcc.Input(placeholder="Mobile*", type='tel', style={'width': '100%', 'padding': '12px', 'marginBottom': '20px', 'borderRadius': '4px', 'border': '1px solid #ccc', 'boxSizing': 'border-box'}),
                        dcc.Textarea(placeholder="Tell us about your project", style={'width': '100%', 'height': '150px', 'padding': '12px', 'marginBottom': '20px', 'borderRadius': '4px', 'border': '1px solid #ccc', 'boxSizing': 'border-box'}),
                        html.Button(
                            "SEND",
                            style={
                                'backgroundColor': '#4a4a4a',
                                'color': 'white',
                                'border': 'none',
                                'padding': '15px 40px',
                                'fontSize': '16px',
                                'fontWeight': 'bold',
                                'cursor': 'pointer',
                                'borderRadius': '4px',
                                'display': 'block',
                                'margin': '0 auto'
                            }
                        )
                    ]
                )
            ]
        ),

        # --- Footer ---
        html.Footer(
            style={'padding': '20px 10%', 'backgroundColor': '#020c1b', 'color': '#ccd6f6', 'textAlign': 'center', 'borderTop': '1px solid rgba(255, 255, 255, 0.1)'},
            children=[
                html.P("© 2025 Beyonders.ai. All Rights Reserved.", style={'margin': 0})
            ]
        )
    ]
)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)

