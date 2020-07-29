import requests
url='https://chartink.com/screener/copy-first-15-minute-high-low-stock-breakouts-12'
req=requests.get(url)
print(req.status_code)
