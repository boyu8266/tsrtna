import pytest

from tsrtna.config import Config


class TestConfig:
    def test_valid_arguments(self):
        config = Config(
            telegram_token='token',
            telegram_userid='userid',
            stocks=['AAPL', 'GOOG']
        )
        assert config.telegram_token == 'token'
        assert config.telegram_userid == 'userid'
        assert config.stocks == ['AAPL', 'GOOG']

    def test_valid_arguments_stocks_list(self):
        config = Config(
            telegram_token='token',
            telegram_userid='userid',
            stocks=['AAPL', 'GOOG']
        )
        assert isinstance(config.stocks, list)

    def test_from_config_file(self):
        config = Config.from_config_file('config.example.ini')
        assert config.telegram_token == '1111111111:xxxxxxxxxxxxxxxxxxxxxxxxx'
        assert config.telegram_userid == '111111111'
        assert config.stocks == ['2330', '2327']
