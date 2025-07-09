from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings
import os

# Determine which DB URL to use
DATABASE_URL = (
    settings.TEST_DATABASE_URL
    if settings.ENVIRONMENT == "test"
    else settings.DATABASE_URL
)

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create async session
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for models
Base = declarative_base()
