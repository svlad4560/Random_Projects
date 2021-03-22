import requests
import json
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

    # hour_dates = []
    # for i in updated_dates:
    #     hour = i.time()
    #     hour_dates.append(hour)
    #
    # short_hand_date_list = []
    # for i in updated_dates:
    #     date = i.date()
    #     short_hand_date_list.append(date)
    #
    # df_of_columns['hour'] = hour_dates
    # df_of_columns['short date'] = short_hand_date_list
    df_of_columns = df_of_columns.drop(columns = ["datetime"])
    # df_of_columns = df_of_columns.drop(columns = ["date"])

    return df_of_columns

data_S = get_price_history("AMD", 'year',1,"daily",1)
# print(type(data_S.iloc[0]['date']))
traded_symbols = ['FUTU']
# traded_symbols = list(trade_data_df['Symbol'])



def find_trade_varaiables():
    # find the gap percentage, where it is on the daily 5 day range and 21 day range, avg volume, price, volume on the day, float, insituitional owner ship. where did it open compared to premarket,
    trade_data_df = pd.read_csv('trades.csv')

    end = datetime.datetime.now()
    start = end-datetime.timedelta(365)

    big_picture_range_value_list = []
    five_day_range_value_list = []
    average_volume_list = []
    gap_percentage_list = []
    atr_list = []
    premarket_df = pd.DataFrame()
    postmarket_df = pd.DataFrame()
    premarket_high_list = []
    premarket_low_list = []
    postmarket_high_list = []
    postmarket_low_list = []
    non_market_hours_value_list = []
    final_test_list =[]

    for i in trade_data_df['Symbol']:

        df = web.DataReader(i, 'yahoo', start, end)
        # # TODO: delete the shit columns
        # TODO: make also check if on that day do we go to the low and test?

        closing_prices = df['Close']
        highs = df.iloc[:-1]['High']
        lows = df.iloc[:-1]['Low']
        opening_price = df.iloc[-1]['Open']
        prior_close = df.iloc[-2]['Close']

        gap_percentage = ((opening_price-prior_close)/prior_close ) *100
        gap_percentage = round(gap_percentage,2)
        gap_percentage_list.append(gap_percentage)

        big_picture_range = max(highs)-min(lows)

        midpoint = (max(highs) + min(lows) ) / 2
        midpoint_25 = (midpoint + min(lows) ) / 2
        midpoint_75 = (midpoint + max(highs) ) / 2

        if opening_price > max(highs):
            # opening above yearly high
            range_value = 5
        if ((opening_price < max(highs)) and (opening_price > midpoint_75)):
            #opening between yearly high and 75
            range_value = 4
        if ((opening_price < midpoint_75) and (opening_price > midpoint)):
            #opening between midpoint and 75
            range_value = 3
        if ((opening_price < midpoint) and (opening_price > midpoint_25)):
            # opening between 25 and midpoint
            range_value = 2
        if ((opening_price < midpoint_25) and (opening_price > min(lows))):
            # opening between low and 25
            range_value = 1
        if opening_price < min(lows):
            # opening below yearly low
            range_value = 0

        big_picture_range_value_list.append(range_value)

        five_day_range_high = highs.iloc[len(highs)-5:len(highs)]
        actual_high = max(five_day_range_high)


        five_day_range_low = lows.iloc[len(highs)-5:len(highs)]
        actual_low = min(five_day_range_low)

        five_day_range_midpoint = (actual_high + actual_low) / 2
        five_day_range_25 = (actual_low + five_day_range_midpoint) / 2
        five_day_range_75 = (actual_high + five_day_range_midpoint) / 2


        if opening_price > actual_high:
            five_day_range_value = 5
        if ((opening_price < actual_high) and (opening_price > five_day_range_75)):
            five_day_range_value = 4
        if ((opening_price < five_day_range_75) and (opening_price > five_day_range_midpoint)):
            five_day_range_value = 3
        if ((opening_price < five_day_range_midpoint) and (opening_price > five_day_range_25)):
            five_day_range_value = 2
        if ((opening_price < five_day_range_25) and (opening_price > actual_low)):
            five_day_range_value = 1
        if (opening_price < actual_low):
            five_day_range_value = 0

        five_day_range_value_list.append(five_day_range_value)

        # this is the average of the year but it can be changed
        avg_volume = df.Volume.mean()
        average_volume_list.append(avg_volume)
#_____________________________________________________________________________________________________________________________________________
        #premarket ranges
        data_S = get_price_history(i, 'day',2,"minute",5)
        # data_S.to_csv('timedatesshit.csv')

        market_open_time = datetime.time(6,30,00)
        market_close_time = datetime.time(13,00,00)

        for j in range(len(data_S)-1):
            # print('starting j loop')
            date = data_S.iloc[j]['date']
            good_date = date.to_pydatetime()
            hour = good_date.time()
            date = good_date.date()

            pre_market_date = datetime.datetime.now()
            pre_market_date = pre_market_date.date()
            pre_market_date = pre_market_date - datetime.timedelta(2)

            post_marekt_date = datetime.datetime.now()
            post_marekt_date = post_marekt_date.date()
            post_marekt_date = post_marekt_date - datetime.timedelta(3)

            if hour > market_close_time and date ==  post_marekt_date:
                global pm_high
                pm_high = data_S.iloc[j]['high']
                pm_low = data_S.iloc[j]['low']
                print(pm_high)
                postmarket_high_list.append(data_S.iloc[j]['high'])

            # postmarket_low_list.append(pm_low)
                # print('past market close')

            if hour < market_open_time and date == pre_market_date:
                high = data_S.loc[j]['high']
                low = data_S.iloc[j]['low']

            # premarket_high_list.append(high)
            # premarket_low_list.append(low)
                # print('before market open')

    #     premarket_df['premarket high'] = premarket_high_list
    #     premarket_df['premarket low'] = premarket_low_list

    #     postmarket_df['postmarket high'] = postmarket_high_list
    #     postmarket_df['postmarket low'] = postmarket_low_list

    #
    #     pre_market_high = max(premarket_df['premarket high'])
    #     pre_market_low = min(premarket_df['premarket low'])
    #     post_market_high = max(postmarket_df['postmarket high'])
    #     post_market_low = min(postmarket_df['postmarket low'])
    #
    #     if pre_market_high > post_market_high:
    #         non_market_hours_high = pre_market_high
    #     else:
    #         non_market_hours_high = post_market_high
    #
    #     if pre_market_low < post_market_low:
    #         non_market_hours_low = pre_market_low
    #     else:
    #         non_market_hours_low = post_market_low
    #
    #     # yikes this is going to need to be fixed
    #     non_market_hours_midpoint = (non_market_hours_high + non_market_hours_low) / 2
    #     non_market_hours_75 = (non_market_hours_midpoint+non_market_hours_high) /2
    #     non_market_hours_25 = (non_market_hours_midpoint+non_market_hours_low) /2
    #
    #     if opening_price > non_market_hours_high:
    #         non_market_hours_value = 5
    #     if ((opening_price < non_market_hours_high) and (opening_price > non_market_hours_75)):
    #         non_market_hours_value = 4
    #     if ((opening_price < non_market_hours_75) and (opening_price > non_market_hours_midpoint)):
    #         non_market_hours_value = 3
    #     if ((opening_price < non_market_hours_midpoint) and (opening_price > non_market_hours_25)):
    #         non_market_hours_value = 2
    #     if ((opening_price < non_market_hours_25) and (opening_price > non_market_hours_low)):
    #         non_market_hours_value = 1
    #     if (opening_price < non_market_hours_low):
    #         non_market_hours_value = 0
    #
    #     non_market_hours_value_list.append(non_market_hours_value)
    #
    # trade_data_df['gap percentage'] = gap_percentage_list
    # trade_data_df['opening price vs big picture'] = big_picture_range_value_list
    # trade_data_df['opening price vs 5 day range'] = five_day_range_value_list
    # trade_data_df['avg volume'] = average_volume_list
    # trade_data_df['opening price vs non market hours range'] = pd.Series(trade_data_df['opening price vs non market hours range'])
    # trade_data_df['opening price vs non market hours range'] = non_market_hours_value_list

    return  postmarket_high_list
# this is what is returned for the final version
# trade_data_df.to_csv('trade v1ariables.csv')

# opening_price = 78.49
# data_S = get_price_history('AMD', 'day',2,"minute",5)
# # print(data_S)
# market_open_time = datetime.time(6,30,00)
# market_close_time = datetime.time(13,00,00)
#
#
# premarket_df = pd.DataFrame()
# postmarket_df = pd.DataFrame()
# hour_list_pre = []
# hour_list_post = []
# premarket_high_list = []
# premarket_low_list = []
# postmarket_high_list = []
# postmarket_low_list = []
# date_list = []
# date_list_pre = []
# non_market_hours_value_list = []
# for j in range(len(data_S)-1):
#     date = data_S.iloc[j]['date']
#     good_date = date.to_pydatetime()
#     hour = good_date.time()
#     date = good_date.date()
#
#     # time_check = data_S.iloc[i]['hour']
#     # date_check = data_S.iloc[i]['short date']
#
#     pre_market_date = datetime.datetime.now()
#     pre_market_date = pre_market_date.date()
#     pre_market_date = pre_market_date - datetime.timedelta(2)
#
#     post_marekt_date = datetime.datetime.now()
#     post_marekt_date = post_marekt_date.date()
#     post_marekt_date = post_marekt_date - datetime.timedelta(3)
#     # print(previous_day)
#     # print(current_date)
#     # previous_day = previous_day.date()
#
#     if hour > market_close_time and date ==  post_marekt_date:
#         pm_high = data_S.iloc[j]['high']
#         pm_low = data_S.iloc[j]['low']
#
#         postmarket_high_list.append(pm_high)
#         postmarket_low_list.append(pm_low)
#         hour_list_post.append(hour)
#         date_list.append(date)
#
#     if hour < market_open_time and date == pre_market_date:
#         high = data_S.loc[j]['high']
#         low = data_S.iloc[j]['low']
#
#         premarket_high_list.append(high)
#         premarket_low_list.append(low)
#         hour_list_pre.append(hour)
#         date_list_pre.append(date)
#
# premarket_df['premarket high'] = premarket_high_list
# premarket_df['premarket low'] = premarket_low_list
# premarket_df['premarket hour'] = hour_list_pre
# premarket_df['hour'] = hour_list_pre
# premarket_df['date'] = date_list_pre
# postmarket_df['postmarket high'] = postmarket_high_list
# postmarket_df['postmarket low'] = postmarket_low_list
# postmarket_df['hour']= hour_list_post
# postmarket_df['date'] = date_list
#
# # premarket_df.to_csv('premarket data.csv')
# # postmarket_df.to_csv('post market.csv')
#
# pre_market_high = max(premarket_df['premarket high'])
# pre_market_low = min(premarket_df['premarket low'])
# post_market_high = max(postmarket_df['postmarket high'])
# post_market_low = min(postmarket_df['postmarket low'])
#
# if pre_market_high > post_market_high:
#     non_market_hours_high = pre_market_high
# else:
#     non_market_hours_high = post_market_high
#
# if pre_market_low < post_market_low:
#     non_market_hours_low = pre_market_low
# else:
#     non_market_hours_low = post_market_low
#
# # yikes this is going to need to be fixed
# non_market_hours_midpoint = (non_market_hours_high + non_market_hours_low) / 2
# non_market_hours_75 = (non_market_hours_midpoint+non_market_hours_high) /2
# non_market_hours_25 = (non_market_hours_midpoint+non_market_hours_low) /2
#
# if opening_price > non_market_hours_high:
#     non_market_hours_value = 5
# if ((opening_price < non_market_hours_high) and (opening_price > non_market_hours_75)):
#     non_market_hours_value = 4
# if ((opening_price < non_market_hours_75) and (opening_price > non_market_hours_midpoint)):
#     non_market_hours_value = 3
# if ((opening_price < non_market_hours_midpoint) and (opening_price > non_market_hours_25)):
#     non_market_hours_value = 2
# if ((opening_price < non_market_hours_25) and (opening_price > non_market_hours_low)):
#     non_market_hours_value = 1
# if (opening_price < non_market_hours_low):
#     non_market_hours_value = 0
#
# print(non_market_hours_value)


tradeds =  ['GME', "AAPL"]


data_G = get_price_history('GME', 'day',2,"minute",5)
data_A = get_price_history('AAPL', 'day',1,"minute",5)

# print( data_S.iloc[0]['date'])

# data_G.to_csv('GMEs.csv')
# data_A.to_csv('AaApl.csv')
find_trade_varaiables()
post_marekt_date = datetime.datetime.now()
post_marekt_date = post_marekt_date.date()
post_marekt_date = post_marekt_date - datetime.timedelta(3)
# print(post_marekt_date)
