from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from src.filtering import filter_plants, load_data
from src.components import landing_page_layout, form_page_layout

# Creating the Dash app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY],
    suppress_callback_exceptions=True,
    # Prevents duplicate callbacks being triggered
    prevent_initial_callbacks="initial_duplicate"
)
app.title = 'Plantgorithm'

# Overall app layout (landing and form pages)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='landing-page', children=landing_page_layout()),
    html.Div(id='form-page', children=form_page_layout())
])

# Landing page layout
@app.callback(
    Output('landing-page', 'style'),
    Output('form-page', 'style'),
    Input('url', 'pathname')
)
# 
def navigate_pages(pathname) -> tuple:
    """
    Allows user to navigate between the landing and form pages

    Args:
        pathname (str): The current URL path

    Returns:
        tuple: The styles/display properties for the landing and form pages
    """
    if pathname == '/form':
        return {'display': 'none'}, {'display': 'block'}
    # Default to the landing page
    return {'display': 'block'}, {'display': 'none'}

def display_page(pathname) ->  html.Div:
    """
    Displays either the landing or form page based on the URL path

    Args:
        pathname (str): The current URL path
    
    Returns:
        html.Div: The layout of the page to be displayed
    """
    if pathname == '/form':
        # Return the form page
        return form_page_layout()
    # Return the landing page
    return landing_page_layout()

# Redirect to Form Page
@app.callback(
    Output('url', 'pathname', allow_duplicate=True), 
    Input('start-button', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_form(n_clicks) -> str:
    """
    Brings user to the form page when they click the button

    Args:
        n_clicks (int): Number of button clicks

    Returns:
        str: URL path to the form page
    """
    if n_clicks and n_clicks > 0: # Check if button was clicked
        return '/form' 
    return None 

@app.callback(
    # Update results-container with filtered suggestions
    Output('results-container', 'children'),
    Input('submit-button', 'n_clicks'),
    # Get the current values of the dropdown menus/radio buttons
    State('sunlight', 'value'),
    State('watering', 'value'),
    State('max-size', 'value'),
    State('rarity', 'value'),
    State('appeal', 'value'),
    prevent_initial_call=True # Don't run on initial load
)
def show_plant_suggestions(n_clicks, sunlight, watering, max_size, rarity, appeal) -> html.Div:
    """
    Generates houseplant suggestions based on the user's preferences

    Args:
        sunlight (str): Sunlight preference
        watering (str): Watering preference
        max_size (str): Maximum size preference
        rarity (str): Rarity/availability preference
        appeal (str): Appeal preference

    Returns:
        html.Div: A div containing the filtered plant suggestions
    """
    preferences = {
        'sunlight': sunlight,
        'watering': watering,
        'size': max_size,
        'rarity': rarity,
        'appeal': appeal
    }

    try:
        # Load the dataset and filter based on user preferences
        df = load_data()
        filtered_df = filter_plants(df, preferences)

        # If the data frame is empty, there were no matches
        if filtered_df.empty:
            return dbc.Alert("No matching plants found — try changing your criteria!", color="warning")

        results = []
        for _, row in filtered_df.iterrows():
            # Use dbc.Card for better styling with Bootstrap
            card = dbc.Card([
                # Display Tropicopia images
                dbc.CardImg(src=row.get('image', '/assets/placeholder.png'), top=True, style={'height':'200px', 'object-fit': 'cover'}),
                dbc.CardBody([
                    # Plant care and origin information
                    html.H4(row.get('common_name', 'Unknown'), className='card-title'),
                    html.P(f"Scientific Name: {row.get('scientific_name', 'N/A')}", className="card-text"),
                    html.P(f"Family: {row.get('family', 'N/A')}", className="card-text"),
                    html.P(f"Type: {row.get('type', 'N/A')}", className="card-text"),
                    html.P(f"Max Height: {row.get('max_height', 'N/A')}m", className="card-text"),
                    html.P(f"Sunlight: {row.get('light', 'N/A')}", className="card-text"),
                    html.P(f"Watering: {row.get('water', 'N/A')}", className="card-text"),
                    html.P(f"Growth Rate: {row.get('growth_rate', 'N/A')}", className="card-text"),
                    html.P(f"Climate: {row.get('climate', 'N/A')}", className="card-text"),
                    html.P(f"Origin: {row.get('origin', 'N/A')}", className="card-text"),
                    html.P(f"Hardiness Zone: {row.get('hardiness_zone', 'N/A')}", className="card-text"),
                ])
            ], style={"width": "18rem", "margin": "10px"}) # Basic card styling

            results.append(card)
        # Bootstrap row for layout
        return dbc.Row(results, justify="center")

    except FileNotFoundError as e:
        return dbc.Alert(f"Error loading data: {e}", color="danger")
    except Exception as e:
        # Raise an error if something goes wrong
        print(f"Error during plant suggestion generation: {e}")
        return dbc.Alert(f"An error occurred while generating suggestions: {e}", color="danger")

# Run the app
if __name__ == '__main__':
    app.run(debug=False)