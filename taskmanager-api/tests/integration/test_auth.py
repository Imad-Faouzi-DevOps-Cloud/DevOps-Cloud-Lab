import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_register_login():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Test user registration
        register_response = await ac.post("/auth/register", json={
            "email": "testuser@example.com",
            "password": "password123",
            "username": "testuser"
        })
        if register_response.status_code != 201:
            print("Registration failed:", register_response.status_code)
            print(register_response.json())
        assert register_response.status_code == 201

        # Test login
        login_response = await ac.post("/auth/login", data={
            "username": "testuser@example.com",
            "password": "password123"
        })
        assert login_response.status_code == 200
        json_resp = login_response.json()
        assert "access_token" in json_resp
        assert json_resp["token_type"] == "bearer"
