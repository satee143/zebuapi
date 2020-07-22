from nsepy import get_history

from datetime import date

data = get_history(symbol='SBIN', start=date(2009, 1, 1), end=date(2020, 4, 17))
data.to_excel('nsehistory1.xlsx')
