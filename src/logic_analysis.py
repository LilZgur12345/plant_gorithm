import pandas as pd
import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

from data import df 

def load_data() -> pd.DataFrame:
    """
    Loads the data frame from data.py

    Returns:
        pd.DataFrame: The plant data frame (df)
    """
    return df

def filter_plants(df: pd.DataFrame, preferences: dict) -> pd.DataFrame:
    """
    Filters the plant data frame based on user-inputted preferences

    Args:
        df (pd.DataFrame): The plant data frame
        preferences (dict): User-inputted preferences for filtering
    
    Returns:
        pd.DataFrame: The filtered data frame
    """
    # First make a copy to avoid changing the original data frame
    df_filtered = df.copy()

    # Filter by 'light' data column
    if 'sunlight' in preferences and preferences['sunlight']:
        sunlight_preference = str(preferences['sunlight'])
        # Ensure the column exists/is not empty
        df_filtered = df_filtered[df_filtered['light'].str.contains(sunlight_preference, case=False, na=False)]
    
    # Filter by 'water' data column
    if 'watering' in preferences and preferences['watering']:
        watering_preference = str(preferences['watering'])
        df_filtered = df_filtered[df_filtered['water'].str.contains(watering_preference, case=False, na=False)]

    # Filter by 'availability' data column
    if 'rarity' in preferences and preferences['rarity']:
        rarity_preference = str(preferences['rarity'])
        df_filtered = df_filtered[df_filtered['availability'].str.contains(rarity_preference, case=False, na=False)]

    # Filter by 'appeal' data column
    if 'appeal' in preferences and preferences['appeal']:
        appeal_preference = str(preferences['appeal'])
        df_filtered = df_filtered[df_filtered['appeal'].str.contains(appeal_preference, case=False, na=False)]

    # Filter by 'max_height' data column
    if 'size' in preferences and preferences['size'] and 'max_height' in df_filtered.columns:
        size_preference = preferences['size']
        # Ensure max_height is numeric/handle null or unknown values
        df_filtered = df_filtered.dropna(subset=['max_height']) 

        if size_preference == 'small':
            # Max height less than 1 meter
            df_filtered = df_filtered[df_filtered['max_height'] < 1.0]
        elif size_preference == 'medium':
            # Max height between 1 and 5 meter (inclusive)
            df_filtered = df_filtered[(df_filtered['max_height'] >= 1.0) & (df_filtered['max_height'] <= 5.0)]
        elif size_preference == 'large':
            # Max height greater than 5 meters
            df_filtered = df_filtered[df_filtered['max_height'] > 5.0]
            
    return df_filtered
