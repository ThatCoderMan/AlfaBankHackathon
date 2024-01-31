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
    mail_starttls: bool
    mail_ssl_tls: bool
    use_credentials: bool
    validate_certs: bool

    class Config:
        env_file = ".env"


settings = Settings()
