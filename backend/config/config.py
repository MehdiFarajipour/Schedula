from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    DB_ENGINE: str = 'postgresql'

    # postgres database
    DB_NAME: str | None = None
    DB_USER: str | None = None
    DB_USER_PASS: str | None = None
    DB_PORT: int = "5432"
    DB_HOST: str = 'localhost'

    # smtp gmail app

    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str

    # django secret key
    SECRET_KEY: str


    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")

config_settings = Settings()
