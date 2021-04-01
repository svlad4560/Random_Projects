# I am going through to check weather I am going through it correctly because the gap percentage was fucked up and I might have been looking at one day in the future
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

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time, extened):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}&needExtendedHoursData={needExtendedHoursData}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time,needExtendedHoursData = extened)
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
stock_list = ['NIO','STKL','TSLA','TWLO','WMT','XOM']
#["BNED",'CSIQ','DBX','DFS','FSLY','GOOG','HD', 'KOPN','LEVI','MGM','NIO','STKL','TSLA','TWLO','WMT','XOM']
dataz = get_price_history("AAPL", 'year',1,"daily",1,False)
AAPl_intraday_data = get_price_history("AAPL", 'day',10,"minute",30,False)
just_close = dataz['volume']
# print(dataz.iloc[249]["open"])
# for i in stock_list:
#     data = get_price_history(i, 'year',1,"daily",1,False)
#     open = data.iloc[249]['open']
#     close = data.iloc[253]['close']
#     change = (close-open)/open
    # print(change)
# yearly_avg_volume = just_close.mean()

# print(AAPl_intraday_data,dataz,yearly_avg_volume)
es_data = get_price_history("ES", 'day',10,"minute",1,True)
es_data.to_csv('es data.csv')
print(es_data)
