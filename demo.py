import nsepy

import datetime

# df = nsepy.get_history(symbol='SBIN', start=date(2020,4,1), end=date(2020,5,30))
df = nsepy.get_history(symbol='TCS', start=datetime.date(2020, 6, 1), end=datetime.date(2020, 6, 12))
print(df)
