import os

import pandas as pd

os.chdir('/storage/emulated/0/bluetooth')
df = pd.read_excel('c.xlsx')
df.reset_index()
df.set_index('Date', inplace=True)
df[['Close']].to_csv('c.csv')
