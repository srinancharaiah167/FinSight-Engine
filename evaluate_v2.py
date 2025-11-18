import pandas as pd
from sklearn.metrics import classification_report, f1_score
import pickle

# --- Configuration ---
# Change this
TEST_FILE = 'test_v2.csv' 
# Change this
DESCRIPTION_COLUMN = 'description' 
# Change this
CATEGORY_COLUMN = 'category'
# Change this
MODEL_FILE = 'model_v2.pkl'
# ---------------------

print("Loading the trained model...")
try:
    # 'rb' means 'read binary'
    with open(MODEL_FILE, 'rb') as f:
        ml_pipeline = pickle.load(f)
except FileNotFoundError:
    print(f"Error: {MODEL_FILE} not found. Run train.py first!")
    exit()

print("Loading test data...")
try:
    test_df = pd.read_csv(TEST_FILE)
    test_df = test_df.dropna(subset=[DESCRIPTION_COLUMN, CATEGORY_COLUMN])
    
    X_test = test_df[DESCRIPTION_COLUMN]
    y_test = test_df[CATEGORY_COLUMN]
    print(f"Loaded {len(y_test)} test rows.")

except FileNotFoundError:
    print(f"Error: {TEST_FILE} not found. Did the DRE run their script?")
    exit()

# 1. Make Predictions
print("Making predictions on test data...")
y_pred = ml_pipeline.predict(X_test)

# 2. Evaluate
print("\n--- CLASSIFICATION REPORT ---")
# This report shows you everything!
print(classification_report(y_test, y_pred))

# 3. Check the specific hackathon requirement
# 'macro' means it averages the F1-score for all categories,
# which is what the judges are looking for.
macro_f1 = f1_score(y_test, y_pred, average='macro')

print(f"Macro F1-Score: {macro_f1:.4f}")

if macro_f1 > 0.90:
    print("Model is above the 0.90 target.")
else:
    print("Model is below the 0.90 target. We may need to tune it.")
