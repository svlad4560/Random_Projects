import requests
import json
import datetime
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
import statistics
from scipy import stats
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'
# this is how to get ranges from a DataFrame
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


df = get_price_history("DKNG", 'day',1,"minute",1)
print(len(df))



# print(data)
avg_high = [None, None,None,None,None]
atr_list = []
hig_open_list = []
five_day_high_average_list = [None, None,None,None,None]
low_5day_range_list = [None, None,None,None,None]
for i in range(len(df)):
    high = df.iloc[i]['high']
    low = df.iloc[i]['low']
    open = df.iloc[i]['open']
    close = df.iloc[i]['close']

    atr_list.append(df.iloc[i]['high']-df.iloc[i]['low'])
    high_open = close-open
    hig_open_list.append(high_open)
    if i > 4:
        five_day_range = df['high'][i-5:i]
        low_range = df['low'][i-5:i]
        mean_low = low_range.mean()
        low_5day_range_list.append(mean_low)
        # print(five_day_range)
        mean_five_day = five_day_range.mean()
        five_day_high_average_list.append(mean_five_day)


df["atr"] = atr_list
df["highopen"] = hig_open_list
df['High 5 day average'] = five_day_high_average_list
df['Low 5 range'] = low_5day_range_list

avg_atr = df.atr.mean()
avg_volume = df.volume.mean()
avg_bar = df.highopen.mean()

bar_greater_list = [None,None,None,None,None]
close_less_than_average_list = [None,None,None,None,None]
for i in range(len(df)):
    if i > 4:
        high = df.iloc[i]['high']
        low = df.iloc[i]['low']
        open = df.iloc[i]['open']
        close = df.iloc[i]['close']
        if (high-low) > avg_atr and df.iloc[i]["volume"] > avg_volume and (high-close) > avg_bar:
            bar_greater_list.append(1)

        else:
            bar_greater_list.append(0)

        if close <= df.iloc[i]['Low 5 range']:
            close_less_than_average_list.append(1)
        else:
            close_less_than_average_list.append(0)

df['bar more than average'] = bar_greater_list
df['close less than low average'] =close_less_than_average_list


price_5_later_list = [None,None,None,None,None]
return_after_5_list = [None,None,None,None,None]
for i in range(len(df)):
    if i > 4:
        if df.iloc[i]['close less than low average'] == 1:
            print(i)


            close_price_5_min_later = df.loc[i+5]['close']
            return_5_min = close_price_5_min_later-df.iloc[i]["close"]
            return_after_5_list.append(return_5_min)
            price_5_later_list.append(close_price_5_min_later)
        else:
            price_5_later_list.append(0)
            return_after_5_list.append(0)
    # if i > 6-len(df):
    #     price_5_later_list.append(None)
    #     return_after_5_list.append(None)
print(len(price_5_later_list), len(return_after_5_list))
df['Price 5 min later'] = price_5_later_list
df['return 5 min after'] = return_after_5_list


# x = df.drop(columns= ['date', 'open','high','low','close','volume','atr'])
# print(x)
df.to_csv('Seesif1min.csv')
# print(df.plot(x = 'Low', y = 'High 5 day average', kind = 'line'))
