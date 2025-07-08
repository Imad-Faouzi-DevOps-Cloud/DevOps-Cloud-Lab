import pytest

@pytest.mark.asyncio
async def test_ticket_flow(client):
    async with client as ac:
        await ac.post("/auth/register", json={
            "email": "ticketuser@example.com",
            "password": "password123",
            "username": "ticketuser"
        })

        login_response = await ac.post("/auth/login", data={
            "username": "ticketuser@example.com",
            "password": "password123"
        })
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        ticket_response = await ac.post("/tickets/", json={
            "title": "Test Ticket",
            "description": "Testing ticket creation"
        }, headers=headers)
        assert ticket_response.status_code == 201

        get_response = await ac.get("/tickets/", headers=headers)
        assert get_response.status_code == 200
        tickets = get_response.json()
        assert any(t["title"] == "Test Ticket" for t in tickets)
