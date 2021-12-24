# import pandas as pd
# from alpha_vantage.timeseries import TimeSeries
# import time
#
#
# api_key = "KEWO0ZYQITEE4LRT"
#
# ts = TimeSeries(key = api_key, output_format = 'pandas')
# data, meta_data = ts.get_intraday(symbol = "AAPL", interval = '1min', outputsize = 'full')
# # data.to_csv('new_api_data.csv')
# df = pd.DataFrame(data = data, columns = list('ohlcv'))
# print(df)
import requests
import json
import pprint
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import smtplib
from email.message import EmailMessage
import datetime
import time



ticker_df = pd.read_csv('ticker.csv')

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
        updated_dates.append((new_vars))
    df_of_columns['date'] = updated_dates
    df_of_columns = df_of_columns.drop(columns = ["datetime"])

    return df_of_columns


data = get_price_history("AMD", 'day',10,"minute",1)

# datess = data.iloc[0]['date']
#
# datess = datess.to_pydatetime()
# time1 = datess.time()
#
# datesss = data.iloc[1]['date']
# datesss = datesss.to_pydatetime()
# time2 = datesss.time()
# if time1 < time2:
#     print('it shoud')
# time_change =  datetime.timedelta(minutes = 5)
#
# da = datess + time_change
#
# print(da.time())
#
precent_change = data.close.pct_change()
data['pc']= precent_change
data['pc']= data.pc.round(decimals = 5)
# to make execute less do not shift
data['xx'] = data['low'].rolling(5).mean()
data['avg_low5'] = data['xx'].shift()

atr_list = []
for i in range(len(data)):
    atr = data.iloc[i]["high"]- data.iloc[i]["low"]
    #I can add some atr coulmn to compare later
    atr_list.append(atr)


avg_atr = sum(atr_list)/len(atr_list)
avg_volume = data.volume.mean()

filter_list = []
five_later_list = []

capital = 1000
for i in range(len(data)):
    if data.iloc[i]['close'] < data.iloc[i]['avg_low5']:

        price_5_later = data.iloc[i+5]["close"]
        filter_list.append(1)
        five_later_list.append(price_5_later)

    else:
        filter_list.append(0)
        five_later_list.append(0)

data['filtere_data'] = filter_list
data['difference'] = data['filtere_data'].diff()

sharesa = []
buy_price_list = []
shares_bought = []
shares_sold_list = []
sell_price_list = []
in_a_poisition = 0
test_a = []
trade_df_coulmn_list = []
# so I want to try a backtest with a stop of just breaks it and then I want to have on that is time and volume based to sell
# I also want to do a high avg minues close coulmn
data['five_later'] = five_later_list

for i in range(len(data)-1):
    if i <= 3893:
        share_price = data.iloc[i]['close']
        shares = capital/share_price
        print(f"{i}index")
        print(f"{in_a_poisition} IN A POSITION")
        filtered = data.iloc[i]["filtere_data"]
        print(f"{filtered}filtered")
        # print(f"{in_a_poisition} in a position count")
        # print(f"{filtered} filtered count")
        # print(f"{i} index     ")
        if in_a_poisition == 0 and filtered == 1:
            #This is when we buy bc close is less than the avg 5
            avg_buy_price =  data.iloc[i]['close']
            shares = capital/share_price
            in_a_poisition = 1
            index_value_bought = i
            index_value_to_sell = i + 5
            trade_df_coulmn_list.append(avg_buy_price)


        position_of_5_later_prev = data.iloc[i-5]['five_later']

        if in_a_poisition == 1 and share_price == position_of_5_later_prev:
            in_a_poisition = 0
            avg_sell_price = data.iloc[i]['close']
            trade_df_coulmn_list.append(avg_sell_price)
        else:
            trade_df_coulmn_list.append(0)




# data['shares bought'] = shares_bought
print(len(trade_df_coulmn_list))
data['trades'] = trade_df_coulmn_list
data.to_csv('ttt.csv')

print((data))
# # I dont know what I want to accomplish I want to make a backtest but I dont know how to come up with it
#
#
#
#
#
#
#
