import os

import numpy as np
from matplotlib import pyplot as plt

import pandas as pd

plt.style.use('fivethirtyeight')

os.chdir('/storage/emulated/0/bluetooth')
data = pd.read_excel("c.xlsx")
# print('Raw data from Yahoo Finance : ')
# print(data.head())


'''plt.plot(data['Close'], label='sbin')
plt.title('SBI Equity price trend')
plt.xlabel('Jan-1-2020 to Apr-30-2020')
plt.ylabel('Closing Price ')
plt.legend(loc='upper left')
plt.show()'''

SMA30 = pd.DataFrame()
SMA30['Close'] = data['Close'].rolling(window=30).mean()

SMA100 = pd.DataFrame()
SMA100['Close'] = data['Close'].rolling(window=100).mean()

'''plt.plot(data['Close'], label='sbin')
plt.plot(SMA30['Close'], label='SMA30')
plt.plot(SMA100['Close'], label='SMA100')
plt.title('SBI Equity price trend')
plt.xlabel('Jan-1-2020 to Apr-30-2020')
plt.ylabel('Closing Price ')
plt.legend(loc='upper left')
plt.show()'''

data2 = pd.DataFrame()
data2['SBIN'] = data['Close']
data2['SMA30'] = SMA30['Close']
data2['SMA100'] = SMA100['Close']


# print(data2)


def buy_sell(data2):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data2)):
        if data2['SMA30'][i] > data2['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data2['SBIN'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)


        elif data2['SMA30'][i] < data2['SMA100'][i]:
            if flag != 0:
                sigPriceSell.append(data2['SBIN'][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)


buy_sell = buy_sell(data2)
data2['Buy_Signal_Price'] = buy_sell[0]
data2['Sell_Signal_Price'] = buy_sell[1]

# print(data2)

plt.plot(data2['SBIN'], label='SBIN', alpha=0.35)
plt.plot(data2['SMA30'], label='SMA30')
plt.plot(data2['SMA100'], label='SMA100')
plt.scatter(data2.index, data2['Buy_Signal_Price'], label='Buy', marker='^', color='green')

plt.scatter(data2.index, data2['Sell_Signal_Price'], label='Sell', marker='v', color='red')
# plt.annotate(data2['Buy_Signal_Price'],data2['Sell_Signal_Price'])
plt.title('SBI Equity price trend')
plt.xlabel('Jan-1-2011 to Apr-30-2020')
plt.ylabel('Closing Price ')
plt.legend(loc='upper left')
plt.show()
