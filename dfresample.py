# pylint:disable=E0611
import os

import nsepy

import datetime
import pandas as pd

# from datetime import timedelta

global df, buy_list
global updates
buy_list = []
updates = []

os.chdir('/storage/emulated/0/Download')
df = nsepy.get_history(symbol='SBIN', start=datetime.date(2020, 4, 1), end=datetime.date.today())
print(type(df))
df2 = pd.DataFrame(df)

# df2.to_excel('a.xlsx')
# print(df[['Open','High','Low','Close']])
df.reset_index('Date', inplace=True)
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
df.set_index('Date', inplace=True)

ohlc_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'}

df = df.resample('W', how=ohlc_dict).dropna(how='any')

cols = ['Open', 'High', 'Low', 'Close']
df = df[cols]
# df = df['Close'].resample('W').ohlc()
print(df)
