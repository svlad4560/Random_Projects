import datetime
import requests
import json
import pandas as pd
import pprint

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time)
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



#
data_S = get_price_history("AAPL","day",10,"minute", 10)

def spy_tick_correlation():
    tick_list_open = []
    tick_list_close = []
    spy_open_list = []
    spy_close_list = []
    xlf_list_open = []
    xlf_list_close = []
    qqq_open_list = []
    qqq_close_list = []
    xle_list_open = []
    xle_list_close = []
    xly_open_list = []
    xly_close_list = []
    sector_gap_up_list = []
    count = 0
    spy_green_count = 0
    spy_red_count = 0
    tick_above_zero_count = 0
    spy_green_volume_list = []
    spy_green_range_list = []
    spy_red_volume_list = []
    spy_red_range_list = []
    tick_data = get_price_history("$TICK", 'year', 1, "daily", 1)
    spy_data = get_price_history("SPY", 'year', 1, "daily", 1)
    xlf_data = get_price_history("XLF", 'year', 1, "daily", 1)
    xlv_data = get_price_history("XLV", 'year', 1, "daily", 1)
    qqq_data = get_price_history("QQQ", 'year', 1, "daily", 1)
    xle_data = get_price_history("XLE", 'year', 1, "daily", 1)
    xly_data = get_price_history("XLY", 'year', 1, "daily", 1)
    for value in range(len(spy_data)-1):
        if value > 0:
            tick_open_value = tick_data.iloc[value]['open']
            tick_close_value = tick_data.iloc[value]['close']
            spy_open_value = spy_data.iloc[value]['open']
            spy_close_value = spy_data.iloc[value]["close"]
            spy_open_value_for_gap = spy_data.loc[value + 1]['open']
            spy_close_value_for_gap = spy_data.iloc[value]["close"]
            gap_up_percent = (
                (spy_open_value_for_gap-spy_close_value_for_gap) / spy_close_value_for_gap)*100
            if tick_open_value > 1000 and gap_up_percent > 1.50:
                spy_open_list.append(spy_open_value_for_gap)
                spy_close_list.append(spy_close_value_for_gap)
                xlf_open_value_for_gap = xlf_data.loc[value+1]['open']
                xlf_close_value_for_gap = xlf_data.iloc[value]["close"]
                xlf_gap_up_percent = (
                    (xlf_open_value_for_gap-xlf_close_value_for_gap) / xlf_close_value_for_gap)*100
                xlv_open_value_for_gap = xlv_data.loc[value+1]['open']
                xlv_close_value_for_gap = xlv_data.iloc[value]["close"]
                xlv_gap_up_percent = (
                    (xlv_open_value_for_gap-xlv_close_value_for_gap) / xlv_close_value_for_gap)*100
                qqq_open_value_for_gap = qqq_data.loc[value+1]['open']
                qqq_close_value_for_gap = qqq_data.iloc[value]["close"]
                qqq_gap_up_percent = (
                    (qqq_open_value_for_gap-qqq_close_value_for_gap) / qqq_close_value_for_gap)*100
                xle_open_value_for_gap = xle_data.loc[value+1]['open']
                xle_close_value_for_gap = xle_data.iloc[value]["close"]
                xle_gap_up_percent = (
                    (xle_open_value_for_gap-xle_close_value_for_gap) / xle_close_value_for_gap)*100
                xly_open_value_for_gap = xly_data.loc[value+1]['open']
                xly_close_value_for_gap = xly_data.iloc[value]["close"]
                xly_gap_up_percent = (
                    (xly_open_value_for_gap-xly_close_value_for_gap) / xly_close_value_for_gap)*100
                day_list = []
                day_list.append(xlf_gap_up_percent)
                day_list.append(xlv_gap_up_percent)
                day_list.append(qqq_gap_up_percent)
                day_list.append(xle_gap_up_percent)
                day_list.append(xly_gap_up_percent)
                sector_gap_up_list.append(day_list)
    return day_list

# print(new_var)
# print(updated_dates)
print(spy_tick_correlation())
