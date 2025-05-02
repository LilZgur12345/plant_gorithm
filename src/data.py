import pandas as pd
import os

# Load the data from the Excel file
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, "plantdata.xlsx")

try:
    df = pd.read_excel(file_path)
# If not found, raise an error
except FileNotFoundError:
    raise FileNotFoundError(f"File not found at: {file_path}")
except Exception as e:
    raise Exception(f"An error occurred loading data: {e}")