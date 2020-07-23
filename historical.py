import os

from nsepy import get_history

from datetime import date

data = get_history(symbol='SBIN', start=date(2020, 1, 1), end=date(2020, 4, 17))
os.chdir('/storage/emulated/0/bluetooth')
print(type(data))
data.to_excel('a.xlsx')
