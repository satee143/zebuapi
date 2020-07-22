import nsepy

import datetime

df = nsepy.get_history(symbol='SBIN', start=datetime.date(2020, 5, 20), end=datetime.date.today())
print(df)
