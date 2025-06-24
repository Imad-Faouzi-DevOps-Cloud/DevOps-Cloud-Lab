# This file contains actual test cases for the /users endpoints.
# These will run automatically in CI/CD to make sure the app behaves correctly.

def test_get_users_empty(client):
    """
    Should return an empty list when no users are added yet.
    """
    response = client.get('/users')             # Send GET request to /users
    assert response.status_code == 200          # Expect HTTP 200 OK
    assert response.get_json() == []            # Expect an empty list of users

def test_create_user_success(client):
    """
    Should successfully create a new user and return it.
    """
    response = client.post('/users', json={"name": "Alice"})
    assert response.status_code == 201          # Expect HTTP 201 Created
    data = response.get_json()
    assert data["name"] == "Alice"              # The returned name should match
    assert "id" in data                         # A new ID should be assigned

def test_create_user_missing_name(client):
    """
    Should return an error when 'name' is missing in POST body.
    """
    response = client.post('/users', json={})   # Send empty JSON body
    assert response.status_code == 400          # Expect HTTP 400 Bad Request
    assert "error" in response.get_json()       # Expect error message in response
