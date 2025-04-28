import pandas as pd

def load_data() -> pd.DataFrame:
    file_path = "/Users/lilyzgurzynski/Desktop/plant_data404.xlsx"
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred loading data: {e}")

def filter_plants(df: pd.DataFrame, preferences: dict) -> pd.DataFrame:
    """
    Filters the plant DataFrame based on user preferences.

    Args:
        df: The input DataFrame of plants.
        preferences: A dictionary containing user preferences.
                     Expected keys: 'sunlight', 'watering', 'size',
                                    'rarity', 'appeal'
                     'size' is expected to be 'small', 'medium', or 'large'.

    Returns:
        A filtered DataFrame
    """
    # Make a copy to avoid modifying the original DataFrame
    df_filtered = df.copy()

    # Filter by data columns
    if 'sunlight' in preferences and preferences['sunlight']:
        sunlight_preference = str(preferences['sunlight'])
        df_filtered = df_filtered[df_filtered['light'].str.contains(sunlight_preference, case=False, na=False)]

    if 'watering' in preferences and preferences['watering']:
        watering_preference = str(preferences['watering'])
        df_filtered = df_filtered[df_filtered['water'].str.contains(watering_preference, case=False, na=False)]

    if 'rarity' in preferences and preferences['rarity']:
        rarity_preference = str(preferences['rarity'])
        df_filtered = df_filtered[df_filtered['availability'].str.contains(rarity_preference, case=False, na=False)]

    if 'appeal' in preferences and preferences['appeal']:
        appeal_preference = str(preferences['appeal'])
        df_filtered = df_filtered[df_filtered['appeal'].str.contains(appeal_preference, case=False, na=False)]

    # Filter by Max Height
    if 'size' in preferences and preferences['size'] and 'max_height' in df_filtered.columns:
        size_preference = preferences['size']
        # Ensure max_height is numeric, handle potential NaNs
        df_filtered = df_filtered.dropna(subset=['max_height']) # Remove rows where height is unknown

        if size_preference == 'small':
            # Max height less than 1 meter
            df_filtered = df_filtered[df_filtered['max_height'] < 1.0]
        elif size_preference == 'medium':
            # Max height between 1 and 5 meter (inclusive)
            df_filtered = df_filtered[(df_filtered['max_height'] >= 1.0) & (df_filtered['max_height'] <= 5.0)]
        elif size_preference == 'large':
            df_filtered = df_filtered[df_filtered['max_height'] > 5.0]
            # Max height greater than 5 meters

    return df_filtered
