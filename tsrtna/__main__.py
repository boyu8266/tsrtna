import argparse

from tsrtna import StockPipeline, __version__, sleep
from tsrtna.config import Config


def main():
    print(f'version: {__version__}')

    parser = argparse.ArgumentParser(description="TW Stock Realtime Notification Application CLI")
    config: Config = Config.from_config_file()
    pipeline = StockPipeline()

    token = config.telegram_token
    user = config.telegram_userid
    for stock in config.stocks:
        pipeline.run(stock, token, user)
        sleep()


if __name__ == "__main__":
    main()
