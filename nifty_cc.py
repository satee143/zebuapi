import openpyxl

import datetime
import pandas as pd

f_list = []
df_cols = ["LTP", 'Times']
df = pd.read_csv(str(datetime.date.today()) + '.csv', names=df_cols, index_col=1, parse_dates=True)
df.reset_index(inplace=True)
df['Times'] = [datetime.datetime.fromtimestamp(x) for x in df['Times']]
# df['Times']=pd.to_datetime(df['Times'], unit='s')
df.set_index('Times', inplace=True)
df = df['LTP'].resample('15min').ohlc().dropna()
# df=df.drop_duplicates(inplace=False)
print((df))
if (float(df.iloc[[1]]['high']) > float(df.iloc[[0]]['high']) and
        float(df.iloc[[1]]['low']) > float(df.iloc[[0]]['low'])):
    print('Nifty Future Sell Recommanded Price is  :', float(df.iloc[[1]]['low']))
    points = float(df.iloc[[1]]['high'] - df.iloc[[1]]['low'])
    print('Nifty Future buy target is :', float(df.iloc[[1]]['low']) - points)
    print('Nifty Future stoploss is :', float(df.iloc[[1]]['high']))
    f_list.append(datetime.date.today())
    f_list.append('NIFTY')
    f_list.append('SELL')
    f_list.append(float(df.iloc[[1]]['low']))
    f_list.append(float(float(df.iloc[[1]]['low']) - points))
    f_list.append(float(df.iloc[[1]]['high']))
    # zebu_api.place_bracket_order('NFO','NIFTYJUL20FUT','BO','BUY','DAY',10300,'l',75,10400,10200,20,)

elif (float(df.iloc[[1]]['low']) < float(df.iloc[[0]]['low']) and
      float(df.iloc[[1]]['high']) < float(df.iloc[[0]]['high'])):
    print('Nifty Future Buy Recommanded Price is  :', float(df.iloc[[1]]['high']))
    points = float(df.iloc[[1]]['high'] - float(df.iloc[[1]]['low']))
    print(points)
    print('Nifty Future sell target is :', float(df.iloc[[1]]['high']) + points)
    print('Nifty Future stoploss is :', float(df.iloc[[1]]['low']))
    f_list.append(str(datetime.date.today()))
    f_list.append('NIFTY')
    f_list.append('BUY')
    f_list.append(float(df.iloc[[1]]['high']))
    f_list.append(float(float(df.iloc[[1]]['high']) + points))
    f_list.append(float(df.iloc[[1]]['low']))

book = openpyxl.load_workbook('results.xlsx')
sheet = book.active

sheet.append(f_list)
book.save('results.xlsx')
