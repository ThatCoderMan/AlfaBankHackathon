from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "AlfaBankHackathon"
    description: str = "AlfaBankHackathon"
    secret: str = "SECRET"
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
    )

    mail_username: str = "mail_username"
    mail_password: str = "mail_password"
    mail_from: str = "example@mail.com"
    mail_port: int = 465
    mail_server: str = "mail_server"
    mail_starttls: bool = False
    mail_ssl_tls: bool = True
    use_credentials: bool = True
    validate_certs: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
