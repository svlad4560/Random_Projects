import requests
import json
# from datetime import datetime, date, time
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math
import pprint




td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time)
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
        updated_dates.append(new_vars)
    df_of_columns['date'] = updated_dates
    df_of_columns = df_of_columns.drop(columns = ["datetime"])
    return df_of_columns

trade_data_df = pd.read_csv('trades.csv')
datas =  get_price_history('TSLA', 'day',3,"minute",1)
datas.to_csv('WBT.csv')


trade_data_df['Open Datetime'] = pd.to_datetime(trade_data_df['Open Datetime'], format='%m/%d/%Y %H:%M')
# this is to get the correct time zone
# open_trade_time_list = []
# for i in trade_data_df['Open Datetime']:
#     minus_time = datetime.time(3,00,00)
#     open_trade_time = i.time()
#     date = datetime.date(1, 1, 1)
#     datetime1 = datetime.datetime.combine(date, open_trade_time)
#     datetime2 = datetime.datetime.combine(date, minus_time)
#     correct_time = datetime1 - datetime2
#     open_trade_time_list.append(correct_time)
#     # print(type(correct_time))
#
traded_symbols_list = list(trade_data_df['Symbol'])


percent_from_open_list = []
start_o = datetime.datetime.now()-datetime.timedelta(2)
end_o = datetime.datetime.now()-datetime.timedelta(1)

for i in range(len(trade_data_df)):
    trade_symbol = trade_data_df.iloc[i]['Symbol']
    opened_price = trade_data_df.iloc[i]['Entry Price']
    data = web.DataReader(trade_symbol, 'yahoo', start_o, end_o)
    underlying_open = data.iloc[-1]['Open']
    distance_from_open_percentage = ((opened_price - underlying_open)/underlying_open)*100
    distance_from_open_percentage = round(distance_from_open_percentage,2)
    percent_from_open_list.append(distance_from_open_percentage)

# print(percent_from_open_list)






# ____________________________________________________________________________
# date_needed = datetime.datetime.now() - datetime.timedelta(1)
# date_needed = date_needed.date()
# market_open_time = datetime.time(6,30,00)
#
# # this is to calculate where it is in its prir range
#
# for i in range(len(trade_data_df)):
#     trade_symbol = trade_data_df.iloc[i]['Symbol']
#     data = get_price_history(trade_symbol, 'day',2,"minute",1)
#     open_trade = trade_data_df.iloc[i]['Open Datetime']
#     opened_price = trade_data_df.iloc[i]['Entry Price']
#     open_trade_time = open_trade.to_pydatetime()
#     open_trade_time = open_trade_time.time()
#     lowes_list =[]
#     highes_list = []
#
#     for j in range(len(data)):
#
#         date = data.iloc[j]['date']
#         good_date = date.to_pydatetime()
#         hour = good_date.time()
#         date = good_date.date()
#         if date == date_needed and hour >= market_open_time and open_trade_time > hour:
#             low = data.iloc[j]['low']
#             high = data.iloc[j]['high']
#             # print(low,high,open_trade_time,hour)
#             print(hour)
#
#             lowes_list.append(low)
#             highes_list.append(high)
#
#     day_low = min(lowes_list)
#     day_high = max(highes_list)
#     midpoint = (day_low+day_high)/2
#     bottom_25 = (midpoint+day_low)/2
#     top_75 = (midpoint+ day_high) / 2
#     # if opened_price >= top_75:
#     #     day_range_value = 3
#     if opened_price >= midpoint:
#         range_value = 2
#         print('success')
#         print(range_value)
#     # if opened_price >= bottom_25 and opened_price <= midpoint:
#     #     day_range_value = 1
#     # if opened_price >= day_low and opened_price <= bottom_25:
#     #     day_range_value = 0
#
#     # print( midpoint, opened_price, range_value)
#     print(range_value)
#     x = 2
