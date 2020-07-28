import pandas as pd
import datetime
import openpyxl


f_list=[]

#Read  nifty csv
df_cols = ["LTP", 'Times']
df = pd.read_csv(str(datetime.date.today()) + '.csv', names=df_cols, index_col=1, parse_dates=True)
df.reset_index(inplace=True)
df['Times'] = [datetime.datetime.fromtimestamp(x) for x in df['Times']]
# df['Times']=pd.to_datetime(df['Times'], unit='s')
df.set_index('Times', inplace=True)
df = df['LTP'].resample('30min',base=15).ohlc().dropna()
# df=df.drop_duplicates(inplace=False)
print((df))


#Read  banknifty csv
df_cols2 = ["LTP", 'Times']
df2 = pd.read_csv(str(datetime.date.today()) + 'bn.csv', names=df_cols2, index_col=1, parse_dates=True)

df2.reset_index(inplace=True)
df2['Times'] = [datetime.datetime.fromtimestamp(x) for x in df2['Times']]
# df['Times']=pd.to_datetime(df['Times'], unit='s')
df2.set_index('Times', inplace=True)

df2 = df2['LTP'].resample('30min',base=15).ohlc().dropna()
# df=df.drop_duplicates(inplace=False)
print((df2))



if (float(df.iloc[[2]]['close']) >float(df.iloc[[2]]['open']) and float(df2.iloc[[2]]['close']) <float(df2.iloc[[2]]['open'])):
    print('nifty buy recommanded is :',float(df[[2]]['high']))
    print('nifty  stoploss is :',float(df[[2]]['low']))
    
    print('bank nifty sell recommanded is :',float(df2[[2]]['low']))
    
    print('bank nifty stop loss  is :',float(df2[[2]]['high']))
 
    f_list.append(datetime.date.today())
    f_list.append('NIFTY')
    f_list.append('BUY')
    f_list.append(float(df.iloc[[2]]['high']))
    f_list.append(float(df.iloc[[2]]['low']))
    f_list.append('BANK NIFTY')
    f_list.append('SELL')
    f_list.append(float(df2.iloc[[2]]['low']))
    f_list.append(float(float(df2.iloc[[2]]['high'])))
   
elif (float(df.iloc[[2]]['close']) <float(df.iloc[[2]]['open']) and float(df2.iloc[[2]]['close']) >float(df2.iloc[[2]]['open'])):
    print('nifty sell recommanded is :',float(df[[2]]['low']))
    print('nifty  stoploss is :',float(df[[2]]['high']))
    
    print('bank nifty buy recommanded is :',float(df2[[2]]['high']))
    
    print('bank nifty stop loss  is :',float(df2[[2]]['low']))
 
    f_list.append(datetime.date.today())
    f_list.append('NIFTY')
    f_list.append('SELL')
    f_list.append(float(df.iloc[[2]]['low']))
    f_list.append(float(df.iloc[[2]]['high']))
    f_list.append('BANK NIFTY')
    f_list.append('BUY')
    f_list.append(float(df2.iloc[[2]]['high']))
    f_list.append(float(float(df2.iloc[[2]]['low'])))
   
    
   



book = openpyxl.load_workbook('impulse_bank_results.xlsx')
sheet = book.active

sheet.append(f_list)
book.save('impulse_bank_results.xlsx')