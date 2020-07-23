# import logging
# logging.basicConfig(level=logging.DEBUG)
import csv
from time import sleep

from alice_blue import *

import datetime


def abc():
    access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@9', twoFA='a',
                                                        api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
    alice = AliceBlue(username='AB102865', password='sampath@9', access_token=access_token,
                      master_contracts_to_download=['NFO'])
    socket_opened = True
    list = []

    def event_handler_quote_update(message):
        f = csv.writer(open('abcde.csv', 'w', newline=''))
        # print(message['ltp'],message['exchange_time_stamp'])
        # print(message)
        # f.writerow(message)
        list.append([message['instrument'][2], message['ltp'],
                     datetime.datetime.fromtimestamp((message['exchange_time_stamp'])), message['high'],
                     message['low'], message['close']])
        f.writerow([message['instrument'][2], message['ltp'],
                    datetime.datetime.fromtimestamp(int(message['exchange_time_stamp'])), message['high'],
                    message['low'], message['close']])

    def open_callback():
        global socket_opened
        socket_opened = True

    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)
    while (socket_opened == False):
        pass

    alice.subscribe([alice.get_instrument_for_fno(symbol='BANKNIFTY', expiry_date=datetime.date(2020, 7, 30),
                                                  is_fut=True, strike=None, is_CE=False),
                     alice.get_instrument_for_fno(symbol='NIFTY', expiry_date=datetime.date(2020, 7, 30), is_fut=True,
                                                  strike=None, is_CE=False)], LiveFeedType.MARKET_DATA)
    # alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None, is_CE = False),LiveFeedType.MARKET_DATA)
    # alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None, is_CE = False),LiveFeedType.MARKET_DATA)
    sleep(2)
    print(list)
    alice.place_order()


abc()
