# Import the Flask module
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route at '/' that returns a simple message
@app.route('/')
def hello():
    return 'Hello from Dockerized Flask API!'
