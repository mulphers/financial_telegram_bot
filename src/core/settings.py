from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
        env_prefix='bot_'
    )

    token: str


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
        env_prefix='database_'
    )

    uri: str
    name: str
    host: Optional[str] = None
    port: Optional[int] = None
    user: Optional[str] = None
    password: Optional[str] = None

    @property
    def url(self) -> str:
        if 'sqlite' in self.uri:
            return self.uri.format(self.name)

        return self.uri.format(f'{self.user}:{self.password}@{self.host}:{self.port}/{self.name}')


class Settings(BaseSettings):
    bot: BotSettings
    db: DatabaseSettings

    @staticmethod
    def root_dir() -> Path:
        return Path(__file__).resolve().parent.parent.parent


def load_settings(
        bot_settings: Optional[BotSettings] = None,
        database_settings: Optional[DatabaseSettings] = None
) -> Settings:
    return Settings(
        bot=bot_settings or BotSettings(),  # type: ignore[call-arg]
        db=database_settings or DatabaseSettings()  # type: ignore[call-arg]
    )
