from tpdp import State


class StockState(State):
    telegram_token: str = None
    telegram_userid: str = None
    
    stock: str = None
    datatime: str = None
    price: str = None

    class Config:
        arbitrary_types_allowed = True
