import pandas as pd
import json
from sklearn.model_selection import train_test_split

# --- Helper Function (from Day 3) ---
def find_category_by_rule(description):
    if not isinstance(description, str):
        return "Other"
    description_lower = description.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description_lower:
                return category
    return "Other"

# 1. Load the rules
with open('categories.json', 'r') as f:
    categories = json.load(f)

# --- 2. Process Dataset 1 (The BIG Bank File) ---
print("Processing Dataset 1: 'bank (1).xlsx'...")
df_bank = pd.read_excel('bank (1).xlsx')
df_bank['category'] = df_bank['TRANSACTION DETAILS'].apply(find_category_by_rule)
df_bank = df_bank[['TRANSACTION DETAILS', 'category']]
df_bank.rename(columns={'TRANSACTION DETAILS': 'description'}, inplace=True)
print(f"Loaded {len(df_bank)} rows from Dataset 1.")


# --- 3. Process Dataset 2 (The NEW Clean File) ---
print("Processing Dataset 2: 'personal_finance_cleaned...'")

# --- FIX 1: Change the file name ---
file_name = 'personal_finance_cleaned(train&testing).xlsx' 

try:
    # --- FIX 2: Use pd.read_excel() ---
    df_personal = pd.read_excel(file_name) 

    # --- FIX 3: Check for 'description' and 'category' columns ---
    if 'description' not in df_personal.columns or 'category' not in df_personal.columns:
        print("Error: The new Excel file does not have 'description' or 'category' columns.")
        exit()
        
    df_personal = df_personal[['description', 'category']]
    print(f"Loaded {len(df_personal)} rows from Dataset 2.")

except FileNotFoundError:
    print(f"Error: Could not find the file '{file_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Did you remember to run 'pip install openpyxl'?")
    exit()


# --- 4. Combine Them! ---
all_data = pd.concat([df_bank, df_personal])
all_data = all_data.dropna(subset=['description', 'category'])
print(f"Combined total rows: {len(all_data)}")

# --- 5. Split the NEW combined dataset ---
print("Splitting new dataset...")
train_df, test_df = train_test_split(all_data, test_size=0.2, random_state=42)

# --- 6. Save the new files ---
train_df.to_csv('train_v2.csv', index=False)
test_df.to_csv('test_v2.csv', index=False)

print("\nSUCCESS! Created 'train_v2.csv' and 'test_v2.csv'.")