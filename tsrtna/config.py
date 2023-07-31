from configparser import ConfigParser
from typing import List

from pydantic import BaseModel


class Config(BaseModel):
    telegram_token: str
    telegram_userid: str
    stocks: List[str]

    @classmethod
    def from_config_file(cls, file: str = 'config.ini'):
        config = ConfigParser()
        config.read(file)

        stocks = [stock.strip() for stock in config.get('TW', 'stocks').split(',')]

        return cls(
            telegram_token=config.get('Telegram', 'token'),
            telegram_userid=config.get('Telegram', 'userid'),
            stocks=stocks
        )
