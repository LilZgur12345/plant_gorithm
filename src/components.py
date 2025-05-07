from dash import html, dcc
import dash_bootstrap_components as dbc

def landing_page_layout() -> html.Div:
    """
    Creates the layout for the landing page with Bootstrap's Minty theme
    
    Returns:
        html.Div: The landing page layout details/components in a div
    """
    return html.Div([
        html.Div([
            # Header and brief description
            html.H1("🪴 Welcome to the Plant-gorithm! 🪴", className = "display-4 text-center mb-4"),
            html.P("Answer the following questions, and we'll suggest houseplants that fit you and your space", className="lead text-center"),
            html.Hr(),
            # Stock image and button
            html.Img(
                src='/assets/Plants.jpg',
                alt='Houseplants',
                className="img-fluid rounded mx-auto d-block my-4",
                style={'maxHeight': '500px'}
            ),
            html.Br(),
            dbc.Button(
                "Get Plant Suggestions",
                id='start-button',
                n_clicks=0,
                color="success",
                size="lg" ,
                className="d-block mx-auto mt-4"
            )
        ], 
        className = "p-4"),
    ],
    # Style choices for the landing page - background color & thick border with round edges
    className="border border-5 border-success rounded",
    style={
        'backgroundColor': '#e6f9ec', 
        'minHeight': '100vh',
        'padding': '1rem',
        'margin': '0',
        'boxSizing': 'border-box'
       })

def form_page_layout() -> html.Div:
    """
    Creates the layout for the preferences form page with Bootstrap's Minty theme
    
    Returns:
        html.Div: The form page layout details/components/user preferences in a div
    """

    # Form page layout with user preferences
    return html.Div([
        html.H1("Enter Your Preferences:", className="mb-4"),
        html.Br(),

        # Sunlight Preference
        html.Label("How much sun does your space get?"),
        html.Br(),
        html.Br(),

        # ArcGIS Pro map - InstantApp format
        html.Iframe(
            src="https://wm-gis.maps.arcgis.com/apps/instant/basic/index.html?appid=39b2ee93a246491f9274e379dd8f98ad",
            width="100%",
            height="500",
            style={"border": "2px solid #28a745", "borderRadius": "10px", "marginBottom": "20px"}
        ),
        
        dbc.RadioItems( 
            id='sunlight',
            options=[
                {'label': 'Strong Light', 'value': 'Strong Light'},
                {'label': 'Full Sun', 'value': 'Full Sun'}
            ],
            # Default value
            value='Strong Light',
            # Centered to align with map and other text
            inline=True,
            className="justify-content-center mb-3"
        ),
        html.Br(),

        # Watering Preference
        html.Label("How much watering do you want to do?"),
        dcc.Dropdown(
            id='watering',
            options=[
                {'label': 'Must Not Dry Between Waterings', 'value': 'Must Not Dry Between Waterings'},
                {'label': 'Can Dry Between Waterings', 'value': 'Can Dry Between Waterings'},
                {'label': 'Water When Half Dry', 'value': 'Water When Half Dry'},
                {'label': 'Water Only When Dry', 'value': 'Water Only When Dry'}
            ],
            value='Water When Half Dry',
            clearable=False,
            className="mb-3",
            style={'margin': '0 auto', 'width': '300px'}
        ),
        html.Br(),

        # Max Size Preference
        html.Label("How Big Do You Want Your Plant to Get?"),
        dbc.RadioItems(
            id='max-size',
            options=[
                {'label': 'Small (< 1 meter)', 'value': 'small'},
                {'label': 'Medium (1 - 5 meters)', 'value': 'medium'},
                {'label': 'Large (> 5 meter)', 'value': 'large'}
            ],
            value='medium',
            className="mb-3 justify-content-center",
            labelStyle={'display': 'block', 'textAlign': 'center'},
            style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
        ),
        html.Br(),

        # Availability/Rarity Preference
        html.Label("How rare would you like your plant to be?"),
        dcc.Dropdown(
            id='rarity',
            options=[
                {'label': 'Regular', 'value': 'Regular'},
                {'label': 'Seasonal', 'value': 'Seasonal'},
                {'label': 'More or Less Rare', 'value': 'More or Less Rare'},
                {'label': 'Sporadic', 'value': 'Sporadic'},
                {'label': 'Rare', 'value': 'Rare'}
            ],
            value='Regular',
            clearable=False,
            className="mb-3",
            style={'margin': '0 auto', 'width': '300px'}
        ),
        html.Br(),

        # Appeal Preference
        html.Label("What should the plant's best feature be?"),
        dcc.Dropdown(
            id='appeal',
            options=[
                {'label': 'Flower', 'value': 'Flower'},
                {'label': 'Foliage', 'value': 'Foliage'},
                {'label': 'Style', 'value': 'Style'},
                {'label': 'Color', 'value': 'Color'},
                {'label': 'Trunc', 'value': 'Trunc'},
                {'label': 'Bearing', 'value': 'Bearing'},
                {'label': 'Robustness', 'value': 'Robustness'}
            ],
            value='Foliage',
            clearable=False,
            className="mb-4",
            style={'margin': '0 auto', 'width': '300px'}
        ),
        html.Br(),

        # Button to submit preferences and filter plants
        dbc.Button(
            "Get Suggestions",
            id='submit-button',
            n_clicks=0,
            color="primary", 
            size="lg", 
            className="mx-auto d-block mb-4"
        ),
     
        html.Br(),
        html.Hr(), 
        html.Div(id='results-container', className="mt-4"),
        html.Br(),

        # Link to go back to the landing page
        html.Div([
            dcc.Link('← Back to Home', href='/', className="btn btn-link")
        ],  className="text-center")
    ],
    className="border border-success border-5 rounded text-center",

    # Style choices for the form page - background color & thick border with round edges
    style={
        'backgroundColor': '#e6f9ec',
        'minHeight': '100vh',
        'margin': '0',
        'padding': '20px',
        'boxSizing': 'border-box'
       })
