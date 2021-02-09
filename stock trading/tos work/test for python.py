import requests
import json
import pprint
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import smtplib
from email.message import EmailMessage
import datetime

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    global open_list
    global high_list
    global low_list
    global volume_list
    global date_list
    global df_of_columns

    # open_list = []
    # high_list = []
    # low_list = []
    # volume_list = []
    # date_list = []

    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}&needExtendedHoursData={needExtendedHoursData}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time,needExtendedHoursData = False)
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
    open_list = list(df_of_columns['open'])
    high_list = list(df_of_columns['high'])
    low_list = list(df_of_columns['low'])
    volume_list = list(df_of_columns['volume'])
    date_list = list(df_of_columns['date'])

    return df_of_columns

data = get_price_history("AAPL","day",10,"minute", 1)

def find_averages(data):
    avg_volume = sum(volume_list) / len(volume_list)

    avg_range_list = []
    for i in range(len(data)):
        high = high_list[i]
        low = low_list[i]
        ranges = high - low
        avg_range_list.append(ranges)

    avg_range = sum(avg_range_list)/ len(avg_range_list)

    count_how_many = 0
    for i in avg_range_list:
        if i > avg_range:
            count_how_many+1

    return avg_volume ,avg_range, count_how_many

print(find_averages(data))
