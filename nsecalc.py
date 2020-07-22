import pandas as pd
import os
import nsepy

import datetime
import openpyxl
import pytest
from datetime import timedelta
df = nsepy.get_history(symbol='SBIN', start=datetime.date(2020, 5, 20), end=datetime.date.today())
print(df)
