def reg_order():
    import requests

    url = "https://www.zebull.in/rest/MobullService/v1/placeOrder/executePlaceOrder"

    payload = "[\r\n  {\r\n   \"complexty\": \"regular\",\r\n    \"discqty\": \"0\",\r\n    \"exch\": \"NSE\",\r\n    \"pCode\": \"mis\",\r\n    \"prctyp\": \"L\",\r\n    \"price\": \"68.70\",\r\n    \"qty\": 1,\r\n    \"ret\": \"DAY\",\r\n    \"symbol_id\": \"212\",\r\n    \"trading_symbol\": \"ASHOKLEY-EQ\",\r\n    \"transtype\": \"BUY\",\r\n    \"trigPrice\": \"\"\r\n  }\r\n]"
    headers = {
        'Authorization': 'Bearer DEL16035 WaV3lZSKVtR91XH1kH6CMWeiaiY3K2C0WxOYsalrEjZVhutlu9UQiQdVGbEqZtavMUuBzXtZKj1lKSglFD6MyRyboJXXkTfhaYsKZ084oa2ZbYEWGvXL3dZKjaRaHAeE8EJji7Tyk3TfUriqz4sU4c1vDZuHOyVZmnKQS0ASL6FSVEf13TgNiYBqOqPSAyTzOOt9PnfWu3oNqOhGjB2f3XbjX9qJGn7hAzQl7tn0v6Y8usKaUOPtkf3Yfrz3jtM7',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def bracket_order():
    import requests

    url = "https://www.zebull.in/rest/MobullService/v1/placeOrder/executePlaceOrder"

    payload = "[\r\n  {\r\n    \"complexty\": \"bo\",\r\n    \"discqty\": \"0\",\r\n    \"exch\": \"NSE\",\r\n    \"pCode\": \"mis\",\r\n    \"prctyp\": \"L\",\r\n    \"price\": \"61\",\r\n    \"qty\": 10,\r\n    \"ret\": \"DAY\",\r\n    \"stopLoss\": 1,\r\n    \"symbol_id\": \"212\",\r\n    \"target\": 1,\r\n    \"trading_symbol\": \"ASHOKLEY-EQ\",\r\n    \"trailing_stop_loss\": 20,\r\n    \"transtype\": \"buy\",\r\n    \"trigPrice\": \"\"\r\n  }\r\n]"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer DEL16035 WaV3lZSKVtR91XH1kH6CMWeiaiY3K2C0WxOYsalrEjZVhutlu9UQiQdVGbEqZtavMUuBzXtZKj1lKSglFD6MyRyboJXXkTfhaYsKZ084oa2ZbYEWGvXL3dZKjaRaHAeE8EJji7Tyk3TfUriqz4sU4c1vDZuHOyVZmnKQS0ASL6FSVEf13TgNiYBqOqPSAyTzOOt9PnfWu3oNqOhGjB2f3XbjX9qJGn7hAzQl7tn0v6Y8usKaUOPtkf3Yfrz3jtM7'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def market_order():
    import requests

    url = "https://www.zebull.in/rest/MobullService/v1/placeOrder/executePlaceOrder"

    payload = "[\r\n  {\r\n    \"complexty\": \"regular\",\r\n    \"discqty\": \"0\",\r\n    \"exch\": \"NSE\",\r\n    \"pCode\": \"mis\",\r\n    \"prctyp\": \"MKT\",\r\n    \"price\": \"\",\r\n    \"qty\": 20,\r\n    \"ret\": \"DAY\",\r\n    \"symbol_id\": \"212\",\r\n    \"trading_symbol\": \"ASHOKLEY-EQ\",\r\n    \"transtype\": \"BUY\",\r\n    \"trigPrice\": \"\"\r\n  }\r\n]"
    headers = {
        'Authorization': 'Bearer DEL16035 WaV3lZSKVtR91XH1kH6CMWeiaiY3K2C0WxOYsalrEjZVhutlu9UQiQdVGbEqZtavMUuBzXtZKj1lKSglFD6MyRyboJXXkTfhaYsKZ084oa2ZbYEWGvXL3dZKjaRaHAeE8EJji7Tyk3TfUriqz4sU4c1vDZuHOyVZmnKQS0ASL6FSVEf13TgNiYBqOqPSAyTzOOt9PnfWu3oNqOhGjB2f3XbjX9qJGn7hAzQl7tn0v6Y8usKaUOPtkf3Yfrz3jtM7',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
