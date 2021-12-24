import pandas as pd

#also how to print useing f strings
print(f"{list_of_five_day_range} this is last 5 days of data")

# this is how to get the range from a list
test_list = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    if i > 4:
        three_data_range = test_list[i-5:i]
        print(three_data_range)

# this is how to get ranges from a DataFrame
start = datetime.datetime(2019,1,1)
end = datetime.datetime.now()
df = web.DataReader("AMD",'yahoo',start,end)
for i in range(10):
    if i > 4:
        #previous 5 day range df["High"][i-5:] not Including its own
        print(df["High"][i-5:i])
        print(i)

#exception values
try :
except ValueError:

#to make your own columns with data
start = datetime.datetime(2019,1,1)
end = datetime.datetime.now()
df = web.DataReader("AMD",'yahoo',start,end)
atr_list = []
hig_open_list = []
five_day_high_average_list = [None, None,None,None,None]
for i in range(len(df)):
    high = df.iloc[i]['High']
    low = df.iloc[i]['Low']
    open = df.iloc[i]['Open']
    atr_day = high-low
    atr_list.append(atr_day)
    high_open = (high-open)/open
    hig_open_list.append(high_open)
    if i > 4:
        five_day_range = df['High'][i-5:i]
        mean_five_day = five_day_range.mean()
        five_day_high_average_list.append(mean_five_day)

df["atr"] = atr_list
df["high-open"] = hig_open_list
df['High 5 day average'] = five_day_high_average_list
