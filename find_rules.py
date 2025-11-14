import pandas as pd

# --- CHANGE THIS ---
# Put the *real* column name you found in Step 2 here
DESCRIPTION_COLUMN = 'TRANSACTION DETAILS'  # <-- CHANGE ME if needed
# -----------------

FILE_NAME = 'bank (1).xlsx'

# Use pd.read_excel()
df = pd.read_excel(FILE_NAME)

# Clean the text (lowercase and remove extra spaces)
# .dropna() is important to avoid errors on blank cells
clean_descriptions = df[DESCRIPTION_COLUMN].dropna().str.lower().str.strip()

# Count the most common merchants
print(f"--- Top 50 Most Common Merchants in '{DESCRIPTION_COLUMN}' ---")
top_merchants = clean_descriptions.value_counts().head(50)

print(top_merchants)

# Save this list to a file so you can look at it
top_merchants.to_csv('top_merchants_list.csv')
print("\nSaved list to 'top_merchants_list.csv'")