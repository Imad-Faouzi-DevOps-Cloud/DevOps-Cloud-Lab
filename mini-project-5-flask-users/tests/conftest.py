# conftest.py is used by pytest to define fixtures that are reused across multiple test files.

import pytest
from app import create_app  # Import the Flask app factory

@pytest.fixture
def client():
    """
    This fixture creates a test client from the Flask app.
    The test client simulates HTTP requests without running a server.
    """
    app = create_app()              # Create app using our factory
    app.config['TESTING'] = True    # Enable test mode
    with app.test_client() as client:
        yield client                # Provide the client to the test

