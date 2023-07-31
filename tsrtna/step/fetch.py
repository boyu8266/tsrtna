from typing import Any, Callable

from tpdp import Step
from twstock.realtime import get

from tsrtna.state import StockState


class FetchRealtimeData(Step):
    def run(self, state: StockState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> StockState:
        data: dict = get(state.stock)
        state.datatime = data['info']['time']
        state.price = data['realtime']['latest_trade_price']
        return state
