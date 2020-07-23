import datetime

s = datetime.datetime.now()
s1 = s + datetime.timedelta(days=1)
print(s)
print(s1.day)
