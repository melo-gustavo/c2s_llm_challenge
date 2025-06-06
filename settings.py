from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
        env_file_encoding="utf-8")

    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_NAME_DEFAULT: str
    POSTGRE_URL_DB: str
    GROQ_API_KEY: str


settings = Settings()
