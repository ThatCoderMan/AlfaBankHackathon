import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = os.getenv('APP_TITLE')
    description: str = os.getenv('DESCRIPTION')
    secret: str = os.getenv('SECRET')
    database_url: str = os.getenv('DATABASE_URL')

    class Config:
        env_file = ".env"


settings = Settings()
