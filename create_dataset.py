import pandas as pd
import json
from sklearn.model_selection import train_test_split

# --- Configuration ---
FILE_NAME = 'bank (1).xlsx'
DESCRIPTION_COLUMN = 'TRANSACTION DETAILS' # From your Day 2 discovery
# ---------------------

def find_category_by_rule(description):
    """
    This is the same logic from app.py. It scans the description
    for keywords from our rules.
    """
    if not isinstance(description, str):
        return "Other"
        
    description_lower = description.lower()
    
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description_lower:
                return category # Found a match!
                
    return "Other" # No match found

# 1. Load the categories.json rules
try:
    with open('categories.json', 'r') as f:
        categories = json.load(f)
    print("Loaded categories.json successfully.")
except Exception as e:
    print(f"Error loading categories.json: {e}")
    categories = {}

# 2. Load the main Excel file
print(f"Loading Excel file: {FILE_NAME}...")
df = pd.read_excel(FILE_NAME)
print("Excel file loaded.")

# 3. Create the 'Category' column
print("Creating 'Category' column using rules...")
df['Category'] = df[DESCRIPTION_COLUMN].apply(find_category_by_rule)

# 4. Filter for ML Training
# We only need two columns: the description (X) and the category (y)
# .dropna() removes any rows where the description was blank
ml_df = df[[DESCRIPTION_COLUMN, 'Category']].dropna()

# Let's see what our new labeled dataset looks like
print("\n--- New Labeled Dataset (Top 5 Rows) ---")
print(ml_df.head())

print("\n--- Category Distribution ---")
print(ml_df['Category'].value_counts())

# 5. Split the data
# We'll split 80% for training, 20% for testing
train_df, test_df = train_test_split(ml_df, test_size=0.2, random_state=42)

print(f"\nTotal rows: {len(ml_df)}")
print(f"Training rows: {len(train_df)}")
print(f"Testing rows: {len(test_df)}")

# 6. Save the files
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

print("\nSUCCESS! Created 'train.csv' and 'test.csv'.")