import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import itertools
import requests
import json
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
    # df_of_columns = df_of_columns.drop(columns = ["date"])

    return df_of_columns
traded = ['GME','AAPL']
end_atr = datetime.datetime.now()
start_atr = end_atr-datetime.timedelta(30)
final_atr_display_list = []
# this is to get a 30 day atr
for m in traded:
    atr_list = []

    df = web.DataReader(m, 'yahoo', start_atr, end_atr)

    for i in range(len(df)):

        atr_high = df.iloc[i]['High']
        atr_low = df.iloc[i]['Low']

        atr = atr_high - atr_low

        atr_list.append(atr)

        true_atr = sum(atr_list) / len(atr_list)

    final_atr_display_list.append(true_atr)
# print(final_atr_display_list)

gme_df = web.DataReader('GME', 'yahoo', start_atr, end_atr)

trade_data_df = pd.read_csv('trades.csv')

market_open_time = datetime.time(6,30,00)
market_close_time = datetime.time(13,00,00)
premarket_df = pd.DataFrame()
postmarket_df = pd.DataFrame()
non_market_hours_value_list = []
for i in traded:
    data_S = get_price_history(i, 'day',2,"minute",5)

    premarket_high_list = []
    premarket_low_list = []
    postmarket_high_list = []
    postmarket_low_list = []

    for j in range(len(data_S)-1):
        date = data_S.iloc[j]['date']
        good_date = date.to_pydatetime()
        hour = good_date.time()
        date = good_date.date()


        pre_market_date = datetime.datetime.now()
        pre_market_date = pre_market_date.date()
        # pre_market_date = pre_market_date - datetime.timedelta(3)

        post_marekt_date = datetime.datetime.now()
        post_marekt_date = post_marekt_date.date()
        post_marekt_date = post_marekt_date - datetime.timedelta(3)

        if date == pre_market_date and hour == market_open_time:
            opening_price = data_S.iloc[j]['open']

        if hour > market_close_time and date ==  post_marekt_date:
            pm_high = data_S.iloc[j]['high']
            pm_low = data_S.iloc[j]['low']

            postmarket_high_list.append(pm_high)
            postmarket_low_list.append(pm_low)

        if hour < market_open_time and date == pre_market_date:
            high = data_S.loc[j]['high']
            low = data_S.iloc[j]['low']

            premarket_high_list.append(high)
            premarket_low_list.append(low)

    # so the issue is that the len of GME premarket_high_list is 50 while the len of AAPL premarket_high_list is 64

    pre_market_high = max(premarket_high_list)
    pre_market_low = min(premarket_low_list)
    post_market_high = max(postmarket_high_list)
    post_market_low = min(postmarket_low_list)

    if pre_market_high > post_market_high:
        non_market_hours_high = pre_market_high
    else:
        non_market_hours_high = post_market_high

    if pre_market_low < post_market_low:
        non_market_hours_low = pre_market_low
    else:
        non_market_hours_low = post_market_low

    # yikes this is going to need to be fixed
    non_market_hours_midpoint = (non_market_hours_high + non_market_hours_low) / 2
    non_market_hours_75 = (non_market_hours_midpoint+non_market_hours_high) /2
    non_market_hours_25 = (non_market_hours_midpoint+non_market_hours_low) /2

    if opening_price > non_market_hours_high:
        non_market_hours_value = 5
    if ((opening_price < non_market_hours_high) and (opening_price > non_market_hours_75)):
        non_market_hours_value = 4
    if ((opening_price < non_market_hours_75) and (opening_price > non_market_hours_midpoint)):
        non_market_hours_value = 3
    if ((opening_price < non_market_hours_midpoint) and (opening_price > non_market_hours_25)):
        non_market_hours_value = 2
    if ((opening_price < non_market_hours_25) and (opening_price > non_market_hours_low)):
        non_market_hours_value = 1
    if (opening_price < non_market_hours_low):
        non_market_hours_value = 0

    

    non_market_hours_value_list.append(non_market_hours_value)

print(non_market_hours_value_list)
# list_final = []
# list_a = []
# list_b = []
# for i in range(2):
#     list_a.append(i)
#     for j in range(1):
#         list_b.append(j)
#     list_final.append(list_a)
#     list_final.append(list_b)
#
# print(list_final)
