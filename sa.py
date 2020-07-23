# from datetime import datetime
# from matplotlib import  pyplot as plt

from nsepy import get_history

from datetime import date

data = get_history(symbol='ONGC', start=date(2010, 1, 1), end=date(2020, 4, 17))
# plt.style.use('fivethirtyeight')


# os.chdir('/storage/emulated/0/bluetooth')
# data = pd.read_excel("c.xlsx")
# print('Raw data from Yahoo Finance : ')
# print(data.head())

data.set_index('Open')
print(data)
