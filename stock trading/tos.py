import requests

key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'


def get_price_history(**kwargs):
    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))

    params = {}
    params.update({'apikey': key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    return requests.get(url, params=params).json()

print(get_price_history(symbol='AAPL', period=1, periodType='day', frequencyType='minutes'))
