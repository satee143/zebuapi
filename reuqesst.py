import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
         'Accept-Language':'en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,te;q=0.6,en-US;q=0.5,en-GB;q=0.4',
         'Accept-Encoding': 'gzip, deflate, br'}
# resp=requests.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json',headers=headers).json()
# print(resp['data'][0]['symbol'],resp['data'][0]['netPrice'])
# print(resp['data'][1]['symbol'],resp['data'][1]['netPrice'])
# print(resp['data'][0])
#
#
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#          'Accept-Language':'en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,te;q=0.6,en-US;q=0.5,en-GB;q=0.4',
#          'Accept-Encoding': 'gzip, deflate, br'}
# resp=requests.get('https://www1.nseindia.com/homepage/Indices1.json',headers=headers).json()
#
# print(resp['data'][0]['change'])
#
# resp = requests.get('https://www1.nseindia.com/homepage/Indices1.json', headers=headers).json()
# nifty_percentage = float(resp['data'][1]['change'])
# print((nifty_percentage))

resp=requests.get('https://www.nseindia.com/api/liveEquity-derivatives?index=top20_contracts',headers=headers).json()
a=resp['data']
result= [x for x in a if x['underlying']=='NIFTY' and x['instrumentType']=="FUTIDX"]
print(result)
print(result[0]['lastPrice'],result[0]['change'],result[0]['pChange'])






resp=requests.get('https://www.nseindia.com/api/quote-derivative?symbol=NIFTY&identifier=FUTIDXNIFTY30-07-2020XX0.00',headers=headers).json()
a=resp['metadata'][0]
print(a)