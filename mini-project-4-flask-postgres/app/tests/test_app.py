# Import the app from our main Flask file
from app.main import app

# Define a test function
def test_home():
    # Create a test client from the Flask app
    tester = app.test_client()

    # Send a GET request to the '/' route
    response = tester.get('/')

    # Check that the response is successful (HTTP 200)
    assert response.status_code == 200

    # Check that the word "Hello" is in the response
    assert b"Hello" in response.data
