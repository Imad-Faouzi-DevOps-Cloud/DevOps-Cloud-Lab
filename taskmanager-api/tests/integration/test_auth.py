import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import uuid

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_register_login():
    email = f"testuser_{uuid.uuid4().hex}@example.com"

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        register_response = await ac.post("/auth/register", json={
            "email": email,
            "password": "password123",
            "username": "testuser"
        })
        print(register_response.json())
        assert register_response.status_code == 201

        login_response = await ac.post("/auth/login", data={
            "username": email,
            "password": "password123"
        })
        assert login_response.status_code == 200
        json_resp = login_response.json()
        assert "access_token" in json_resp
        assert json_resp["token_type"] == "bearer"
