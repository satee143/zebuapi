import numpy as np
from nsepy import get_history

from datetime import date

data = get_history(symbol='ONGC', start=date(2020, 1, 1), end=date(2020, 4, 17))
print(data)
# print(len(data))
data['sno'] = np.arange(0, len(data), step=1)
data.reset_index('Date', inplace=True)
print(data)
data.set_index('sno', inplace=True)
print(data.columns.values)
print(data)
