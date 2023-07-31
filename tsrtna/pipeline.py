from tpdp import Pipeline

from tsrtna.state import StockState
from tsrtna.step import *


class StockPipeline:
    def __init__(self):
        fetchrealtimedata = FetchRealtimeData('fetch realtime data')
        telegramsendtextinfo = TelegramSendTextInfo('telegram send text info')
        steps = [fetchrealtimedata, telegramsendtextinfo]

        pipeline = Pipeline('stock pipeline')
        for step in steps:
            pipeline.registry_step(step)
        self.__pipeline = pipeline

    def run(self, stock: str,  telegram_token: str = None, telegram_userid: str = None) -> StockState:
        state = StockState(
            telegram_token=telegram_token,
            telegram_userid=telegram_userid,
            stock=stock
        )
        self.__pipeline.run(state)
        return state
