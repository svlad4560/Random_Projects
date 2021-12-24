import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
import statistics
from scipy import stats
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn import preprocessing
from sklearn import utils

# df = get_price_history("DKNG", 'day',1,"minute",1)
df = pd.read_csv("Seesif1min1.csv")
new_1 = pd.read_csv('test reg.csv')
print(new_1)

# print(df)
# new = df.iloc[: , [1, 6, 7]].copy()
# print(new)



# print(data)
# avg_high = [None, None,None,None,None]
# atr_list = []
# hig_open_list = []
# five_day_high_average_list = [None, None,None,None,None]
# low_5day_range_list = [None, None,None,None,None]
#
# for i in range(len(df)):
#     high = df.iloc[i]['high']
#     low = df.iloc[i]['low']
#     open = df.iloc[i]['open']
#     close = df.iloc[i]['close']
#
#     atr_list.append(df.iloc[i]['high']-df.iloc[i]['low'])
#     high_open = close-open
#     hig_open_list.append(high_open)
#     if i > 4:
#         five_day_range = df['high'][i-5:i]
#         low_range = df['low'][i-5:i]
#         mean_low = low_range.mean()
#         low_5day_range_list.append(mean_low)
#         # print(five_day_range)
#         mean_five_day = five_day_range.mean()
#         five_day_high_average_list.append(mean_five_day)
#
#
# df["atr"] = atr_list
# df["highopen"] = hig_open_list
# df['High 5 day average'] = five_day_high_average_list
# df['Low 5 range'] = low_5day_range_list
#
# avg_atr = df.atr.mean()
# avg_volume = df.volume.mean()
# avg_bar = df.highopen.mean()
#
# bar_greater_list = [None,None,None,None,None]
# close_less_than_average_list = [None,None,None,None,None]
# for i in range(len(df)):
#     if i > 4:
#         high = df.iloc[i]['high']
#         low = df.iloc[i]['low']
#         open = df.iloc[i]['open']
#         close = df.iloc[i]['close']
#         if (high-low) > avg_atr and df.iloc[i]["volume"] > avg_volume and (high-close) > avg_bar:
#             bar_greater_list.append(1)
#
#         else:
#             bar_greater_list.append(0)
#
#         if close <= df.iloc[i]['Low 5 range']:
#             close_less_than_average_list.append(1)
#         else:
#             close_less_than_average_list.append(0)
#
# df['bar more than average'] = bar_greater_list
# df['close less than low average'] =close_less_than_average_list
#
#
# price_5_later_list = [None,None,None,None,None]
# return_after_5_list = [None,None,None,None,None]
# for i in range(len(df)):
#     if i > 4:
#         if df.iloc[i]['close less than low average'] == 1:
#             # print(i)
#
#
#             close_price_5_min_later = df.loc[i+5]['close']
#             return_5_min = close_price_5_min_later-df.iloc[i]["close"]
#             return_after_5_list.append(return_5_min)
#             price_5_later_list.append(close_price_5_min_later)
#         else:
#             price_5_later_list.append(0)
#             return_after_5_list.append(0)
#
#
# df['Price 5 min later'] = price_5_later_list
# df['return 5 min after'] = return_after_5_list


x = new_1.drop(columns= ['return 5 min after'])
y = new_1['return 5 min after']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(y_train)
print(training_scores_encoded)
print(utils.multiclass.type_of_target(y_train))
print(utils.multiclass.type_of_target(y_train.astype('int')))
print(utils.multiclass.type_of_target(training_scores_encoded))
model = DecisionTreeClassifier()
model.fit(x_train,training_scores_encoded)
prediction = model.predict(x_test)

score = accuracy_score(y_test,prediction)

print(score)
# df.to_csv('Seesif1min.csv')
# print(df)
# print(df.plot(x = 'Low', y = 'High 5 day average', kind = 'line'))
