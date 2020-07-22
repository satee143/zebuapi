import numpy as np

import pandas as pd

ds = pd.date_range('01/02/2020', periods=7)
x = pd.DataFrame(np.arange(7), index=ds)
y = (pd.Series(np.arange(7), index=ds))
print(x.dtypes)
print(y.dtypes)
