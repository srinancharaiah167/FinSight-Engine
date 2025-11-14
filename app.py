import json
from flask import Flask, request, jsonify

# 1. Initialize the Flask App
app = Flask(__name__)

# 2. Load the Rules from categories.json (once, at startup)
# This is a critical optimization. We load the file once
# so we don't have to read it for every single API request.
try:
    with open('categories.json', 'r') as f:
        categories = json.load(f)
    print("Loaded categories.json successfully.")
except FileNotFoundError:
    print("ERROR: 'categories.json' not found. API will return 'Other'.")
    categories = {}
except json.JSONDecodeError:
    print("ERROR: 'categories.json' is not valid JSON. Check for errors.")
    categories = {}

# 3. Helper Function: This is the Stage 1 "Rules Engine"
def find_category_by_rule(description):
    """
    Scans the description string for any keywords from our rules.
    """
    if not description:
        return "Other"
        
    # Make the search case-insensitive
    description_lower = description.lower()
    
    # Loop through our categories and their keywords
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description_lower:
                # Found a match! Return the category name.
                return category
                
    # If no match is found after all loops
    return "Other"

# 4. Create the API Endpoint
@app.route('/categorize', methods=['POST'])
def categorize_transaction():
    """
    This is the main API endpoint.
    It expects a JSON payload like: {"description": "STRBKS #1234"}
    """
    
    # Get the JSON data that the user sent in the request
    data = request.get_json()

    # --- Input Validation ---
    # Check if JSON is empty or the 'description' key is missing
    if not data or 'description' not in data:
        # Return a 400 Bad Request error
        return jsonify({"error": "Missing 'description' in request body"}), 400

    description = data['description']
    
    # --- Run our Logic ---
    category = find_category_by_rule(description)
    
    # --- Format the Response ---
    # Send back a clean JSON response
    result = {
        "description": description,
        "category": category,
        "source": "Stage 1 (Rules Engine)"
    }
    
    return jsonify(result)

# 5. A 'health check' route to see if the server is running
@app.route('/', methods=['GET'])
def home():
    return "FinSight Engine API (Stage 1) is running!"

# This block allows you to run the file directly with `python app.py`
if __name__ == '__main__':
    # debug=True means the server will auto-reload when you save changes
    app.run(debug=True)