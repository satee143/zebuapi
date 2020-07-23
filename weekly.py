import os

import plotly.graph_objects as go

import pandas as pd


def create_chart():
    df = pd.read_csv('c.csv', names=['date', 'Close'], index_col=0, parse_dates=True)
    df = df['Close'].resample('1M').ohlc()
    df.reset_index('date', inplace=True)
    print(df)
    fig = go.Figure(
        data=[go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
    fig.show()


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
