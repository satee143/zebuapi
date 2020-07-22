from nsepy import get_history
import pandas as pd
from datetime import date
data = get_history(symbol="SBIN", start=date(2020,1,1), end=date(2020,4,10))
import os
os.chdir('/storage/emulated/0/Download')
data.to_excel('val.xlsx')
print(type(data))