# tests/integration/test_tickets.py

import pytest

@pytest.mark.asyncio
async def test_ticket_flow(client):  # uses the fixture
    # Register a test user
    await client.post("/auth/register", json={
        "email": "ticketuser@example.com",
        "password": "password123",
        "username": "ticketuser"
    })

    # Log in and get JWT token
    login_response = await client.post("/auth/login", data={
        "username": "ticketuser@example.com",
        "password": "password123"
    })
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a new ticket
    ticket_response = await client.post("/tickets/", json={
        "title": "Test Ticket",
        "description": "Testing ticket creation"
    }, headers=headers)
    assert ticket_response.status_code == 201

    # Get all tickets and check for the one we just created
    get_response = await client.get("/tickets/", headers=headers)
    assert get_response.status_code == 200
    tickets = get_response.json()
    assert any(t["title"] == "Test Ticket" for t in tickets)
