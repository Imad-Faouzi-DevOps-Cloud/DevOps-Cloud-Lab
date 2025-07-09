import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from app.config import settings
from app.deps import get_db  # Dependency we override

# Ensure we're in test environment and prepare test DB
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_db():
    # Confirm test environment
    assert settings.ENVIRONMENT == "test", "Not using test environment!"

    # Create async engine for test DB (from DATABASE_URL)
    test_engine = create_async_engine(settings.DATABASE_URL, future=True)

    # Create async sessionmaker bound to test engine
    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    # Drop and recreate all tables fresh for test session
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # Override get_db dependency to use TestingSessionLocal for tests
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    yield  # Run tests

    # Optional cleanup after all tests finish
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# Provide async test HTTP client using FastAPI's ASGI app
@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
