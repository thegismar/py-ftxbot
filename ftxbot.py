import os
from ftx import FtxClient


class AutoFtxTrader:
    api_key = os.getenv('FTX_API')
    api_secret = os.getenv('FTX_SECRET')

    def __init__(self):
        self.client = FtxClient(api_key=self.api_key, api_secret=self.api_secret)
        self.placeOrderDict = {}

    def set_order(self, order_info):
        market = order_info['market']
        side = order_info['side']
        price = order_info['price']
        size = order_info['size']
        type = order_info['type']
        reduce_only = order_info['reduce_only']
        ioc = order_info['ioc']
        post_only = order_info['post_only']
        client_id = order_info['client_id']

        return self.client.place_order(market=market, side=side, price=price, size=size, type=type,
                                       reduce_only=reduce_only, ioc=ioc, post_only=post_only, client_id=client_id)

    def place_trigger(self, trigger_info):
        market = trigger_info['market']
        side = trigger_info['side']
        size = ['size']
        type = trigger_info['type']
        reduce_only = trigger_info['reduce_only']
        cancel = trigger_info['cancel']
        trigger_price = trigger_info['trigger_price']
        limit_price = trigger_info['limit_price']

        return self.client.place_conditional_order(market=market, side=side, size=size, type=type,
                                                   limit_price=limit_price, reduce_only=reduce_only, cancel=cancel,
                                                   trigger_price=trigger_price)

    def create_order(self, order_info, sl_info, tp_info):
        assert ['market', 'side', 'price', 'type', 'size', 'reduce_only', 'client_id', 'ioc', 'post_only'] in order_info
        assert ['market', 'side', 'size', 'type', 'reduce_only', 'cancel', 'trigger_price', 'limit_price'] in sl_info
        assert ['market', 'side', 'size', 'type', 'reduce_only', 'cancel', 'trigger_price', 'limit_price'] in tp_info
