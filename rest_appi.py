import requests
from requests.auth import HTTPBasicAuth
import jsonpath
import json
r = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('satee143@gmail.com', 'Satee@1432'))
print(r.content)
print(r.encoding)