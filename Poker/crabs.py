# import random
# import pandas as pd
# import statistics
# import numpy as np
# import matplotlib.pyplot as plt
#
# list_of_random = []
#
# for i in range(0,100):
#     x = random.randint(2,12)
#     list_of_random.append(x)
#
#
#
# data_for_crabs = {"rt":list_of_random}
# crabs_random_df = pd.DataFrame(data_for_crabs)
# # crabs_random_df.to_csv("crabs.csv")
#
# good_crabs = pd.read_csv("crabs.csv")
#
# mean = good_crabs.rt.mean()
# stdev = statistics.stdev(good_crabs["rt"])
# percent_look_for = 5
# z_score = (percent_look_for - mean)/stdev
#
#
#
# print(mean,stdev)
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

    return df_of_columns


data_S = get_price_history("MRVL", 'day',1,"minute",1)
data_S.to_csv('highavg.csv')
