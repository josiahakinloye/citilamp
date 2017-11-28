"""
This module contains everything that has to do with currency exchange
Tip: to get a list of valid short names of currencies visit https://free.currencyconverterapi.com/
and look at the select element on their web page or call this api https://free.currencyconverterapi.com/api/v5/currencies
"""

import requests


def convertCurrency(currency_from, currency_to, amount):
    """
    Converts a given currency to another using the value gotten from an api call
    to api_url variable.
    :param currency_from: type String The short name of the currency you are  converting from
    :param currency_to: type String The short of name of the currency you are converting to
    :param amount: type Int the amount of the currency_from  you want to convert
    :return: type Int the value of the amount when converted to the currency specified by the param currency_to
    """
    currency_from = str(currency_from).upper()
    currency_to = str(currency_to).upper()
    api_url = "https://free.currencyconverterapi.com/api/v5/convert?q=" + currency_from+"_"+currency_to +"&compact=y"
    res  = requests.get(api_url).json()
    convert_key= currency_from+"_"+currency_to
    try:
        current_rate = res[convert_key]['val']
    except:
        raise Exception("Api call was unsuccessful")
    return current_rate * amount

if __name__  == "__main__":
    print(convertCurrency("USD","NGN", 1))
