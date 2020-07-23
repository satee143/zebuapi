import datetime;

import pandas as pd

# columns in data frame
df_cols = ["Timestamp", "Token", "LTP"]

data_frame = pd.DataFrame(data=[], columns=df_cols, index=[])


def on_ticks():
    global data_frame, df_cols

    data = dict()
    token = 'sbin'
    ltp = 1402
    timestamp = datetime.datetime.today().strftime('%d%m%Y %H:%M')

    data[timestamp] = [timestamp, token, ltp]
    print(data)
    tick_df = pd.DataFrame(data.values(), columns=df_cols, index=data.keys())
    # print(tick_df)
    data_frame = data_frame.append(tick_df)
    ggframe = data_frame.set_index(['Timestamp'], ['Token'])
    gticks = ggframe.loc[:, ['LTP']]
    print(gticks)
    candles = gticks['LTP'].resample('1D').ohlc().dropna()
    print(candles)


on_ticks()
'''
    
    
    print candles

def on_connect(kws , response):
    print('Connected')
    kws.subscribe(trd_tkn1)
    kws.set_mode(kws.MODE_FULL, trd_tkn1)

def on_close(ws, code, reason):
    print('Connection Error')


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()
'''
