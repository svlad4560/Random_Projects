import pandas as pd
import math
import datetime
import pandas_datareader.data as web



start = datetime.datetime(2015,1,1)

end = datetime.datetime.now()
df = web.DataReader("TSLA",'yahoo',start,end)
percent_list =[]
atr_list = []
gap_percent_list = [None]
open = list(df.Open)
gapp_five_list =[None,None,None,None,None,None]
print(len(df))
# print(df.iloc[])



for i in range(len(df)):
    open = df.iloc[i]["Open"]
    close = df.iloc[i]["Close"]
    percent = ((close-open)/open ) *100
    percent_list.append(percent)

    high = df.iloc[i]["High"]
    low = df.iloc[i]["Low"]
    atr = high - low
    atr_list.append(atr)


    if i > 0:
        gap_percent = ((df.iloc[i]["Open"]- df.iloc[i-1]["Close"]) / df.iloc[i-1]["Close"]) * 100
        gap_percent_list.append(gap_percent)


        # this correctly looks to see if today it is gapping over 5 day range
    if i > 5 and i < len(df):
        five_range = df.iloc[i-6:i-1]['High']
        current_position = df.iloc[i-1]["Open"]


        if current_position > five_range.max():

            gapp_five_list.append(1)
        else:

            gapp_five_list.append(0)







# gapp_five_list.append(None)





df['Percent_Close'] = percent_list
df['atr'] = atr_list
df['gapP'] = gap_percent_list
df['gapp_five'] = gapp_five_list

atr_avg_list, volume_average_list = [],[]

avg_atr = df.atr.mean()
avg_volume = df.Volume.mean()

for i in range(len(df)):
    if df.iloc[i]['atr'] > avg_atr:
        atr_avg_list.append(1)
    else:
        atr_avg_list.append(0)

    if df.iloc[i]['Volume'] > avg_volume:
        volume_average_list.append(1)
    else:
        volume_average_list.append(0)

df['atr greater'] = atr_avg_list
df['volume greqater'] = volume_average_list

print(df.head())
df.to_csv('test12345.csv')

df.shift(periods=3, fill_value=0)
