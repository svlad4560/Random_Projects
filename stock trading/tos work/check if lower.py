import requests
import json
import datetime
import pandas as pd
import pandas_datareader.data as web
import math

# So one of the things that I can do is have it either by percent or by ATRS
# Have it for any symbols and as many years as you want to go back.
symbol = 'TSLA'

start = datetime.datetime(2020,1,1)

end = datetime.datetime.now()
df = web.DataReader(symbol,'yahoo',start,end)

percent_look_for = 0.0996
close_under_open_list = []
close_above_under_list = []
times_above_percent = 0
close_above_open_count = 0
close_below_open_count =  0
time_aboce_midpoint = 0
close_above_midpoint_list = []
time_below_midpoint = 0
close_below_midpoint_list = []
time_it_occers_count = 0
Volume_list_less_than_open = []
volume_list_midpoint = []


for i in range(len(df)):

    open = df.iloc[i]["Open"]
    high = df.iloc[i]["High"]
    volume = df.iloc[i]["Volume"]

    percent_difference = (high/open) -1
    midpoint = ((df.iloc[i]["High"] + df.iloc[i]["Open"]) / 2)

    if percent_difference > percent_look_for:

        time_it_occers_count = time_it_occers_count + 1

        if df.iloc[i]['Close'] < df.iloc[i]['Open']:
            close_below_open_count = close_below_open_count + 1
            close_under_open_list.append(percent_difference)
            Volume_list_less_than_open.append(volume)

        if df.iloc[i]['Close'] >  df.iloc[i]['Open']:
            close_above_open_count = close_above_open_count +1
            close_above_under_list.append(percent_difference)

        if df.iloc[i]["Close"] > midpoint:
            time_aboce_midpoint = time_aboce_midpoint  + 1
            close_above_midpoint_list.append(percent_difference)

        if df.iloc[i]["Close"] < midpoint:
            time_below_midpoint = time_below_midpoint  + 1
            close_below_midpoint_list.append(percent_difference)
            volume_list_midpoint.append(volume)

new_df = pd.DataFrame()
new_df['volume midpoint'] = volume_list_midpoint
# new_df["volume open"] = Volume_list_less_than_open
new_df["percent midpoint high"] = close_below_midpoint_list
# new_df["percent open high"] = close_under_open_list

new_df.to_csv("data for close.csv")



percent_it_closes_below_midpoint = round((time_below_midpoint/time_it_occers_count)*100,2)
percent_it_closes_below_open = round((close_below_open_count/time_it_occers_count)*100,2)

print("this percent high or atrs " + str(percent_look_for*100)+"  has been put in "+str(time_it_occers_count)+" times")
print("on average it closes below high open midpoint "+ str(percent_it_closes_below_midpoint)+ "%")
print ("on average it closes below opening price "+ str(percent_it_closes_below_open)+ "%")
