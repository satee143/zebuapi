import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG)
import csv
import datetime
from alice_blue import *

access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@4', twoFA='a',
                                                    api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
alice = AliceBlue(username='AB102865', password='sampath@4', access_token=access_token,
                  master_contracts_to_download=['NFO'])
socket_opened = True


def event_handler_quote_update(message):
    with open('bank-j.csv', 'a', newline='') as ff:
        f = csv.writer(ff)
        # f=csv.writer(open('bank_nifty.csv', 'a', newline=''))
        print(message['ltp'], message['exchange_time_stamp'])
        f.writerow([message['ltp'], message['exchange_time_stamp']])


def open_callback():
    global socket_opened
    socket_opened = True


alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while (socket_opened == False):
    pass
alice.subscribe(
    alice.get_instrument_for_fno(symbol='BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None,
                                 is_CE=False),
    LiveFeedType.MARKET_DATA)
# alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None, is_CE = False),LiveFeedType.MARKET_DATA)
sleep(9000000000)
