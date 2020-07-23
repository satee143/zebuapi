import numpy as np

import pandas as pd

l = [10, 20, 30]
x = pd.Series(l)
y = np.array(l)
print(x)
print(y)
print(type(y))
