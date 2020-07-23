import matplotlib.pyplot as plt
import nsepy

import datetime

# df = nsepy.get_history(symbol='SBIN', start=date(2020,4,1), end=date(2020,5,30))
df = nsepy.get_history(symbol='TCS', start=datetime.date(2020, 1, 1), end=datetime.date(2020, 6, 24))

window_length = 14
close = df['Close']
delta = close.diff()
# print(delta)
# Get rid of the first row, which is NaN since it did not have a previous 
# row to calculate the differences
delta = delta[1:]

# Make the positive gains (up) and negative gains (down) Series
up, down = delta.copy(), delta.copy()
up[up < 0] = 0
down[down > 0] = 0

# Calculate the EWMA
roll_up1 = up.ewm(span=window_length).mean()
roll_down1 = down.abs().ewm(span=window_length).mean()

# Calculate the RSI based on EWMA
RS1 = roll_up1 / roll_down1
RSI1 = 100.0 - (100.0 / (1.0 + RS1))

# Calculate the SMA
roll_up2 = up.rolling(window_length).mean()
roll_down2 = down.abs().rolling(window_length).mean()

# Calculate the RSI based on SMA
RS2 = roll_up2 / roll_down2
RSI2 = 100.0 - (100.0 / (1.0 + RS2))
print(RSI2[RSI2 >= 60])
df['RSI'] = RSI2
df.to_excel('rsi.xlsx')
# Compare graphically
plt.figure(figsize=(8, 6))
# df['Close'].plot()
# RSI1.plot()
RSI2.plot()
plt.legend(['RSI via EWMA', 'RSI via SMA'])
plt.show()
