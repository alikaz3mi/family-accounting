from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    username: str
    password: str
    host: str
    port: int
    name: str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="db_",
        extra="ignore",
    )
