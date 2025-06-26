import requests
import tabulate
import apikey


def main():
    currency_input = check_currency()
    if currency_input == "USD":
        usd_currency()
    else:
        eur_currency()


def check_currency():
    while True:
        user_input = input("Select your currency\nUSD or EUR: ")
        if user_input == "USD" or user_input == "EUR":
            return user_input
        else:
            print("The currency you have provided is not supported!")
            continue



def usd_currency():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'10',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apikey.api_key,
    }
    json = requests.get(url, params=parameters, headers=headers).json()
    coins = json["data"]
    table_data = []
    for coin in coins:
        name = coin["name"]
        price = coin["quote"]["USD"]["price"]
        change_24h = coin["quote"]["USD"]["percent_change_24h"]
        table_data.append([name, price, change_24h])
    print(tabulate.tabulate(table_data, headers=["Name", "Price (USD)", "24h % Change"], tablefmt="grid", numalign="center"))


def eur_currency():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'10',
    'convert':'EUR'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apikey.api_key,
    }
    json = requests.get(url, params=parameters, headers=headers).json()
    coins = json["data"]
    table_data = []
    for coin in coins:
        name = coin["name"]
        price = coin["quote"]["EUR"]["price"]
        change_24h = coin["quote"]["EUR"]["percent_change_24h"]
        table_data.append([name, price, change_24h])
    print(tabulate.tabulate(table_data, headers=["Name", "Price (EUR)", "24h % Change"], tablefmt="grid", numalign="center"))



if __name__ == "__main__":
    main()

