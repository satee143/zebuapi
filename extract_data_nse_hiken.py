import os

import nsepy
import plotly.graph_objects as go

import datetime

global df


def create_chart():
    # dfx=pd.read_excel('c.xlsx',index_col=0,parse_dates=True)
    # print(dfx)
    # print(dfx.index)
    df = nsepy.get_history(symbol='CIPLA', start=datetime.date(2006, 6, 1), end=datetime.date.today())
    # print(df.index)
    df.reset_index('Date', inplace=True)
    # print(df.index)
    # print(df)
    df['Date'] = df['Date'].astype(str)
    import datetime as dt
    df['Date'] = df['Date'].apply(lambda x:
                                  dt.datetime.strptime(x, '%Y-%m-%d'))
    df.set_index('Date', inplace=True)
    # print(df.index)
    df = df['Close'].resample('1M').ohlc()
    df.reset_index('Date', inplace=True)
    print('After resampling')
    print(df)
    df.to_excel('monthly.xlsx')
    fig = go.Figure(data=[go.Ohlc(x=df['Date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
    df['HA_Close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    df['HA_Open'] = (df['open'].shift(1) + df['open'].shift(1)) / 2
    df.iloc[0, df.columns.get_loc("HA_Open")] = (df.iloc[0]['open'] + df.iloc[0]['close']) / 2
    df['HA_High'] = df[['high', 'low', 'HA_Open', 'HA_Close']].max(axis=1)
    df['HA_Low'] = df[['high', 'low', 'HA_Open', 'HA_Close']].min(axis=1)

    print(df[['Date', 'HA_Open', 'HA_High', 'HA_Low', 'HA_Close']])
    fig = go.Figure(data=[
        go.Candlestick(x=df['Date'], open=df['HA_Open'], high=df['HA_High'], low=df['HA_Low'], close=df['HA_Close'])])

    if (float(df.iloc[[-2]]['HA_High']) <= float(df.iloc[[-2]]['HA_Open'])):
        if (float(df.iloc[[-2]]['HA_Low']) <= float(df.iloc[[-2]]['HA_Close'])):
            print('Sell Recommanded Price:', float(df.iloc[[-2]]['HA_Low']) * 98 / 100)
    if (float(df.iloc[[-2]]['HA_Low']) >= float(df.iloc[[-2]]['HA_Open'])):
        if ((float(df.iloc[[-2]]['HA_High']) >= float(df.iloc[[-2]]['HA_Close']))):
            print('Buy Recommanded Price:', float(df.iloc[[-2]]['HA_High']) * 102 / 100)
    fig.show()
    return df


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
