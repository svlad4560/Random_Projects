import requests
import json
import datetime
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
import statistics
from scipy import stats

percent_look_for = 0.05
input_high_open_perent = 0.06

start = datetime.datetime(2019,1,1)

end = datetime.datetime.now()
# df = web.DataReader("BABA",'yahoo',start,end)



def find_prob_for_over(percent_look_for,input_high_open_perent,symbol):

    start = datetime.datetime(2019,1,1)

    end = datetime.datetime.now()
    df = web.DataReader(symbol,'yahoo',start,end)

    atr_list = []

    data_list = []
    differences = []

    for i in range(len(df)):
        atr = df.iloc[i]['High'] - df.iloc[i]['Low']
        atr_list.append(atr)


    atr = sum(atr_list)/len(atr_list)
    avg_vol = df['Volume'].mean()


    for i in range(len(df)):
        high = df.iloc[i]['High']
        low = df.iloc[i]['Low']
        # print(i)
        open = df.iloc[i]['Open']
        # print(i)
        high_open = (high-open)/open
        atr_day = high-low
        five_day_range = df['High'][-5:]


        if high_open > input_high_open_perent and df.iloc[i]["Volume"] > avg_vol and atr_day > atr:

            good_high = df.iloc[i]["Close"]
            good_low = df.iloc[i]["Open"]
            difference = (good_high - good_low)/good_low
            differences.append(difference)

    datas = {'difference':differences}
    filtered_high = pd.DataFrame(datas)
    # print(filtered_high['difference'][-5:])


    average_norm = filtered_high['difference'].mean()
    stdev_norm = statistics.stdev(filtered_high['difference'])
    z_score = (percent_look_for - average_norm)/stdev_norm
    probability = 1 - stats.norm.cdf(z_score)
    return probability

print(find_prob_for_over(0.06,0.08,"BABA"))

def find_prob_for_under(percent_look_for,input_high_open_perent,symbol):

    start = datetime.datetime(2019,1,1)

    end = datetime.datetime.now()
    df = web.DataReader(symbol,'yahoo',start,end)

    atr_list = []

    data_list = []
    differences = []

    for i in range(len(df)):
        atr = df.iloc[i]['High'] - df.iloc[i]['Low']
        atr_list.append(atr)


    atr = sum(atr_list)/len(atr_list)
    avg_vol = df['Volume'].mean()


    for i in range(len(df)):
        high = df.iloc[i]['High']
        low = df.iloc[i]['Low']
        # print(i)
        open = df.iloc[i]['Open']
        # print(i)
        high_open = (high-open)/open
        atr_day = high-low


        if high_open > input_high_open_perent and df.iloc[i]["Volume"] > avg_vol and atr_day > atr:

            good_high = df.iloc[i]["Close"]
            good_low = df.iloc[i]["Open"]
            difference = (good_high - good_low)/good_low
            differences.append(difference)

    datas = {'difference':differences}
    filtered_high = pd.DataFrame(datas)


    average_norm = filtered_high['difference'].mean()
    stdev_norm = statistics.stdev(filtered_high['difference'])
    z_score = (percent_look_for - average_norm)/stdev_norm
    probability = stats.norm.cdf(z_score)
    return probability

# print(find_prob_for_under(0.03,0.09,"TSLA"))
