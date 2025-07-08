# tests/integration/test_auth.py

import pytest

@pytest.mark.asyncio
async def test_register_login(client):  # uses the fixture
    # Register a new test user
    register_response = await client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "password123",
        "username": "testuser"
    })
    assert register_response.status_code == 201

    # Log in with that user
    login_response = await client.post("/auth/login", data={
        "username": "testuser@example.com",
        "password": "password123"
    })
    assert login_response.status_code == 200
    json_resp = login_response.json()
    assert "access_token" in json_resp
    assert json_resp["token_type"] == "bearer"
