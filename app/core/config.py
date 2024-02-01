from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "AlfaBankHackathon"
    description: str = "AlfaBankHackathon"
    secret: str = "SECRET"
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
    )

    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    mail_starttls: bool = False
    mail_ssl_tls: bool = True
    use_credentials: bool = True
    validate_certs: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
