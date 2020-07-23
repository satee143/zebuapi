import pandas as pd
from datetime import datetime

df_cols = ["LTP", 'Times']
df = pd.read_csv('/storage/emulated/0/termux/downloads/bank_nifty.csv', names=df_cols, index_col=1, parse_dates=True)
df.reset_index(inplace=True)

print(df)

df['Times'] = [datetime.fromtimestamp(x) for x in df['Times']]
# df['Times']=pd.to_datetime(df['Times'], unit='s')
print(df['Times'])
df.set_index('Times', inplace=True)
candles = df['LTP'].resample('5min').ohlc().dropna()
# df=df.drop_duplicates(inplace=False)
print(candles)
