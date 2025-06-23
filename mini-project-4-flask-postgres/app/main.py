# Import Flask and helper function to return JSON
from flask import Flask, jsonify

# Create a Flask web app instance
app = Flask(__name__)

# Define a route for the homepage ('/')
@app.route('/')
def home():
    # When this route is called, return a JSON message
    return jsonify({"message": "Hello from Flask API!"})

# Run the app only if this file is the main script
# It listens on all IPs (0.0.0.0) on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

