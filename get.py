import json

import jsonpath
import requests

uri = 'https://reqres.in/api/users?page=2'
request = requests.get(uri)
print(request.headers.get('Server'))
# print(request.content)
# print(request.cookies)
# print(request.elapsed)
# print(request.status_code)
req_con = request.content
json_res = json.loads(req_con)
# print(json_res)
l2 = ['Holt', 'Meorris', 'Ramos']
l1 = []
for i in range(3):
    l = jsonpath.jsonpath(json_res, 'data[' + str(i) + '].last_name')
    # print(l)
    l1.append(l[0])

print(l1)
for i in range(len(l1)):
    if l1[i] in l2:
        print('avalible')

    else:
        print(l1[i], 'not avable')
