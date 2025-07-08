# tests/integration/conftest.py

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from app.config import settings
from app.database import Base
from app.main import app

# ✅ Ensure we’re using the test environment
@pytest.fixture(scope="session", autouse=True)
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
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
