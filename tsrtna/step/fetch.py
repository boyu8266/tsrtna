from typing import Any, Callable

import pandas as pd
from tpdp import Step
from twstock.realtime import get

from tsrtna.state import StockState


class FetchRealtimeData(Step):
    def run(self, state: StockState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> StockState:
        data: dict = get(state.stock)

        state.datatime = data['info']['time']

        df = pd.DataFrame(data['realtime'])[['best_bid_price', 'best_ask_price']]
        df.columns = ['bid', 'ask']
        state.dataframe = df
        return state
