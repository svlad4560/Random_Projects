import requests
import json
import pprint
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
        updated_dates.append(str(new_vars))
    df_of_columns['date'] = updated_dates
    df_of_columns = df_of_columns.drop(columns = ["datetime"])

    return df_of_columns

# data_S = get_price_history("XLF", 'year',1,"daily",1)
sector_etfs = ['XLF', 'XLV', 'QQQ', "XLE", "XLY" , "XLP", 'XLU', 'XLI', 'GDX']
# XLF: fincnicals
# XLV: health compare
# XLE : oil
#ICLN: clean energy
# XLY : broad consumer discretionary AMZN TSLA HD MCD NKE SBUX
# XLP: consumer staples PG WMT PEP KO COST
# XLU: Utilities (energy companies)
# XLI: INdustrials UNP UPS BA CAT
# GDX: Materials (gold)

def spy_tick_correlation():
    tick_list_open = []
    tick_list_close = []
    spy_open_list = []
    spy_close_list = []
    spy_gap_list = []
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

    tick_data = get_price_history("$TICK", 'year',1,"daily",1)
    # tick_data.to_csv("tick.csv")
    # tick_data = tick_data.read_csv('tick.csv')

    spy_data = get_price_history("SPY", 'year',1,"daily",1)
    # spy_data.to_csv("spy.csv")
    # spy_data = spy_data.read_csv('spy.csv')
    xlf_gapup_list = []
    xlv_gapup_list = []
    qqq_gapup_list = []
    xle_gapup_list = []
    xly_gapup_list = []

    spy_close_percentage_list = []
    xlf_close_percentage_list = []
    xlv_close_percentage_list = []
    qqq_close_percentage_list = []
    xle_close_percentage_list = []
    xly_close_percentage_list = []

    xlf_data = get_price_history("XLF", 'year',1,"daily",1)
    # xlf_data.to_csv("xlf.csv")
    # xlf_data = xlf_data.read_csv('xlf.csv')

    xlv_data = get_price_history("XLV", 'year',1,"daily",1)
    # xlv_data.to_csv("xlv.csv")
    # xlv_data = xlv_data.read_csv('xlv.csv')

    qqq_data = get_price_history("QQQ", 'year',1,"daily",1)
    # qqq_data.to_csv("qqq.csv")
    # qqq_data = qqq_data.read_csv('qqq.csv')

    xle_data = get_price_history("XLE", 'year',1,"daily",1)
    # xle_data.to_csv("xle.csv")
    # xle_data = xle_data.read_csv('xle.csv')

    xly_data = get_price_history("XLY", 'year',1,"daily",1)
    # xly_data.to_csv("xly.csv")
    # xly_data = xly_data.read_csv('xly.csv')


    for value in range(len(spy_data)-1):

        if value > 0 :
            tick_open_value = tick_data.iloc[value]['open']
            tick_close_value = tick_data.iloc[value]['close']

            spy_open_value = spy_data.iloc[value]['open']
            spy_close_value = spy_data.iloc[value]["close"]

            spy_open_value_for_gap = spy_data.iloc[value]['open']
            spy_close_value_for_gap = spy_data.iloc[value-1]["close"]

            gap_up_percent = ((spy_open_value_for_gap-spy_close_value_for_gap) / spy_close_value_for_gap)*100

            # print(spy_open_value,spy_close_value, gap_up_percent )

            if  tick_open_value > 1000:

                if value >4:
                    five_day_range = [-5:i]
                tick_list_open.append(tick_open_value)

                spy_open_value_for_close_percentage= spy_data.iloc[value]['open']
                spy_close_value_for_close_percentage = spy_data.loc[value]["close"]
                spy_close_percentage = ((spy_close_value_for_close_percentage-spy_open_value_for_close_percentage) / spy_open_value_for_close_percentage)*100


                xlf_open_value_for_gap = xlf_data.loc[value]['open']
                xlf_close_value = xlf_data.loc[value]['close']
                xlf_close_value_for_gap = xlf_data.iloc[value-1]["close"]
                xlf_close_percentage = ((xlf_close_value-xlf_open_value_for_gap)/xlf_open_value_for_gap) *100
                xlf_gap_up_percent = ((xlf_open_value_for_gap-xlf_close_value_for_gap) / xlf_close_value_for_gap)*100

                xlv_open_value_for_gap = xlv_data.iloc[value]['open']
                xlv_close_value = xlv_data.iloc[value]['close']
                xlv_close_value_for_gap = xlv_data.loc[value-1]["close"]
                xlv_close_percentage = ((xlv_close_value-xlv_open_value_for_gap)/xlv_open_value_for_gap) *100
                xlv_gap_up_percent = ((xlv_open_value_for_gap-xlv_close_value_for_gap) / xlv_close_value_for_gap)*100

                qqq_open_value_for_gap = qqq_data.iloc[value]['open']
                qqq_close_value = qqq_data.iloc[value]['close']
                qqq_close_value_for_gap = qqq_data.loc[value-1]["close"]
                qqq_close_percentage = ((qqq_close_value-qqq_open_value_for_gap)/qqq_open_value_for_gap) *100
                qqq_gap_up_percent = ((qqq_open_value_for_gap-qqq_close_value_for_gap) / qqq_close_value_for_gap)*100

                xle_open_value_for_gap = xle_data.iloc[value]['open']
                xle_close_value = xle_data.iloc[value]['close']
                xle_close_value_for_gap = xle_data.iloc[value-1]["close"]
                xle_close_percentage = ((xle_close_value-xle_open_value_for_gap)/xle_open_value_for_gap) * 100
                xle_gap_up_percent = ((xle_open_value_for_gap-xle_close_value_for_gap) / xle_close_value_for_gap)*100

                xly_open_value_for_gap = xly_data.iloc[value]['open']
                xly_close_value = xly_data.iloc[value]['close']
                xly_close_value_for_gap = xly_data.loc[value-1]["close"]
                xly_close_percentage = ((xly_close_value-xly_open_value_for_gap)/xly_open_value_for_gap) *100
                xly_gap_up_percent = ((xly_open_value_for_gap-xly_close_value_for_gap) / xly_close_value_for_gap)*100

                day = []
                day.append(xlf_gap_up_percent)
                day.append(xlv_gap_up_percent)
                day.append(qqq_gap_up_percent)
                day.append(xle_gap_up_percent)
                day.append(xly_gap_up_percent)
                sector_gap_up_list.append(day)

                spy_gap_list.append(gap_up_percent)
                xlf_gapup_list.append(xlf_gap_up_percent)
                xlv_gapup_list.append(xlv_gap_up_percent)
                qqq_gapup_list.append(qqq_gap_up_percent)
                xle_gapup_list.append(xle_gap_up_percent)
                xly_gapup_list.append(xly_gap_up_percent)

                spy_close_percentage_list.append(spy_close_percentage)
                xlf_close_percentage_list.append(xlf_close_percentage)
                xlv_close_percentage_list.append(xlv_close_percentage)
                qqq_close_percentage_list.append(qqq_close_percentage)
                xle_close_percentage_list.append(xle_close_percentage)
                xly_close_percentage_list.append(xly_close_percentage)







    # for value in sector_gap_up_list:
    #     for num in value:
    #         print(num)
    new_data_for_df = {'SPY Gap Up':spy_gap_list,"TICK open": tick_list_open,"XLF Gap Up": xlf_gapup_list, "XLV Gap Up": xlv_gapup_list,"QQQ gap up":  qqq_gapup_list, "XLE Gap Up":xle_gapup_list, "XLY Gap Up": xly_gapup_list}
    new_data = pd.DataFrame(new_data_for_df)
    new_data['SPY Close Percentage'] = spy_close_percentage_list
    new_data['XLF Close percentage'] = xlf_close_percentage_list
    new_data['XLV Close percentage'] = xlv_close_percentage_list
    new_data['QQQ Close percentage'] = qqq_close_percentage_list
    new_data['XLE Close percentage'] = xle_close_percentage_list
    new_data['XLY Close percentage'] = xly_close_percentage_list










    return new_data
#
# length = len(spy_tick_correlation())
# test = length%2

excel_data = spy_tick_correlation()
excel_data.to_csv("sector data.csv")

print(spy_tick_correlation())
# what are some other variables that I want to check for.
    variables_to_check = [tick_open,spy_gap_percent,spy_percentage,distance_from_5day_ema,and_the_distance_from_50, SPY_volume, sector_volume, where_is_spy_and_sector_on_daily, ]
    what_to_maximize = [close_distance_from_open, as_well_what_sector performance the best when gapping up]
