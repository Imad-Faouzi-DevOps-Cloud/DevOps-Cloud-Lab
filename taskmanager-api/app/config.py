# app/config.py

import os
from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict


class Settings(BaseSettings):
    # Dynamically set the env file based on the ENVIRONMENT variable
    model_config = ConfigDict(
        env_file=".env.test" if os.getenv("ENVIRONMENT") == "test" else ".env",
        extra="forbid"
    )

    # Required variables
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")

    # Optional / defaults
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ENVIRONMENT: str = Field(..., env="ENVIRONMENT")
    APP_HOST: str = Field(..., env="APP_HOST")
    APP_PORT: int = Field(..., env="APP_PORT")

    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT")

    LOG_LEVEL: str = Field(..., env="LOG_LEVEL")
    RELOAD: bool = Field(..., env="RELOAD")


settings = Settings()
