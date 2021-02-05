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
        updated_dates.append(str(new_vars))
    df_of_columns['date'] = updated_dates
    df_of_columns = df_of_columns.drop(columns = ["datetime"])

    return df_of_columns

dataz = get_price_history("AAPL", 'year',1,"daily",1)
# print(dataz)

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

        if num > 0 :
            open_value = data.iloc[num]["open"]
            close_value = data.iloc[num-1]["close"]
            gap_up_percent = ((open_value-close_value) / close_value)*100


            if gap_up_percent >= percent:
                search_open = data.iloc[num]["open"]
                search_close = data.iloc[num]["close"]
                open_list.append(search_open)
                close_list.append(search_close)

                if search_open < search_close:
                    close_higher += 1

                if search_open > search_close:
                    close_lower += 1

                high = list(data["high"])
                low = list(data["low"])

                if num > 4:
                    five_day_range_high = high[num-5:num]
                    actual_high = max(five_day_range_high)


                    five_day_range_low = low[num-5:num]
                    actual_low = min(five_day_range_low)

                    five_day_range_midpoint = (actual_high + actual_low) / 2
                    five_day_range_25 = (actual_low + five_day_range_midpoint) / 2
                    five_day_range_75 = (actual_high + five_day_range_midpoint) / 2

                    # this checks if we closed higher than we open
                    if search_open < search_close :
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


    else:
        return ("no Bias detected")


print(gap_up_certain_up_or_down(dataz, 2.00))
