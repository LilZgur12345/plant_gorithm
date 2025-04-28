from dash import html, dcc

def landing_page_layout():
    """Creates the layout for the landing page."""
    return html.Div([
        html.H1("🪴 Welcome to the Plant-gorithm! 🪴"),
        html.Hr(),
        html.P("Answer the following questions, and we'll suggest houseplants that fit you and your space."),
        html.Img(
            src='/assets/plants2.jpg', 
            alt='Housplants', 
            style={ 
                'height': '500px', 
                'width': 'auto', 
                'display': 'block',
                # Left-aligned  
                'margin-left': '0', 
                'margin-right': 'auto',
                'margin-top': '25px',   
                'margin-bottom': '25px'
            }
        ),
        html.Br(),
        # Button triggers the form page
        html.Button("Get Plant Suggestions", id='start-button', n_clicks=0,
        style={ 
                'padding': '8px 30px',   
                'font-size': '18px',     
                'cursor': 'pointer',     
                'border-radius': '1px',   
                'border': '3px solid black'
            }
        )
        ],
        style={ 
           'background-color': '#adc96c',
           'padding': '20px', 
       })

def form_page_layout():
    """Creates the layout for the preferences form page."""

    # Form page layout with user preferences
    return html.Div([
        html.H1("Enter Your Preferences"),
        html.Br(),
        
        # Sunlight Preference
        html.Label("Choose how much sun your space gets:"),
        html.Img(
            src='/assets/Sunlight.png', 
            alt='Sunlight Map', 
            style={ 
                'height': '250px', 
                'width': 'auto', 
                'display': 'block',
                # Left-aligned
                'margin-left': '0',   
                'margin-right': 'auto',
                'margin-top': '25px',   
                'margin-bottom': '25px'
            }
        ),
        dcc.RadioItems(
            id='sunlight',
            options=[
                # Values match 'light' column in data 
                {'label': 'Strong Light', 'value': 'Strong Light'},
                {'label': 'Full Sun', 'value': 'Full Sun'} # Add more if needed
            ],
            value='Strong Light', # Default value
            labelStyle={'display': 'block'}
        ),
        html.Br(),

        # Watering Preference
        html.Label("How much watering do you want to do?"),
        dcc.Dropdown(
            id='watering',
            options=[
                # Values match 'water' column in data
                {'label': 'Must Not Dry Between Waterings', 'value': 'Must Not Dry Between Waterings'},
                {'label': 'Can Dry Between Waterings', 'value': 'Can Dry Between Waterings'},
                {'label': 'Water When Half Dry', 'value': 'Water When Half Dry'},
                {'label': 'Water Only When Dry', 'value': 'Water Only When Dry'}
            ],
            value='Water When Half Dry', # Default value
            clearable=False 
        ),
        html.Br(),

        html.Label("How Big Do You Want Your Plant to Get?"),
        dcc.RadioItems(
            id='max-size',
            options=[
                {'label': 'Small (< 1 meter)', 'value': 'small'},
                {'label': 'Medium (1 - 5 meters)', 'value': 'medium'},
                {'label': 'Large (> 5 meters)', 'value': 'large'} 
            ],
            value='medium', # Default value
            labelStyle={'display': 'block'}
        ),
        html.Br(),

        # Rarity Preference
        html.Label("How rare would you like your plant to be?"),
        dcc.Dropdown(
            id='rarity',
            options=[
                 # Values match 'availability' column data
                {'label': 'Regular', 'value': 'Regular'},
                {'label': 'Seasonal', 'value': 'Seasonal'},
                {'label': 'More or Less Rare', 'value': 'More or Less Rare'}, 
                {'label': 'Sporadic', 'value': 'Sporadic'},
                {'label': 'Rare', 'value': 'Rare'}
            ],
            value='Regular', # Default value
            clearable=False
        ),
        html.Br(),

        # Appeal Preference
        html.Label("What should the plant's best feature be?"),
        dcc.Dropdown(
            id='appeal',
            options=[
                # Values match 'appeal' column in data
                {'label': 'Flower', 'value': 'Flower'},
                {'label': 'Foliage', 'value': 'Foliage'},
                {'label': 'Style', 'value': 'Style'},
                {'label': 'Color', 'value': 'Color'}, 
                {'label': 'Trunc', 'value': 'Trunc'}, 
                {'label': 'Bearing', 'value': 'Bearing'},
                {'label': 'Robustness', 'value': 'Robustness'} 
            ],
            value='Foliage', # Default value
            clearable=False
        ),
        html.Br(),

        # Button triggers the 'suggestions' callback 
        html.Button('Get Suggestions', id='submit-button', n_clicks=0,
        style={ 
                'padding': '8px 30px',   
                'font-size': '18px',     
                'cursor': 'pointer',     
                'border-radius': '1px',   
                'border': '3px solid black'
            }
        ),
        html.Br(),
        html.Hr(), # Separator before results
        html.Div(id='results-container'),
        html.Br(),

        # Back to home link
        dcc.Link('← Back to Home', href='/')
    ],
        style={
           'background-color': '#adc96c',
           'padding': '20px', 
       })

