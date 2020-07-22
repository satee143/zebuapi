import os

import nsepy
import plotly.graph_objects as go

import datetime
from datetime import timedelta

global df, buy_list
global updates
buy_list = []
updates = []

data = 'INFY'
buy = []
date_y = datetime.date.today() - timedelta(days=30)
df = nsepy.get_history(symbol='ITC', start=datetime.date(2020, 6, 1), end=datetime.date(2020, 6, 14))
df.reset_index('Date', inplace=True)
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
df.set_index('Date', inplace=True)
ohlc_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'}
print(df)
df = df.resample('W').agg(ohlc_dict).dropna(how='any')
cols = ['Open', 'High', 'Low', 'Close']
df = df[cols]

# df = df['Close'].resample('1M').ohlc()
df.reset_index('Date', inplace=True)
print(df)

df['HA_Close'] = round(((df['Open'] + df['High'] + df['Low'] + df['Close']) / 4), 2)
df['HA_Open'] = round((df['Open'].shift(1) + df['Close'].shift(1)) / 2, 2)

df.iloc[0, df.columns.get_loc("HA_Open")] = round((df.iloc[0]['Open'] + df.iloc[0]['Close']) / 2, 2)

# for i in range(0,len(df)):
#	if i==0:
#		df['HA_Open'][i]=((df['Open'][i]+df['Close'][i])/2)
#	else:
#		df['HA_Open'][i]=((df['Open'][i-1]+df['Close'][i-1])/2)

df['HA_High'] = df[['High', 'Low', 'HA_Open', 'HA_Close']].max(axis=1)
df['HA_Low'] = ((df[['High', 'Low', 'HA_Open', 'HA_Close']].min(axis=1)))

print(df[['HA_Open', 'HA_High', 'HA_Low', 'HA_Close']])
# df.reset_index('Date', inplace=True)
# fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'],high=df['High'], low=df['Low'], close=df['Close'],increasing_line_color= 'blue', decreasing_line_color= 'red')])

fig = go.Figure(
    data=[go.Ohlc(x=df['Date'], open=df['HA_Open'], high=df['HA_High'], low=df['HA_Low'], close=df['HA_Close'])])
fig.show()

if (float(df.iloc[[-2]]['HA_Close']) <= float(df.iloc[[-2]]['HA_Open'])):
    if (float(df.iloc[[-1]]['HA_Close']) >= float(df.iloc[[-1]]['HA_Open'])):
        if (float(df.iloc[[-1]]['HA_High']) > float(df.iloc[[-2]]['HA_High']) and float(
                df.iloc[[-1]]['HA_Low']) < float(df.iloc[[-2]]['HA_Low'])):
            print('Buy Recommanded Price for ' + data + ' :', round(float(df.iloc[[-1]]['HA_High']), 2))
elif (float(df.iloc[[-2]]['HA_Close']) >= float(df.iloc[[-2]]['HA_Open'])):
    if ((float(df.iloc[[-1]]['HA_Close']) <= float(df.iloc[[-1]]['HA_Open']))):
        print('Sell Recommanded Price for ' + data + ':', round(float(df.iloc[[-1]]['HA_Low']), 2))
    os.chdir('/storage/emulated/0/recom')
    df[['Date', 'HA_Open', 'HA_High', 'HA_Low', 'HA_Close']].to_excel('w.xlsx')
# df.to_excel('weekly.xlsx')
# fig.write_html(data+'.html')
fig.show()
