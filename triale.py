import pandas as pd
import os
import nsepy
import datetime
import openpyxl
import pytest

from datetime import timedelta  
os.chdir('/storage/emulated/0/Download')
date_y=datetime.date.today() - timedelta(days=2)
df = nsepy.get_history(symbol='SBIN', start=datetime.date(2020,5,1), end=datetime.date.today())
print(df)
'''
if (float(df.iloc[[-1]]['Open']) >= float(df.iloc[[-1]]['High'])):
	print('Sell Price',float(df.iloc[[-1]]['Open']))
	
elif (float(df.iloc[[-1]]['Open']) >= float(df.iloc[[-1]]['High'])):
	print('Buy Recommanded Price',float(df.iloc[[-1]]['Open']))
	
'''