from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from src.analysis import filter_plants, load_data
from src.components import landing_page_layout, form_page_layout

# Creating the Dash app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks="initial_duplicate"
)
app.title = 'Plantgorithm'

# Main layout structure
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Landing page layout
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/form':
        # Return the layout defined in components.py
        return form_page_layout()
    # Default to landing page
    return landing_page_layout()

# Redirect to Form Page
@app.callback(
    Output('url', 'pathname', allow_duplicate=True), 
    Input('start-button', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_form(n_clicks):
    if n_clicks and n_clicks > 0: # Check if button was clicked
        return '/form'
    return None 

@app.callback(
    # Update the results-container which IS PART of form_page_layout
    Output('results-container', 'children'),
    # Triggered by the submit button on the form page
    Input('submit-button', 'n_clicks'),
    # Get the current values from the form components
    State('sunlight', 'value'),
    State('watering', 'value'),
    State('max-size', 'value'), # Corrected ID from components.py
    State('rarity', 'value'),
    State('appeal', 'value'),
    prevent_initial_call=True # Don't run on page load
)
def show_plant_suggestions(n_clicks, sunlight, watering, max_size, rarity, appeal):
    if n_clicks is None or n_clicks == 0:
        return [] # Return empty list if button is not clicked

    # Construct preferences dictionary
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

        if filtered_df.empty:
            return dbc.Alert("No matching plants found based on your selections. Try relaxing your criteria!", color="warning")

        results = []
        for _, row in filtered_df.iterrows():
            # Using dbc.Card for better styling with Bootstrap
            card = dbc.Card([
                # Use row.get('column_name', default_value) for safety
                dbc.CardImg(src=row.get('image', '/assets/placeholder.png'), top=True, style={'height':'200px', 'object-fit': 'cover'}), # Added style
                dbc.CardBody([
                    html.H4(row.get('common_name', 'Unknown'), className='card-title'),
                    html.P(f"Scientific Name: {row.get('scientific_name', 'N/A')}", className="card-text"),
                    html.P(f"Family: {row.get('family', 'N/A')}", className="card-text"),
                    html.P(f"Type: {row.get('type', 'N/A')}", className="card-text"),
                    html.P(f"Max Height: {row.get('max_height', 'N/A')}m", className="card-text"), # Show max height
                    html.P(f"Sunlight: {row.get('light', 'N/A')}", className="card-text"),
                    html.P(f"Watering: {row.get('water', 'N/A')}", className="card-text"),
                    html.P(f"Growth Rate: {row.get('growth_rate', 'N/A')}", className="card-text"),
                    html.P(f"Climate: {row.get('climate', 'N/A')}", className="card-text"),
                    html.P(f"Origin: {row.get('origin', 'N/A')}", className="card-text"),
                    html.P(f"Hardiness Zone: {row.get('hardiness_zone', 'N/A')}", className="card-text"),
                ])
            ], style={"width": "18rem", "margin": "10px"}) # Basic card styling

            results.append(card)

        # Arrange query results in a row using dbc.Row for better layout control
        # Use 'justify="center"' to center the cards if they don't fill the row
        return dbc.Row(results, justify="center")

    except FileNotFoundError as e:
        return dbc.Alert(f"Error loading data: {e}", color="danger")
    except Exception as e:
        # Raise an error if something goes wrong
        print(f"Error during suggestion generation: {e}")
        return dbc.Alert(f"An error occurred while generating suggestions: {e}", color="danger")


# Run the app
if __name__ == '__main__':
    app.run(debug=True)