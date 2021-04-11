import requests
import json
import pandas as pd
import datetime
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

def get_price_history_tick(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
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

SPY_data = get_price_history("SPY",'year',1,"daily",1)
TICK_data = get_price_history("$TICK",'year',1,"daily",1)

tick_open = []
spy_close_dollar_list = []
spy_next_day_gap_dollars_list = []
open_minus_low = []
spy_gap_percetange= []

for i in range(len(SPY_data)):
    if i > 0:
        spy_gap_percet = ((SPY_data.iloc[i]['open'] - SPY_data.iloc[i-1]['close'])/SPY_data.iloc[i-1]['close']) *100

        if TICK_data.iloc[i]['open'] > 999 and spy_gap_percet > 1:
            spy_gap_percetange.append(spy_gap_percet)
            tick_open.append(TICK_data.iloc[i]['open'])

            spy_close_dollars = SPY_data.iloc[i]['close'] - SPY_data.iloc[i]['open']
            spy_close_dollar_list.append(spy_close_dollars)

            next_day_gap_dollars = SPY_data.iloc[i+1]['open'] - SPY_data.iloc[i]['close']
            spy_next_day_gap_dollars_list.append(next_day_gap_dollars)


# print(SPY_data)
stats_df = pd.DataFrame()
# TICK_data.to_csv('TICk Data.csv')
stats_df['Tick_Open'] = tick_open
stats_df['SPY Close Dollar'] = spy_close_dollar_list
stats_df['Gap Difference Dollars'] = spy_next_day_gap_dollars_list
stats_df['SPY gap percent'] = spy_gap_percetange
stats_df.to_csv('SPY vs Tick.csv')
# print(stats_df.corr())
# print(stats_df.Tick_Open)
# print(TICK_data)
# print(TICK_data)
# print(tick_open)
