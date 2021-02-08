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
    open_list = [df_of_columns['open']]
    high_list = [df_of_columns['high']]
    low_list = [df_of_columns['low']]
    volume_list = [df_of_columns['volume']]
    date_list = [df_of_columns['date']]



data = get_price_history("AAPL","day",10,"minute", 1)

# What do I want to accomplish?
    # Check avg bar range and volume avergage.


bar_range_list = []
for i in range(len(open_list)):
    top = high_list[i]
    bottom = low_list[i]
    ranges = top - bottom
    bar_range_list.append(ranges)

average_bar = sum(bar_range_list)/ len(bar_range_list)
print(average_bar)

avg_list = []
for i in range(len(volume_list)):
    avg_list.append(volume_list[i])
avg_num = sum(avg_list)/len(avg_list)
print(avg_num)
# print(volume_list)
