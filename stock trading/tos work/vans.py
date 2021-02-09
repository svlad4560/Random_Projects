import requests
import json
import pprint
import pandas as pd
import datetime


td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}&needExtendedHoursData={needExtendedHoursData}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time,needExtendedHoursData=False)
    # endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
    page = requests.get(url=full_url_price_history, params={'apikey' : td_consumer_key})
    # look at content and convert into list / dict
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

data_S = get_price_history("SPY", 'day',1,"minute",1)
volume_list = list(data_S['volume'])
high_list = list(data_S['high'])
low_list = list(data_S['low'])
avg_volume = sum(volume_list)/len(volume_list)
range_list = []
for i in range(len(data_S)):
    bar_range = high_list[i]- low_list[i]
    # if bar_range != 0 :
    #     range_list.append(bar_range)
    range_list.append(bar_range)
    print(bar_range)


avg_bar = sum(range_list)/ len(range_list)
# print(avg_bar)
# print(avg_volume)
# print(data_S)
