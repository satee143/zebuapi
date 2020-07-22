import pandas as pd 
import os
import numpy as np
from sklearn.svm import  SVR
import matplotlib.pyplot as plt


os.chdir('/storage/emulated/0/bluetooth')
df= pd.read_excel("c.xlsx")
#print('Raw data from Yahoo Finance : ')
#print(df.head(10))

dates=[]
prices=[]
#print(df.shape)
#print(df.tail(1))

df=df.head(28)
#print(df.shape)
df['Date']=pd.to_datetime(df['Date'])
df['day']=df['Date'].dt.day
print(df)
df_dates=df.loc[:,'day']
df_close=df.loc[:,'Close']


for date in df_dates:
	dates.append([int(date)])
#print(dates)
	
for amt in df_close:
	prices.append(float(amt))
#print(price)

def pred_prices(dates,price,x):
	svr_lin=SVR(kernel='linear',C=1e3)
	svr_poly=SVR(kernel='poly',C=1e3,degree=2)
	svr_rbf=SVR(kernel='rbf',C=1e3,gamma='auto')
	
	svr_lin.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)
	
	plt.scatter(dates,prices,color='black',label='Data')
	plt.scatter(dates,svr_rbf.predict(dates),color='red',label='RBF')
	plt.scatter(dates,svr_lin.predict(dates),color='green',label='Linear')
	plt.scatter(dates,svr_poly.predict(dates),color='blue',label='Polynominal')
	plt.xlabel('Dates')
	plt.ylabel('price')
	plt.title('Prediction')
	plt.legend()
	plt.show()
	
	return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]
	
	
predicted_prices=pred_prices(dates,prices,[[3]])
print(predicted_prices)

'''#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Symbol',axis=1) 
data = data.drop('Series',axis=1) 
data = data.drop('Prev Close',axis=1) 
data = data.drop('Last',axis=1) 
print('\n\nData after removing Date and Adj Close : ')
print(data.head())
#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)
#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))

error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

from matplotlib import  pyplot as plt
#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Tesla Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
#plt.show()
'''