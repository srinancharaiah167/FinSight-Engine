import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import pickle

# --- Configuration ---
TRAIN_FILE = 'train.csv'
DESCRIPTION_COLUMN = 'TRANSACTION DETAILS'
CATEGORY_COLUMN = 'Category'
MODEL_FILE = 'model.pkl' # This is our output
# ---------------------

print(f"Loading training data from {TRAIN_FILE}...")
try:
    # Load the training data created by the DRE
    train_df = pd.read_csv(TRAIN_FILE)
    
    # Handle any potential blank rows that might have slipped through
    train_df = train_df.dropna(subset=[DESCRIPTION_COLUMN, CATEGORY_COLUMN])

    X_train = train_df[DESCRIPTION_COLUMN]
    y_train = train_df[CATEGORY_COLUMN]
    
    print(f"Loaded {len(y_train)} training rows.")

except FileNotFoundError:
    print(f"Error: {TRAIN_FILE} not found. Did the DRE run their script?")
    exit()
except Exception as e:
    print(f"Error loading data: {e}")
    exit()


# 2. Define the ML Pipeline
# A pipeline bundles multiple steps into one object.
# This is the standard, professional way to build models.
print("Defining ML pipeline...")
ml_pipeline = Pipeline([
    # Step 1: Vectorizer (Converts "pvr limited" into numbers [0, 0, 1.5, 0.2, ...])
    ('tfidf', TfidfVectorizer(stop_words='english')),
    
    # Step 2: Classifier (The 'brain' that learns)
    ('clf', LinearSVC(random_state=42))
])

# 3. Train the Model
print("Training the model... This might take a minute.")
ml_pipeline.fit(X_train, y_train)
print("Model training complete!")

# 4. Save the Model
# We save the *entire* trained pipeline to a file
# 'wb' means 'write binary'
with open(MODEL_FILE, 'wb') as f:
    pickle.dump(ml_pipeline, f)

print(f"\nSUCCESS! Model saved to {MODEL_FILE}.")