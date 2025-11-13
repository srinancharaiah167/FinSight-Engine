from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/categorize', methods=['POST'])
def categorize():
    """
    A dummy endpoint that returns a simple JSON message.
    We use methods=['POST'] as this endpoint will
    likely receive data to categorize in the future.
    """
    # For now, just return a confirmation message
    response = {
        "message": "OK"
    }
    return jsonify(response)

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True, port=5000)