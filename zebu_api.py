import hashlib
import json

import jsonpath
import requests

global headers
global baseurl
baseurl = 'https://www.zebull.in/rest/MobullService/v1/'
headers = {'Content-Type': 'application/json'}


def get_encryption_key():
    url_pass = "customer/getAPIEncpkey"
    url = baseurl + url_pass
    payload = '{"userId": "DEL16035"}'
    # headers = {'Content-Type': 'application/json'}
    response = requests.post(url, payload, headers=headers)
    enc_key = jsonpath.jsonpath(json.loads(response.text), 'encKey')
    return enc_key[0]


def api_to_hash():
    uid = 'DEL16035'
    api = 'k6FgDo8BldvMAI5ko5XRb5DVxeRRUVpn9IZRPot2WE4ads5ACJxmIUP1bJDundKcE0Vvd2B31Y5KKMyrpYWUM2VvvKNjFnIRoMGUjJ0Q026u3MFWoP9hYPGWvQrqmMdp'
    str = uid + api + get_encryption_key()
    result = hashlib.sha256(str.encode())
    value = result.hexdigest()
    return value


def get_session_id():
    url_pass = "customer/getUserSID"
    url = baseurl + url_pass
    userdata = {'userId': 'DEL16035', 'userData': api_to_hash()}
    json_object = json.dumps(userdata)
    response = requests.post(url, json_object, headers=headers)
    session_id = jsonpath.jsonpath(json.loads(response.text), 'sessionID')
    return session_id[0]


def auther_key():
    static_text = 'Bearer'
    user_id = 'DEL16035'
    auth_key = static_text + " " + user_id + " " + get_session_id()
    return auth_key


def get_limits():
    url_pass = "limits/getRmsLimits"
    url = baseurl + url_pass
    payload = {}
    headers = {'Authorization': auther_key()}
    response = requests.get(url, payload, headers=headers)
    credits = jsonpath.jsonpath(response.json()[0], 'credits')
    return credits


def search_symbol(exchange, symbol):
    url = "https://www.zebull.in/rest/MobullService/exchange/getScripForSearch"
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    exchange = [exchange]
    payload = {'symbol': symbol, 'exchange': exchange}
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    token = response.json()
    # token = jsonpath.jsonpath(json.loads(response.text), 'token')
    # return int(token[0]['token'])
    return response.text


def place_regular_order(exchange, symbol, complexty, order_type, validity, price, price_type, quantity, discqty='0',
                        trigger_price='0',
                        product_code='mis'):
    url_pass = "placeOrder/executePlaceOrder"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}

    payload = {'complexty': complexty, 'trading_symbol': symbol, 'discqty': discqty, 'exch': exchange,
               'transtype': order_type.upper(), 'ret': validity.upper(), 'prctyp': price_type, 'qty': quantity,
               'symbol_id': '',
               'price': price, 'trigPrice': trigger_price, 'pCode': product_code}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def place_bracket_order(exchange, symbol, complexty, order_type, validity, price, price_type, quantity, target,
                        stoploss, t_stoploss, discqty='0', trigger_price='0',
                        product_code='mis'):
    url_pass = "placeOrder/executePlaceOrder"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'complexty': complexty, 'trading_symbol': symbol, 'discqty': discqty, 'exch': exchange,
               'transtype': order_type.upper(), 'ret': validity.upper(), 'prctyp': price_type, 'qty': quantity,
               'symbol_id': '35135',
               'price': price, 'trigPrice': trigger_price, 'pCode': product_code,
               'target': target, 'stopLoss': stoploss, 'trailing_stop_loss': t_stoploss}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def get_order_book():
    url_pass = "placeOrder/fetchOrderBook"
    url = baseurl + url_pass
    payload = {}
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    response = requests.get(url, payload, headers=headers)
    return response.text


def get_trade_book():
    url_pass = "placeOrder/fetchTradeBook"
    url = baseurl + url_pass
    payload = {}
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    response = requests.get(url, payload, headers=headers)
    return response.text


def modify_order(exchange, nest_ref, symbol, price, price_type, quantity, discqty='0', trigger_price='0'):
    url_pass = "placeOrder/executePlaceOrder"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'discqty': discqty, 'exch': exchange, 'filledQuantity': '0',
               'nestOrderNumber': nest_ref, 'trading_symbol': symbol,
               'prctyp': price_type, 'qty': quantity,
               'price': price, 'trigPrice': trigger_price, }
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def cancel_order(exchange, symbol, nest_ref):
    url_pass = "placeOrder/cancelOrder"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'exch': exchange,
               'nestOrderNumber': nest_ref, 'trading_symbol': symbol}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def nse_order_history(nest_ref):
    url_pass = "placeOrder/orderHistory"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'nestOrderNumber': nest_ref}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def get_holdings():
    url_pass = "positionAndHoldings/holdings"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def get_positions(retention):
    url_pass = "positionAndHoldings/positionBook"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'ret': retention}
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def conversion_position(exchange, quantity, symbol):
    url_pass = "positionAndHoldings/positionConvertion"
    url = baseurl + url_pass
    headers = {'Authorization': auther_key(), 'Content-Type': 'application/json'}
    payload = {'exch': exchange, 'productTocode': 'NRML', 'tsym': '',
               'qty': quantity, 'transtype': 'B', 'tokenNO': '', 'type': 'DAY',
               'pCode': 'MIS'
               }
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


def square_off_position(exchange, symbol, quantity, token):
    url_pass = "positionAndHoldings/sqrOofPosition"
    url = baseurl + url_pass
    payload = {'exchSeg': exchange, 'pCode': 'MIS', 'netQty': quantity, 'tokenNO': '', 'symbol': symbol}
    payload = [payload]
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


# print(place_regular_order())
print(place_bracket_order('NFO', 'indus', 'bo', 'BUY', 'DAY', 1350, 'L', '50', 3, 4, 5))
print(search_symbol('NFO', 'NIFTY23JUL2015200CE'))
