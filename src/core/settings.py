from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class BotSetting:
    token: str


@dataclass
class DatabaseSettings:
    _url: str
    name: str
    host: Optional[str] = None
    port: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None

    @property
    def url(self) -> str:
        if 'sqlite' in self._url:
            return self._url.format(self.name)

        return self._url.format(
            f'{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
        )


@dataclass
class Settings:
    bot: BotSetting
    db: DatabaseSettings


def load_settings() -> Settings:
    env = Env()
    env.read_env(path='./.env')

    return Settings(
        bot=BotSetting(
            token=env('BOT_TOKEN')
        ),
        db=DatabaseSettings(
            _url=env('DATABASE_URL'),
            name=env('DATABASE_NAME'),
            host=env('DATABASE_HOST'),
            port=env('DATABASE_PORT'),
            user=env('DATABASE_USER'),
            password=env('DATABASE_PASSWORD')
        )
    )
