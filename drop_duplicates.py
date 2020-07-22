import os

import pandas as pd

os.chdir('/storage/emulated/0/Download')
df = pd.read_excel('quote_list.xlsx', 'quote')
# print(df)
pf = df.drop_duplicates(keep=False)
pf.to_excel('quote_list.xlsx', 'quote1')
'''
book=openpyxl.load_workbook('quote_list.xlsx')
sheet=book.active
for row in pf:
	sheet.append(row)
	
book.save('ledger.xlsx')
'''
