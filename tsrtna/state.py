import pandas as pd
from tpdp import State


class StockState(State):
    telegram_token: str = None
    telegram_userid: str = None

    stock: str = None
    datatime: str = None
    dataframe: pd.DateOffset = None

    class Config:
        arbitrary_types_allowed = True
