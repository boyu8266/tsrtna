from datetime import datetime
from typing import Any, Callable

import telebot
from tpdp import Step

from tsrtna.state import StockState


class TelegramSendTextInfo(Step):
    def run(self, state: StockState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> StockState:
        if not isinstance(state.telegram_token, str) or not isinstance(state.telegram_userid, str):
            return state

        token = state.telegram_token
        userid = state.telegram_userid

        bot = telebot.TeleBot(token)
        message_text = f"""
[{state.stock}]
Data Date: {state.datatime}
Price: {state.price}
"""
        bot.send_message(userid, message_text)
        return state
