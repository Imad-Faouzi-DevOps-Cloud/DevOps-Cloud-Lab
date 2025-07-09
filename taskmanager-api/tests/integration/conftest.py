import pytest_asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from app.config import settings
from app.deps import get_db  # 👈 Required to override dependency


# ✅ Ensure we’re using test env
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_db():
    assert settings.ENVIRONMENT == "test", "Not using test environment!"

    # Create a new engine for the test DB
    test_engine = create_async_engine(settings.DATABASE_URL, future=True)

    # Bind test sessionmaker
    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    # Drop and recreate all tables
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # 🧠 Dependency override
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    yield  # Run tests

    # Optional cleanup
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# ✅ Test client using ASGITransport
@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
