from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "AlfaBankHackathon"
    description: str = "AlfaBankHackathon"
    secret: str = "SECRET"
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"

    mail_username: str = 'AlfaBankHackathon@ya.ru'
    mail_password: str = 'yfidmxkvwehwyhju'  # noqa
    mail_from: str = 'AlfaBankHackathon@ya.ru'
    mail_port: int = 465
    mail_server: str = 'smtp.yandex.ru'
    mail_starttls: bool = False
    mail_ssl_tls: bool = True
    use_credentials: bool = True
    validate_certs: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
