import pytest
from httpx import AsyncClient, ASGITransport 
from app.main import app

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_ticket_flow():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Register user (needed before login)
        await ac.post("/auth/register", json={
            "email": "testuser@example.com",
            "password": "password123",
            "username": "testuser"
        })

        # Login first (assuming user exists)
        login_response = await ac.post("/auth/login", data={
            "username": "testuser@example.com",
            "password": "password123"
        })
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Create a ticket
        ticket_response = await ac.post("/tickets/", json={
            "title": "Test Ticket",
            "description": "Testing ticket creation"
        }, headers=headers)
        assert ticket_response.status_code == 201

        # Get tickets
        get_response = await ac.get("/tickets/", headers=headers)
        assert get_response.status_code == 200
        tickets = get_response.json()
        assert any(t["title"] == "Test Ticket" for t in tickets)
