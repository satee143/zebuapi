import os

import numpy as np
from matplotlib import pyplot as plt
from nsepy import get_history

import datetime
import pandas as pd

quote = 'infy'
# quote=input('Enter the NSE Symbol')

data = get_history(symbol=quote, start=datetime.date(2015, 6, 1), end=datetime.date.today())
plt.style.use('fivethirtyeight')

data['sno'] = np.arange(0, len(data), step=1)
data.reset_index('Date', inplace=True)
data.set_index('sno', inplace=True)

'''os.chdir('/storage/emulated/0/bluetooth')
data = pd.read_excel("c.xlsx")
#print('Raw data from Yahoo Finance : ')
#print(data.head())
'''

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
#plt.show()'''

data2 = pd.DataFrame()
data2[quote] = data['Close']
data2['SMA30'] = SMA30['Close']
data2['SMA100'] = SMA100['Close']
data2['day'] = data['Date']


# print(data2)


def buy_sell(data2):
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


buy_sell = buy_sell(data2)
data2['Buy_Signal_Price'] = buy_sell[0]
data2['Sell_Signal_Price'] = buy_sell[1]

print(data2)
data2.set_index('day', inplace=True)
plt.figure(figsize=(40.5, 9.5), dpi=150)
plt.plot(data2[quote], label=quote)
plt.plot(data2['SMA30'], label='SMA30', alpha=0.6)
plt.plot(data2['SMA100'], label='SMA100', alpha=0.8)
plt.scatter(data2.index, data2['Buy_Signal_Price'], label='Buy', marker='^', color='green', linewidths=10)

plt.scatter(data2.index, data2['Sell_Signal_Price'], label='Sell', marker='v', color='red', alpha=1, linewidths=10)
# plt.annotate(data2['Buy_Signal_Price'],data2['Sell_Signal_Price'])
plt.title(quote + ' Equity price trend')
plt.xlabel('June-1-2011 to ' + str(datetime.date.today()))
# plt.yticks([100,150,200,250,300])
# plt.xticks(np.arange(datetime(2014,11,20), datetime(2020,4,30), timedelta(days=160)).astype(datetime))
plt.yticks(np.arange(round(int(min(data2[quote])), -1), int(max(data2[quote])), step=100))
plt.ylabel('Closing Price ')
plt.legend(loc='upper left')
os.chdir('/storage/emulated/0/bluetooth')

plt.savefig(quote + '.png')
plt.show()
