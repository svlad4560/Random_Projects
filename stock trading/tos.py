import requests
import json
import pprint
import matplotlib
import matplotlib.pyplot as plt
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


def gap_up_certain_up_or_down(data,percent):
    #data is data_S
    open_list = []
    close_list = []
    five_day_range_list = []
    close_lower = 0
    close_higher = 0
    above_high = 0
    range_75_to_high = 0
    range_50_to_75 = 0
    range_25_to_50 = 0
    range_low_to_25 = 0
    above_high_close = 0
    range_75_to_high_close = 0
    range_50_to_75_close = 0
    range_25_to_50_close = 0
    range_low_to_25_close = 0
    green_range = []
    red_range = []

    for num in range(len(data.index) - 1):
        open_value = data.iloc[num+1]["open"]
        close_value = data.iloc[num]["close"]
        gap_up_percent = ((open_value-close_value) / close_value)*100
        long_term_range = []

        if gap_up_percent >= percent:
            search_open = data.iloc[num+1]["open"]
            search_close = data.iloc[num+1]["close"]
            open_list.append(search_open)
            close_list.append(search_close)

            if search_open < search_close:
                close_higher += 1

            if search_open > search_close:
                close_lower += 1

            high = list(data["high"])
            low = list(data["low"])

            if num > 4:
                five_day_range_high = high[num-4:num+1]
                actual_high = max(five_day_range_high)

                five_day_range_low = low[num-4:num+1]
                actual_low = min(five_day_range_low)

                five_day_range_midpoint = (actual_high + actual_low) / 2
                five_day_range_25 = (actual_low + five_day_range_midpoint) / 2
                five_day_range_75 = (actual_high + five_day_range_midpoint) / 2

                # print(actual_high, five_day_range_high , five_day_range_midpoint)
                if search_open < search_close:
                    if search_open > actual_high:
                        above_high +=1
                    if ((search_open < actual_high) and (search_open > five_day_range_75)):
                        range_75_to_high += 1
                    if ((search_open < five_day_range_75) and (search_open > five_day_range_midpoint)):
                        range_50_to_75 += 1
                    if ((search_open < five_day_range_midpoint) and (search_open > five_day_range_25)):
                        range_25_to_50 += 1
                    if ((search_open < five_day_range_25) and (search_open > actual_low)):
                        range_low_to_25 += 1

                if search_open > search_close:
                    if search_open > actual_high:
                        above_high_close +=1
                    if ((search_open < actual_high) and (search_open > five_day_range_75)):
                        range_75_to_high_close += 1
                    if ((search_open < five_day_range_75) and (search_open > five_day_range_midpoint)):
                        range_50_to_75_close += 1
                    if ((search_open < five_day_range_midpoint) and (search_open > five_day_range_25)):
                        range_25_to_50_close += 1
                    if ((search_open < five_day_range_25) and (search_open > actual_low)):
                        range_low_to_25_close += 1


    # the next step is to compare close > open and closes <  open
    # for num in range(len(open_list)):
    #     if open_list[num] < close_list[num]:
    #         close_higher += 1
    #     if open_list[num] > close_list[num]:
    #         close_lower += 1
    length = len(open_list)
    if close_lower > close_higher:
        if above_high_close > (range_75_to_high_close and range_50_to_75_close and range_25_to_50_close and range_low_to_25_close):
            return(" Have a short Bias. When it gaps "
            + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
            + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time." +"Best chances of success when gapping up above a high")
        if range_75_to_high_close  > ( above_high_close and range_50_to_75_close and range_25_to_50_close and range_low_to_25_close):
            return(" Have a short Bias.When it gaps "
            + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
            + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time. "+ "Best chances of success when gapping up in the 75 percent range")
        if range_50_to_75_close > ( above_high_close and range_75_to_high_close and range_25_to_50_close and range_low_to_25_close):
            return(" Have a short Bias.When it gaps "
            + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
            + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time."+ "Best chances of success when gapping up in the 50 to 75 percent range")
        if  range_25_to_50_close > ( above_high_close and range_75_to_high_close and range_50_to_75_close  and range_low_to_25_close):
            return(" Have a short Bias.When it gaps "
            + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
            + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time."+ "Best chances of success when gapping up in the 25 to 50 percent range")
        if  range_low_to_25_close > ( above_high_close and range_75_to_high_close and range_50_to_75_close  and range_25_to_50_close):
            return(" Have a short Bias.When it gaps "
            + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
            + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time."+ "Best chances of success when gapping up in the low to 25 percent range")

        # return (" Have a short Bias.When it gaps "
        # + str(percent)+" it has closed lower "+ str(close_lower) + " times. Closing higher "
        # + str(close_higher)+ " times. It closes lower than it opened "+ str((close_lower/length ) *100) + " percent of the time")

    if close_higher > close_lower:
        if above_high > (range_75_to_high and range_50_to_75 and range_25_to_50 and range_low_to_25):
            return(" Have a long Bias. When it gaps "
            + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
            + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time. Best chances of success when gapping up above a high")
        if range_75_to_high  > ( above_high and range_50_to_75 and range_25_to_50 and range_low_to_25):
            return(" Have a long Bias.When it gaps "
            + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
            + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time. Best chances of success when gapping up in the 75 percent range")
        if range_50_to_75 > ( above_high and range_75_to_high and range_25_to_50 and range_low_to_25):
            return(" Have a long Bias.When it gaps "
            + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
            + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time. Best chances of success when gapping up in the 50 to 75 percent range")
        if  range_25_to_50 > ( above_high and range_75_to_high and range_50_to_75  and range_low_to_25):
            return(" Have a long Bias.When it gaps "
            + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
            + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time. Best chances of success when gapping up in the 25 to 50 percent range")
        if  range_low_to_25 > ( above_high and range_75_to_high and range_50_to_75  and range_25_to_50):
            return(" Have a long Bias.When it gaps "
            + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
            + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time. Best chances of success when gapping up in the low to 25 percent range")

        # return (" Have a long Bias.When it gaps "
        # + str(percent)+" it has closed higher "+ str(close_higher) + " times. Closing lower "
        # + str(close_lower)+ " times. It closes higher than it opened "+ str((close_higher/length ) * 100) + " percent of the time")

    else:
        return ("no Bias detected")
    # return  open_list, close_list

def spy_tick_correlation():
    tick_list_open = []
    tick_list_close = []
    spy_open_list = []
    spy_close_list = []

    count = 0
    spy_green_count = 0
    spy_red_count = 0
    tick_above_zero_count = 0

    spy_green_volume_list = []
    spy_green_range_list = []
    spy_red_volume_list = []
    spy_red_range_list = []

    tick_data = get_price_history("$TICK", 'year',1,"daily",1)
    spy_data = get_price_history("SPY", 'year',1,"daily",1)
    for value in range(len(spy_data.index) ):
        spy_datetime = spy_data.iloc[value]['datetime']
        tick_datetime = tick_data.iloc[value]['datetime']
        if spy_datetime == tick_datetime:
                tick_open_value = tick_data.iloc[value]['open']
                tick_close_value = tick_data.iloc[value]['close']

                spy_open_value = spy_data.iloc[value]['open']
                spy_close_value = spy_data.iloc[value]["close"]

                spy_green_volume_value = spy_data.iloc[value]['volume']
                spy_green_range_value = spy_data.iloc[value]['high'] - spy_data.iloc[value]['low']


                spy_red_volume_value = spy_data.iloc[value]['volume']
                spy_red_range_value = spy_data.iloc[value]['high'] - spy_data.iloc[value]['low']

                if tick_open_value > 1000:
                    # where does spy close on the day red and green
                    # what is the gap percentage?
                    tick_list_open.append(tick_open_value)
                    tick_list_close.append(tick_close_value)

                    if tick_close_value > 0:
                        tick_above_zero_count += 1

                    if spy_close_value > spy_open_value:
                        spy_green_count += 1
                        spy_green_volume_list.append(spy_green_volume_value)
                        spy_green_range_list.append(spy_green_range_value)


                    if spy_close_value < spy_open_value:
                        spy_red_count +=1
                        spy_red_volume_list.append(spy_red_volume_value)
                        spy_red_range_list.append(spy_red_range_value)
    average_spy_green_volume_days = sum(spy_green_volume_list) / len(spy_green_volume_list)
    average_spy_green_range_days = sum(spy_green_range_list) / len(spy_green_range_list)

    average_spy_red_volume_days = sum(spy_red_volume_list) / len(spy_red_volume_list)
    average_spy_red_range_days = sum(spy_red_range_list) / len(spy_red_range_list)

    test = "There is  " + str(average_spy_green_volume_days-average_spy_red_volume_days)+ " more volume on Green SPY closes rather than red SPY closes from the open"
    # now I need to get more specific. usually when there is a green day when is the low of day put in?

    return spy_green_count , spy_red_count, average_spy_green_range_days, average_spy_green_volume_days, test

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

def reformat_datatime(data):
    new_datetime_list = []
    new_data = data
    new_data = new_data.drop(columns = "datetime")
    data = data.drop(columns = ['open','high','low','close','volume'])

    for num in range(len(data.index)):
        # datetime_value = data.iloc[num]['datetime']
        datetime_value = pd.Timestamp(data.iloc[num]['datetime'], unit='ms')
        new_datetime_list.append(datetime_value)

    # so this needs to be out with and just spit out the data with out the timestamp part

    return new_data , data, new_datetime_list


data_S = get_price_history("AAPL", 'year',1,"daily",1)
# data_S.to_csv('data_S_.csv')
check_data = breakout_fiveday(data_S)
# print(data_S)
print(gap_up_certain_up_or_down(data_S, 5.00))
# print(spy_tick_correlation())
test_data  = get_price_history("AAPL","day",10,"minute", 10)
# print(reformat_datatime(data_S))
# print(pd.Timestamp(test_data.iloc[-1]['datetime'], unit='ms'))
# print(data_S)
# print(test_data)





# this checks to see the date time if greater than it means older
# open_value = data_S.iloc[open_search_value]["datetime"]
# close_value = data_S.iloc[close_search_value]["datetime"]

# if open_value > close_value:
    # print("shit")



# pd.set_option("display.max_rows", None, "display.max_columns", None)
