import csv
from time import sleep

import requests
from alice_blue import *

import datetime
from threading import Timer

x = datetime.datetime.today()
y = x.replace(day=x.day + 1, hour=0, minute=53, second=16, microsecond=0)
delta_t = y - x
secs = delta_t.seconds + 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept-Language': 'en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,te;q=0.6,en-US;q=0.5,en-GB;q=0.4',
    'Accept-Encoding': 'gzip, deflate, br'}


def get_nifty_status():
    resp = requests.get('https://www1.nseindia.com/homepage/Indices1.json', headers=headers).json()
    nifty_percentage = float(resp['data'][0]['change'])
    return nifty_percentage


def get_2_top_gainers():
    resp = requests.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json',
                        headers=headers).json()
    # print(resp['data'][0]['symbol'], resp['data'][0]['netPrice'])
    # print(resp['data'][1]['symbol'], resp['data'][1]['netPrice'])
    '''l1=[]
    for i in range(2):
        if int(resp['data'][i]['netPrice'])<2:
            l1.append(resp['data'][0]['symbol'])'''
    return (resp['data'][0]['symbol'], resp['data'][1]['symbol'])


def get_2_top_loosers():
    resp = requests.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json',
                        headers=headers).json()
    print(resp['data'][0]['symbol'], resp['data'][0]['netPrice'])
    print(resp['data'][1]['symbol'], resp['data'][1]['netPrice'])
    return (resp['data'][0]['symbol'], resp['data'][1]['symbol'])


def calling_results():
    nifty = get_nifty_status()
    if nifty > 0:
        return get_2_top_gainers()
    else:
        return get_2_top_loosers()


def abc():
    access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@9', twoFA='a',
                                                        api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
    alice = AliceBlue(username='AB102865', password='sampath@9', access_token=access_token,
                      master_contracts_to_download=['NSE'])
    socket_opened = True
    list = []

    def event_handler_quote_update(message):
        f = csv.writer(open('abcd.csv', 'w', newline=''))
        # print(message['ltp'],message['exchange_time_stamp'])
        print(message)
        # f.writerow(message)
        list.append([message['instrument'][2], message['ltp'],
                     datetime.datetime.fromtimestamp(int(message['exchange_time_stamp'])), message['open'],
                     message['high'],
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

    '''alice.subscribe([alice.get_instrument_for_fno(symbol='BANKNIFTY', expiry_date=datetime.date(2020, 7, 30),
                                                  is_fut=True, strike=None, is_CE=False),alice.get_instrument_by_symbol('NSE', 'NIFTY50'),
                     alice.get_instrument_for_fno(symbol='NIFTY', expiry_date=datetime.date(2020, 7, 30), is_fut=True,
                                                  strike=None, is_CE=False)], LiveFeedType.MARKET_DATA)'''
    alice.subscribe([alice.get_instrument_by_symbol('NSE', calling_results()[0]),
                     alice.get_instrument_by_symbol('NSE', calling_results()[1])], LiveFeedType.MARKET_DATA)
    # alice.subscribe(alice.get_instrument_for_fno(symbol='NIFTY', expiry_date=datetime.date(2020, 7, 30), is_fut=True,strike=None, is_CE=False),LiveFeedType.MARKET_DATA)
    # alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None, is_CE = False),LiveFeedType.MARKET_DATA)
    # alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 6, 25), is_fut=True, strike=None, is_CE = False),LiveFeedType.MARKET_DATA)
    sleep(1)
    for x in list:
        if ((x[1] > x[3]) and (x[5] > x[3]) and (x[5] == x[1])):
            print('1st cond', x[0], x[4])
        elif ((x[1] > x[3]) and (x[5] < x[3]) and (x[5] == x[1])):
            print('2 cond', x[0], x[4])
        elif ((x[1] > x[3]) and (x[5] < x[3]) and (x[4] > x[1])):
            print('3 cond', x[0], x[4])
        print(x)


t = Timer(secs, abc)
t.start()
