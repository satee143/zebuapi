import json

import jsonpath
import requests

import zebu_api

url = "https://www.zebull.in/rest/MobullService/v1/limits/getRmsLimits"
a = 'Bearer'
u = 'DEL16035'
m = a + ' ' + u + ' ' + zebu_api.get_session_key()

payload = {}
headers = {
    'Authorization': m}

response = requests.request("GET", url, headers=headers, data=payload)
credits = jsonpath.jsonpath(json.loads(response.content)[0], 'credits')
print(credits)
print(json.loads(response.content)[0])

# print(type(response.text))
# print(response.text.encode('utf8'))
