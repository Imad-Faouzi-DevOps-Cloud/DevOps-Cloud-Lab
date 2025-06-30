# app/config.py

from pydantic_settings import BaseSettings

# Load .env vars using pydantic BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"  # Load from .env file

settings = Settings()
