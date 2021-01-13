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

def gap_up_certain_uo_or_down(data,percent):
    #data is data_S
    open_list = []
    close_list = []
    close_lower = 0
    close_higher = 0
    for num in range(len(data.index) - 1):
        open_value = data.iloc[num+1]["open"]
        close_value = data.iloc[num]["close"]
        gap_up_percent = ((open_value-close_value) / close_value)*100
        if gap_up_percent > percent:
            search_open = data.iloc[num+1]["open"]
            search_close = data.iloc[num+1]["close"]
            open_list.append(search_open)
            close_list.append(search_close)
    for num in range(len(open_list)):
        if open_list[num] < close_list[num]:
            close_higher += 1
        if open_list[num] > close_list[num]:
            close_lower += 1
    length = len(open_list)
    if close_lower > close_higher:
        return ("You should have a short biase bc of the times that it gapped up "
        + str(percent)+" it has closed lower "+ str(close_lower) + " times. While only closeing higher "
        + str(close_higher)+ " times. It gaps down "+ str((close_lower/length ) *100) + " percent")
    if close_higher > close_lower:
        return ("You should have a long biase bc of the times that it gapped up "
        + str(percent)+" it has closed higher "+ str(close_higher) + " times. While only closeing lower "
        + str(close_lower)+ " times. It gaps up "+ str((close_higher/length ) *100) + " percent")
    else:
        return ("no biase detected")
    # return close_higher, close_lower , open_list, close_list


def breakout_fiveday(price_history):
    list_of_five_day_range = []
    list_of_max_value = []

    for nums in range(len(price_history.index) - 1):
        bars = price_history.iloc[-5 + int(-nums): int(-nums)]["high"]
        list_of_five_day_range.append(bars)
        max_value = bars.max()
        list_of_max_value.append(max_value)

    # print(list_of_max_value)
    return list_of_five_day_range

data_S = get_price_history("RKT", 'year',1,"daily",1)
# data_S.to_csv('data_S.csv')
check_data = breakout_fiveday(data_S)

print(gap_up_certain_uo_or_down(data_S, 5.00))
# print(data_S)



# this is for the gap up percentage calulator
open_search_value = 9
close_search_value = 8
open_value = data_S.iloc[open_search_value]["open"]
close_value = data_S.iloc[close_search_value]["close"]
gap_up_percent = ((open_value-close_value) / close_value)*100
# print(gap_up_percent)

# this checks to see the date time if greater than it means older
open_value = data_S.iloc[open_search_value]["datetime"]
close_value = data_S.iloc[close_search_value]["datetime"]
# if open_value > close_value:
    # print("shit")



# pd.set_option("display.max_rows", None, "display.max_columns", None)
