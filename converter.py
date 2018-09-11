import requests


API_URL = 'https://free.currencyconverterapi.com/api/v6'


def convert(value: float, currency_from: str = 'USD', currency_to: str = 'RUB'):
    """Converts from currency_from to currency_to."""
    from_to = '{}_{}'.format(currency_from, currency_to)
    res = requests.get(API_URL + '/convert?q={}&compact=y'.format(from_to))
    if res.status_code != 200:
        raise RequestError(res.text)
    final_res = res.json()
    exchange = final_res[from_to]['val']
    return exchange * value


class RequestError(Exception):
    """Something went wrong"""

    pass
