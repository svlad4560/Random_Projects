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

    open_list = []
    high_list = []
    low_list =[]
    close_list = []
    volume_list = []
    datetime_list = []
    updated_dates = []

    for i in content['candles']:
        open_list.append( i['open'])
        high_list.append(i['high'])
        low_list.append(i['low'])
        close_list.append(i['close'])
        volume_list.append(i['volume'])
        time = i['datetime']
        new_time = datetime.datetime.fromtimestamp(time / 1e3)
        datetime_list.append(str(new_time))

    data_dic = {'open':open_list,'high': high_list, "low": low_list, "close": close_list, "volume":volume_list, 'datetime':datetime_list}

    return data_dic

dataz = get_price_history("AAPL", 'year',1,"daily",1)

open_data = dataz['open']
for i in open_data:
    print('opening:', i)
    print('high: ', dataz[i]['high'])
    # print(i)
