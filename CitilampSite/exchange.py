


#brl_money = convert_money(100,"USD","NGN")

#print(brl_money)

import requests

res = requests.get("https://openexchangerates.org/api/convert/19999.95/GBP/EUR?app_id=1a4a43cc9b274f2884e120cd54c827c9").json()

print(res)