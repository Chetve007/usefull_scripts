import requests


def cur_converter(currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    rates = requests.get(url).json()["rates"]
    print(f"{currency} to RUB: {rates['RUB']}")


cur_converter('USD')
cur_converter('EUR')
