import datetime
import requests
import json
import pandas as pd
import pprint

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time)
    # endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
    page = requests.get(url=full_url_price_history, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    data = pd.DataFrame(data=content)
    df_of_columns = data["candles"].apply(pd.Series)
    updated_dates = []
    test_dates = list(df_of_columns['datetime'])

    for var in test_dates:
        times = var
        new_vars = datetime.datetime.fromtimestamp(times / 1e3)
        updated_dates.append(str(new_vars))
    df_of_columns['date'] = updated_dates
    df_of_columns = df_of_columns.drop(columns = ["datetime"])

    return df_of_columns



#
data_S = get_price_history("AAPL","day",10,"minute", 10)

def get_movers():
    url = 'https://api.tdameritrade.com/v1/marketdata/{index}/movers?direction={direction}'
    full_url = url.format(index = '$COMPX', direction = 'up')
    page = requests.get(url=full_url, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    return content

# print(new_var)
# print(updated_dates)
pprint.pprint(data_S)
