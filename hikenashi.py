import os

import plotly.graph_objects as go

import pandas as pd

global df


def create_chart():
    df = pd.read_csv('c.csv', names=['date', 'Close'], index_col=0, parse_dates=True)

    df = df['Close'].resample('1M').ohlc()
    df.reset_index('date', inplace=True)
    # print(df)
    fig = go.Figure(data=[go.Ohlc(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
    # fig.show()
    return df


def heikenashi():
    df = create_chart()
    df['HA_Close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    df['HA_Open'] = (df['open'].shift(1) + df['open'].shift(1)) / 2
    df.iloc[0, df.columns.get_loc("HA_Open")] = (df.iloc[0]['open'] + df.iloc[0]['close']) / 2
    df['HA_High'] = df[['high', 'low', 'HA_Open', 'HA_Close']].max(axis=1)
    df['HA_Low'] = df[['high', 'low', 'HA_Open', 'HA_Close']].min(axis=1)
    df = df.drop(['open', 'high', 'low', 'close'], axis=1)  # remove old columns
    # df = df.rename(columns={"HA_Open": "open", "HA_High": "high", "HA_Low": "low", "HA_Close": "close", "Volume": "Volume"})
    # df = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # reorder columns
    print(df)
    fig = go.Figure(data=[
        go.Candlestick(x=df['date'], open=df['HA_Open'], high=df['HA_High'], low=df['HA_Low'], close=df['HA_Close'])])
    if (float(df.iloc[[-1]]['HA_High']) <= float(df.iloc[[-1]]['HA_Open']) or float(df.iloc[[-1]]['HA_Low']) >= float(
            df.iloc[[-1]]['HA_Open'])):
        if (float(df.iloc[[-1]]['HA_Low']) <= float(df.iloc[[-1]]['HA_Close'])):
            print(float(df.iloc[[-1]]['HA_Low']) * 98 / 100)
        elif ((float(df.iloc[[-1]]['HA_High']) >= float(df.iloc[[-1]]['HA_Close']))):
            print(float(df.iloc[[-1]]['HA_High']) * 102 / 100)


# fig.show()


'''
def buy_sell():
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data2)):
        if data2['SMA30'][i] > data2['SMA100'][i]:

            if flag != 1:
                sigPriceBuy.append(data2['SMA30'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)


        elif data2['SMA30'][i] < data2['SMA100'][i]:
            if flag != 0:
                sigPriceSell.append(data2['SMA30'][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)

        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)
'''
os.chdir('/storage/emulated/0/bluetooth')

create_chart()
heikenashi()
