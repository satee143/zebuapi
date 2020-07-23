# pylint:disable=E1101
import nsepy

import datetime

# df = nsepy.get_history(symbol='SBIN', start=date(2020,4,1), end=date(2020,5,30))
df = nsepy.get_history(symbol='SBIN', start=datetime.date(2020, 4, 1), end=datetime.date.today())
print(type(df))
df.reset_index('Date', inplace=True)
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
df.set_index('Date', inplace=True)

ohlc_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'}

df = df.resample('W', how=ohlc_dict).dropna(how='any')

# cols=['Open', 'High', 'Low', 'Close']
# df = df[cols]
# df = df['Close'].resample('W').ohlc()
print(df.info())
