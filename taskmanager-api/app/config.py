from dotenv import load_dotenv
import os

# Load correct .env file early and manually
if os.environ.get("ENVIRONMENT") == "test":
    load_dotenv(".env.test")
else:
    load_dotenv(".env")


from pydantic_settings import BaseSettings
from pydantic import Field

# Detect the correct .env file
env_file_path = ".env.test" if os.environ.get("ENVIRONMENT") == "test" else ".env"

class Settings(BaseSettings):
    # All environment variables
    ENVIRONMENT: str = Field("local", env="ENVIRONMENT")

    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    TEST_DATABASE_URL: str | None = Field(None, env="TEST_DATABASE_URL")
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")

    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    APP_HOST: str = Field("0.0.0.0", env="APP_HOST")
    APP_PORT: int = Field(8000, env="APP_PORT")

    POSTGRES_USER: str = Field("postgres", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("postgres", env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("taskmanager", env="POSTGRES_DB")
    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")

    LOG_LEVEL: str = Field("info", env="LOG_LEVEL")
    RELOAD: bool = Field(False, env="RELOAD")

    class Config:
        env_file = env_file_path
        extra = "forbid"

settings = Settings()
