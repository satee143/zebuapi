import hashlib

uid = 'DEL16035'
api = 'k6FgDo8BldvMAI5ko5XRb5DVxeRRUVpn9IZRPot2WE4ads5ACJxmIUP1bJDundKcE0Vvd2B31Y5KKMyrpYWUM2VvvKNjFnIRoMGUjJ0Q026u3MFWoP9hYPGWvQrqmMdp'
enc = 'O0YSP7VP6T27RU54Q2M474H9J16L3D11'

str = uid + api + enc
result = hashlib.sha256(str.encode())
value = result.hexdigest()
print(value)
