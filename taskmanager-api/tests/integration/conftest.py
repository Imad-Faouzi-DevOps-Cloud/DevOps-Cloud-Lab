# tests/integration/conftest.py

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from app.config import settings
from app.database import Base
from app.main import app


# 🚨 This runs ONCE per test session to reset the DB
@pytest.fixture(scope="session", autouse=True)
async def setup_test_db():
    assert settings.ENVIRONMENT == "test", "Not using test environment!"

    # Create async SQLAlchemy engine from DATABASE_URL in .env.test
    test_engine = create_async_engine(settings.DATABASE_URL, future=True)

    # Drop all tables, then create all fresh
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield  # Run tests...

    # (Optional) Clean up after tests
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# 🧪 Reusable test client for all tests
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
