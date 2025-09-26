import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# --- APP INITIALIZATION ---
# Initialize the Dash app with a dark theme from dash-bootstrap-components and Font Awesome for icons.
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, "https://use.fontawesome.com/releases/v5.15.4/css/all.css"], suppress_callback_exceptions=True)
server = app.server
app.title = "Beyonders AI"

# --- REUSABLE COMPONENTS ---

# Navigation Bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.NavItem(dbc.NavLink("Services", href="/services")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        dbc.Button("Get Started", color="primary", className="ms-2", href="/contact"),
    ],
    brand="Beyonders AI",
    brand_href="/",
    color="dark",
    dark=True,
    className="fixed-top", # Make navbar sticky
)

# Footer
footer = html.Footer(
    dbc.Container(
        dbc.Row(
            dbc.Col(
                html.P("© 2024 Beyonders AI. All Rights Reserved.", className="text-center text-muted mt-4 mb-2")
            )
        )
    )
)

# --- PAGE LAYOUTS ---

# Home Page Layout
home_layout = html.Div([
    # Hero Section
    dbc.Container(
        className="text-center my-5 py-5",
        # style={},
        children=[
            html.H1("We are the BEYONDERS", className="display-3 fw-bold text-light"),
            html.P("The future of AI is here.", className="lead text-muted"),
            dbc.Button("Get Started", color="primary", size="lg", className="mt-3", href="/contact"),
        ],
        fluid=True,
        # This style simulates a background image effect.
        style={
            "background": "linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(https://placehold.co/1600x900/000000/FFFFFF?text=AI+Concept)",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "color": "white",
            "minHeight": "80vh",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center",
            "paddingTop": "10rem", "paddingBottom": "10rem"
        }
    ),

    # Who Are We Section
    dbc.Container(
        className="py-5",
        children=[
            html.H2("WHO ARE WE?", className="text-center mb-4"),
            html.P(
                "We are a team of passionate AI engineers, data scientists, and business strategists dedicated to helping businesses leverage the power of artificial intelligence. Our mission is to provide innovative AI solutions that drive growth, efficiency, and transformation.",
                className="text-center lead text-muted"
            ),
        ],
    ),

    # What We Do Section
    dbc.Container(
        className="py-5 bg-light text-dark rounded p-5",
        children=[
            html.H2("WHAT WE DO?", className="text-center mb-5"),
            dbc.Row([
                dbc.Col(html.Div([
                    html.I(className="fas fa-brain fa-3x mb-3 text-primary"),
                    html.H4("AI Model Training"),
                    html.P("Custom AI models tailored to your specific business needs and data.")
                ], className="text-center"), md=4),
                dbc.Col(html.Div([
                    html.I(className="fas fa-cogs fa-3x mb-3 text-primary"),
                    html.H4("Business Automation"),
                    html.P("Automate repetitive tasks and workflows to increase efficiency.")
                ], className="text-center"), md=4),
                dbc.Col(html.Div([
                    html.I(className="fas fa-comments fa-3x mb-3 text-primary"),
                    html.H4("AI Chatbot Development"),
                    html.P("Intelligent chatbots to enhance customer engagement and support.")
                ], className="text-center"), md=4),
            ]),
        ],
        fluid=True
    ),

    # Why Us Section
    dbc.Container(
        className="py-5",
        children=[
            html.H2("WHY US?", className="text-center mb-5"),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("Cost Effective", className="card-title"),
                        html.P("Affordable AI solutions without compromising on quality.")
                    ])
                ], color="dark"), md=4, className="mb-4"),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("Time Efficiency", className="card-title"),
                        html.P("Rapid development and deployment cycles to get you to market faster.")
                    ])
                ], color="dark"), md=4, className="mb-4"),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("Data Security", className="card-title"),
                        html.P("Robust security protocols to ensure your data is always safe.")
                    ])
                ], color="dark"), md=4, className="mb-4"),
            ]),
        ],
    ),
])

# About Page Layout
about_layout = dbc.Container(
    className="py-5 mt-5",
    children=[
        html.H1("About Us", className="display-4 text-center my-5"),
        dbc.Row([
            dbc.Col([
                html.P(
                    "Beyonders AI was founded on the principle that artificial intelligence should be accessible to all businesses, regardless of size. We believe in the transformative power of AI to solve complex problems, create new opportunities, and drive human progress.",
                    className="lead"
                ),
                html.P(
                    "Our team consists of industry experts with years of experience in machine learning, natural language processing, computer vision, and data analytics. We are committed to delivering cutting-edge, reliable, and scalable AI solutions that deliver measurable results.",
                    className="lead"
                ),
                html.P(
                    "Our mission is to be your trusted partner on your AI journey. We work closely with you to understand your unique challenges and goals, ensuring that the solutions we build are perfectly aligned with your vision.",
                    className="lead"
                ),
            ], md=8, className="mx-auto")
        ])
    ]
)

# Services Page Layout
services_layout = dbc.Container(
    className="py-5 mt-5",
    children=[
        html.H1("Our Services", className="display-4 text-center my-5"),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H4("AI Model Training")),
                dbc.CardBody([
                    html.P("We specialize in creating custom-built machine learning models from the ground up. Whether it's for predictive analytics, image recognition, or natural language understanding, we tailor our models to your specific datasets and objectives to ensure maximum accuracy and performance.")
                ])
            ], className="h-100"), md=6, className="mb-4"),
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H4("AI Chatbot Development")),
                dbc.CardBody([
                    html.P("Engage your customers 24/7 with intelligent, human-like chatbots. We develop and deploy sophisticated conversational AI agents that can handle customer queries, automate sales processes, and provide personalized support across your website and messaging platforms.")
                ])
            ], className="h-100"), md=6, className="mb-4"),
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H4("Business Automation")),
                dbc.CardBody([
                    html.P("Unlock new levels of productivity by automating your core business processes. We identify opportunities for automation and implement AI-driven solutions to streamline workflows, reduce manual effort, and minimize operational costs.")
                ])
            ], className="h-100"), md=6, className="mb-4"),
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H4("AI Consultancy")),
                dbc.CardBody([
                    html.P("Navigate the complexities of AI adoption with our expert guidance. We provide strategic consulting to help you identify the right AI opportunities, develop a robust AI strategy, and build a roadmap for successful implementation and integration.")
                ])
            ], className="h-100"), md=6, className="mb-4"),
        ])
    ]
)

# Contact Page Layout
contact_layout = dbc.Container(
    className="py-5 mt-5",
    children=[
        html.H1("Contact Us", className="display-4 text-center my-5"),
        dbc.Row([
            dbc.Col([
                html.H4("Get in Touch"),
                html.P("We'd love to hear from you. Fill out the form below and we'll get back to you as soon as possible."),
                dbc.Form([
                    dbc.Row([
                        dbc.Col(dbc.Label("Name"), width="auto"),
                        dbc.Col(dbc.Input(type="text", placeholder="Enter your name"), className="mb-3"),
                    ]),
                     dbc.Row([
                        dbc.Col(dbc.Label("Email"), width="auto"),
                        dbc.Col(dbc.Input(type="email", placeholder="Enter your email"), className="mb-3"),
                    ]),
                    dbc.Row([
                        dbc.Col(dbc.Label("Message"), width="auto"),
                        dbc.Col(dbc.Textarea(placeholder="Your message...", rows=5), className="mb-3"),
                    ]),
                    dbc.Button("Submit", color="primary"),
                ]),
            ], md=6),
            dbc.Col([
                html.H4("Our Information"),
                html.P([html.I(className="fas fa-map-marker-alt me-2"), " 123 AI Street, Tech City, 12345"]),
                html.P([html.I(className="fas fa-phone me-2"), " (123) 456-7890"]),
                html.P([html.I(className="fas fa-envelope me-2"), " contact@beyonders.ai"]),
            ], md=6),
        ])
    ]
)


# --- APP LAYOUT ---
# The main layout of the application. It includes the URL component for routing,
# the navbar, a container for page content, and the footer.
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'paddingTop': '56px'}), # Add padding to avoid content being hidden by fixed navbar
    footer
])


# --- CALLBACKS ---
# This callback renders the correct page layout based on the URL pathname.
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return about_layout
    elif pathname == '/services':
        return services_layout
    elif pathname == '/contact':
        return contact_layout
    else:
        return home_layout


# --- RUN SERVER ---
if __name__ == '__main__':
    app.run(debug=True)
