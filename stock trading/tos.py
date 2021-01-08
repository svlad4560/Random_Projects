import requests
import json
import pprint
import pandas as pd

starting_balance = 100000
step = 0
def get_right_extensions():
    right_list = []
    for symbol in symbol_list_none['ticker']:
        if "." not in symbol:
            right_list.append(symbol)
    return right_list

symbol_list_none = pd.read_csv ('symbol_list.csv')
symbol_list = get_right_extensions()

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'
stock = "AAPL"

def get_fundamentals(stocks):
    base_url_fund = 'https://api.tdameritrade.com/v1/instruments?&symbol={stock_ticker}&projection={projection}'
    endpoint_fund = base_url_fund.format(stock_ticker = stocks, projection = 'fundamental')
    page = requests.get(url=endpoint_fund, params={'apikey' : td_consumer_key})
    fundamental_data = json.loads(page.content)
    return fundamental_data

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time)
    # endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
    page = requests.get(url=full_url_price_history, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    data = pd.DataFrame(data=content)
    df_of_columns = data["candles"].apply(pd.Series)
    return df_of_columns
data_S = get_price_history("BA", 'year',1,"daily",1)

def get_options_data():
    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}\&contractType={contract_type}&strike={strike}&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = 'AAL', contract_type = 'PUT', strike = 9, date='2020-06-19')
    page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    return content

def get_marketCap(stocks):
    fund = get_fundamentals(stocks)
    first_key = fund[stocks]
    second_key = first_key['fundamental']
    return second_key['marketCap']

def get_smallCap():
    global small_cap_list
    small_cap_list = []
    for stock in symbol_list:
        market_cap = get_marketCap(stock)
        if market_cap < 10:
            small_cap_list.append(stock)
    return small_cap_list

def count_gap_ups(data):
    # data is the get_price_history
    gap_up_count = 0
    for num in range(len(data.index) - 1):
        open_value = data.iloc[num+1]["open"]
        close_value = data.iloc[num]["close"]
        if open_value > close_value:
            gap_up_count += 1
    return gap_up_count

# print(data_S[:10])

# print(data_S.index)

def breakout_fiveday(price_history):

    for nums in range(len(price_history.index) - 1):
        list_of_five_day_range = []
        #so then it starts with the first list being the most recent and then [X,Y,Z] Z is the most recent
        list_of_max_value = []
        bars = price_history.iloc[-5 + int(-nums): int(-nums)]["high"]
        list_of_five_day_range.append(bars)
        max_value = bars.max()
        list_of_max_value.append(max_value)
        # print( str(bars)+ " this is the veyr first list of range ")


    return list_of_five_day_range, list_of_max_value

check_data = pd.DataFrame(data = breakout_fiveday(data_S))
# check_data.to_csv("5 day range.csv")
pprint.pprint(breakout_fiveday(data_S))


data_S = get_price_history("BA", 'year',1,"daily",1)

# this is for the gap up percentage calulator
open_search_value = 9
close_search_value = 8
open_value = data_S.iloc[open_search_value]["open"]
close_value = data_S.iloc[close_search_value]["close"]
gap_up_percent = ((open_value-close_value) / close_value)*100

# this checks to see the date time if greater than it means older
open_value = data_S.iloc[open_search_value]["datetime"]
close_value = data_S.iloc[close_search_value]["datetime"]
# if open_value > close_value:
    # print("the bottom day is greater than the top date")


# print(gap_up_percent)


pd.set_option("display.max_rows", None, "display.max_columns", None)
# data_S = data_S.drop(columns=["high", "low"])
print(data_S)

# print(str(count_gap_ups(data_S))+ " gap up count")
# print(str(len(data_S))+ " length of data frame")
# print(data_S.tail())

# for nums in range(1):
#     list_of_five_day_range = []
#     #so then it starts with the first list being the most recent and then [X,Y,Z] Z is the most recent
#     list_of_max_value = []
#     bars = data_S.iloc[-5 + int(-nums): int(-nums)]["high"]
#     list_of_five_day_range.append(bars)
#     max_value = bars.max()
#     list_of_max_value.append(max_value)
    # print( str(bars)+ " this is the veyr first list of range ")

# for numbers in range(len(datas.index) - 2):
list_of_five_day_range = []
#so then it starts with the first list being the most recent and then [X,Y,Z] Z is the most recent
list_of_max_value = []
bars = data_S.iloc[-5:]['high']
list_of_five_day_range.append(list(bars))
max_value = bars.max()
list_of_max_value.append(max_value)


bars1 = data_S.iloc[-6:-1]['high']
list_of_five_day_range.append(list(bars1))
max_value1 = bars1.max()
list_of_max_value.append(max_value1)

max_id = bars.max()

# [X,Y,Z] Z is the most recent with the list at [0] is the most recent data
# print(str(list_of_five_day_range) + " this is last 5 days of data")

# with the first number in the list is for the most recent first day high.
# print(str(list_of_max_value)+" this is maxium number in last 5 days")

for stat in data_S["high"]:
    val = -5
    control = int(stat)
    list_of_bars = []
    list_of_max = []
    value = True
    if value == True:
        bars = data_S.iloc[control + val:-5]['open']
    value = False
    bars = data_S.iloc[ control + val:-5]['open']
    list_of_bars = bars.append(data_S.iloc[control + val:-5 - control]['open'])
    max_id = bars.max()
    list_of_max.append(max_id)
    # print (max_id)



# for num in range(len(data.index) - 1):
#     bars = data_S["open"][-5]
#     is_new_high = False
#     if len(bars.high) == 5:
#         is_new_high = (bars.high[-1] > max(bars.high[:-1]))
