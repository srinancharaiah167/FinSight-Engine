import pandas as pd

# The file you uploaded is an Excel file
FILE_NAME = 'bank (1).xlsx'

try:
    # Use pd.read_excel() to read .xlsx files
    df = pd.read_excel(FILE_NAME)

    print("--- 1. First 5 Rows (SUCCESS!) ---")
    print(df.head())

    print("\n--- 2. Column Names and Data Types ---")
    df.info()

except FileNotFoundError:
    print(f"Error: Could not find the file '{FILE_NAME}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Did you remember to run 'pip install openpyxl'?")
    