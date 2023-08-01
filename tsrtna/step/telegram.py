from typing import Any, Callable

import telebot
from tabulate import tabulate
from tpdp import Step

from tsrtna.state import StockState


class TelegramSendTextInfo(Step):
    def run(self, state: StockState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> StockState:
        if not isinstance(state.telegram_token, str) or not isinstance(state.telegram_userid, str):
            return state

        token = state.telegram_token
        userid = state.telegram_userid

        bot = telebot.TeleBot(token)
        table = tabulate(
            state.dataframe,
            headers='keys',
            tablefmt='outline',
            showindex=False
        )
        bot.send_message(userid, f'<pre>{table}</pre>', parse_mode='HTML')
        return state
