import pandas as pd

# The new "secret weapon" file
FILE_NAME = 'personal_finance_cleaned(train&testing).xlsx'
# Try the same encoding fix that worked before
ENCODING_TYPE = 'latin1' 

try:
    # Use the 'encoding' parameter to read the file
    df = pd.read_csv(FILE_NAME, encoding=ENCODING_TYPE)

    print("--- 1. First 5 Rows of New Dataset ---")
    print(df.head())

    print("\n--- 2. Column Names and Data Types ---")
    df.info()

except FileNotFoundError:
    print(f"Error: Could not find the file '{FILE_NAME}'.")
except Exception as e:
    print(f"An error occurred: {e}")