from nsepy import get_history

from datetime import date

sbin = get_history(symbol='DMART',
                   start=date(2020, 5, 15),
                   end=date(2020, 5, 21))
print(sbin)
