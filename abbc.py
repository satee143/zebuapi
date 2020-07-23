import psycopg2
from alice_blue import *

import datetime

access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@1', twoFA='a',
                                                    api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
alice = AliceBlue(username='AB102865', password='sampath@1', access_token=access_token,
                  master_contracts_to_download=['NSE', 'NFO', 'BSE'])

socket_opened = False


def event_handler_quote_update(message):
    con = psycopg2.connect(database='stockmarket', user='postgres', password='0690252')
    cur = con.cursor()
    # print(message['ltp'],datetime.datetime.fromtimestamp(int(message['exchange_time_stamp'])))
    print(message['ltp'], message['open'], message['high'], message['low'], message['close'],
          datetime.datetime.fromtimestamp(int(message['exchange_time_stamp'])))
    sql = "insert into banknifty values('%s',%f,%f,%f,%f,%f,'%s')"
    cur.execute(sql % (
    message['instrument'][2], message['ltp'], message['open'], message['high'], message['low'], message['close'],
    datetime.datetime.fromtimestamp(message['exchange_time_stamp'])))

    con.commit()


def open_callback():
    global socket_opened
    socket_opened = True


alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while (socket_opened == False):
    pass
alice.subscribe(
    alice.get_instrument_for_fno(symbol='BANKNIFTY', expiry_date=datetime.date(2020, 5, 28), is_fut=True, strike=None,
                                 is_CE=False), LiveFeedType.MARKET_DATA)
