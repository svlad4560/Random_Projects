import requests
import json
import datetime

import pandas as pd
import pandas_datareader.data as web


large_df = pd.read_csv('large.csv')

good_tickers = []
bad_tickers = []

ticker_list = list(large_df['Ticker'])

# df_test = pd.DataFrame(data = ticker_list)
# print(df_test)

for i in range(len(ticker_list)):
    stock = ticker_list[i]
    start = datetime.datetime(2013,1,1)
    end = datetime.datetime.now()
    stock = str(stock)

    stock_info = web.DataReader(stock, 'yahoo', start, end)
    length_need = 2207

    length_of_df = len(stock_info)

    if length_of_df >= 2207:
        good_tickers.append(stock)

    else:
        bad_tickers.append(stock)



print(good_tickers)

# print(bad_tickers)

# so the length of we need to be greater than is 2207

# print(type(first))

# print(stock_info)
# print(large_df)
