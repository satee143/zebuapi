from alice_blue import *

access_token = AliceBlue.login_and_get_access_token(username='AB102865', password='sampath@9', twoFA='a',
                                                    api_secret='CW7LT01PAQRAVVUFQ0VH0PGXV1VJUG10RGWK3IAMIJGHJ1KCXYU1QBZWQJZ1FR53')
alice = AliceBlue(username='AB102865', password='sampath@9', access_token=access_token,
                  master_contracts_to_download=['NSE', 'BSE', 'MCX', 'NFO'])
socket_opened = True
print(alice.get_all_subscriptions())
