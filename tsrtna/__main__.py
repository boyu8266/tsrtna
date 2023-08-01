import argparse

from tabulate import tabulate

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
        state = pipeline.run(stock, token, user)
        print(f'{state.stock}, {state.datatime}')
        table = tabulate(
            state.dataframe,
            headers='keys',
            tablefmt='rounded_outline',
            showindex=False
        )
        print(table)
        sleep()


if __name__ == "__main__":
    main()
