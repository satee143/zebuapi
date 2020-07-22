from datetime import date
from nsepy import get_history
sbin = get_history(symbol='DMART',
                   start=date(2020,5,15),
                   end=date(2020,5,21))
print(sbin)