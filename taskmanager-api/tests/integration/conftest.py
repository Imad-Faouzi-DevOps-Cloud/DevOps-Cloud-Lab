# tests/integration/conftest.py

import pytest_asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine
from app.config import settings
from app.database import Base  # <-- ⛏️ Ajouté pour faire fonctionner drop_all/create_all
from app.main import app

# ✅ Ensure we’re using the test environment
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_db():
    assert settings.ENVIRONMENT == "test", "Not using test environment!"

    # Create a fresh test database engine
    test_engine = create_async_engine(settings.DATABASE_URL, future=True)

    # Drop and recreate all tables before tests run
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield  # Run all tests

    # Optional cleanup after test session
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# ✅ Provide a test HTTP client using FastAPI's ASGI app
@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app, lifespan="on")
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
