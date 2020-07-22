from nsetools import Nse

nse = Nse()
q = nse.get_quote('infy')
print(type(q))
# pprint(q)
