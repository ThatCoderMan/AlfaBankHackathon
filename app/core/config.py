from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "AlfaBankHackathon"
    description: str = "AlfaBankHackathon"
    secret: str = "SECRET"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

    class Config:
        env_file = ".env"


settings = Settings()
