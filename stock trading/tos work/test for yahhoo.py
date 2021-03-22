import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import itertools
traded = ['GME','AAPL']
# for i, j in itertools.product(traded, range(10)):
#     print('stock traded ' + i)
#     print(' index position ' + str(j))



end = datetime.datetime.now()
start = end-datetime.timedelta(5)

morning_time = datetime.time(4,00,00)
atr_list = []
df = web.DataReader("TSLA", 'yahoo', start, end)
for i in range(len(df)):
    atr_high = df.iloc[i]['High']
    atr_low = df.iloc[i]['Low']
    atr = atr_high - atr_low
    atr_list.append(atr)

true_atr = sum(atr_list) / len(atr_list)
# print(true_atr)


data = pd.read_csv('timedatesshit.csv')
# print(df)
# data = data.drop(columns = ["hour"])
# data = data.drop(columns = ["short date"])
# dates = data.iloc[0]['date']
pre_market_date = datetime.datetime.now()
pre_market_date = pre_market_date.date()
pre_market_date = pre_market_date - datetime.timedelta(1)

post_marekt_date = datetime.datetime.now()
post_marekt_date = post_marekt_date.date()
post_marekt_date = post_marekt_date - datetime.timedelta(2)
traded = ['GME','AAPL']

empty_list = []

for i in ((traded)):
    # print('stock traded ' + i)
    for j in range(len(data)-1):
        if data.iloc[j]['open'] > 13:
            empty_list.append(data.iloc[j]['open'])

        # print(' index position ' + str(j))

print(empty_list)







# print(pre_market_date, post_marekt_date)



# data['new date'] = pd.to_datetime(data['date'], format ='%Y-%m-%d:%H:%M:%S.%f')
# print(data)
# pre_market_date = datetime.datetime.now()
# pre_market_date = pre_market_date.date()
# format = '%Y-%m-%d %H:%M:%S'
# print(datetime.datetime.strptime(dates, format))
# pre_market_date = pre_market_date.strftime("%H:%M:%S")

# previous_day = pre_market_date - datetime.timedelta(1)


# print(type(pre_market_date))
# print(type(previous_day))

# print(type(dates))
# print(type(data.iloc[0]['hour']))
# print(type(data.iloc[0]['short date']))

#
# for i in range(10):
#     market_open_time = datetime.time(6,30,00)
#     market_close_time = datetime.time(13,00,00)
    # print(type(data.iloc[i]['hour']))
    # if morning_time < data.iloc[i]['hour']:
    #     print(morning_time)


# if end > datetime.time(12,30,00):
#     print('it is now past 12')
# print(datetime.datetime.now().strftime('%M:%S.%f')[:-4])
# print(end.time())
# print(morning_time)

a = 1
b =2
# if a > b or b > a:
#     value =

# restriction = end.date()
# print(restriction)
