from alice_blue import *

access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@4', twoFA='a',
                                                    api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
'''alice = AliceBlue(username='AB102865', password='sampath@4', access_token=access_token)
#print(alice.get_profile())
all_banknifty_scrips = alice.search_instruments('NFO', 'BANKNIFTY')
print(all_banknifty_scrips)'''

alice = AliceBlue(username='AB102865', password='sampath@4', access_token=access_token,
                  master_contracts_to_download=['NSE', 'NFO', 'BSE'])
'''tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)
bn_fut = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 5,28), is_fut=True, strike=None, is_CE = False)
bn_call = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 5,28), is_fut=False, strike=19000, is_CE = True)
bn_put = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2020, 5,28), is_fut=False, strike=19000, is_CE = False)
print(bn_fut)

print(bn_call)

print(bn_put)'''

ax = alice.subscribe(alice.get_instrument_by_symbol('NSE', 'TATASTEEL'), LiveFeedType.COMPACT)
socket_opened = False


def event_handler_quote_update(message):
    print(f"quote update {message}")


def open_callback():
    global socket_opened
    socket_opened = True


alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while (socket_opened == False):
    pass
alice.subscribe(alice.get_instrument_by_symbol('NFO', 'ONGC'), LiveFeedType.MARKET_DATA)
