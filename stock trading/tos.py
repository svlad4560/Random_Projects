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

def get_price_history(stocks):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
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


data_S = get_price_history("AAPL")
pd.set_option("display.max_rows", None, "display.max_columns", None)
data_S = data_S.drop(columns=["high", "low"])
print(data_S[:10])
# print(data_S)
# so then the last row is the values for yesterdays trading day
def count_gap_ups(data):
    # data is the get_price_history
    # data['open'].iloc[-254]
    open_search_value = 1
    close_search_value = 0
    gap_up_count = 0
    range_count =len(data_S)

    for num in range(10):
        open_value = data_S.iloc[open_search_value]["open"]
        close_value = data_S.iloc[close_search_value]["close"]
        if open_value > close_value:
            gap_up_count += 1
            open_value += 1
            close_search_value += 1

        print(num)

    return gap_up_count

print(str(count_gap_ups(data_S))+ " gap up count")
print(str(len(data_S))+ " length of data frame")
list_open = list(data_S["open"])

print(list_open[0])



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
