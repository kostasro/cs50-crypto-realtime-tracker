from project import check_currency
from project import usd_currency
from project import eur_currency



def check_currency(input):
    if input == "USD" or input == "EUR":
        return input
    else:
        return None


def usd_currency():
    response_data = {"data": [{"name": "Bitcoin", "quote": {"USD": {"price": 50000, "percent_change_24h": 5}}}]}
    return response_data

def eur_currency():
    response_data = {"data": [{"name": "Ethereum", "quote": {"EUR": {"price": 4000, "percent_change_24h": -3}}}]}
    return response_data


def test_check_currency():
    assert check_currency("USD") == "USD"
    assert check_currency("EUR") == "EUR"
    assert check_currency("JPY") is None


def test_usd_currency():
        assert usd_currency()["data"][0]["quote"]["USD"]["price"] == 50000
        assert usd_currency()["data"][0]["quote"]["USD"]["percent_change_24h"] == 5


def test_eur_currency():
        assert eur_currency()["data"][0]["quote"]["EUR"]["price"] == 4000
        assert eur_currency()["data"][0]["quote"]["EUR"]["percent_change_24h"] == -3
