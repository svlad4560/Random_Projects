import pandas as pd

# how to referce the order of a DataFrame
data_S = pd.read_csv("real_AAPL data.csv")

print(data_S)



# this is the way to manually get the list for th elast 5 day high range_count# for numbers in range(len(datas.index) - 2):
list_of_five_day_range = []
#so then it starts with the first list being the most recent and then [X,Y,Z] Z is the most recent
list_of_max_value = []
list_of_bars = list(data_S['high'])
bars = data_S.iloc[-5:]['high']
list_of_five_day_range.append(list(bars))
max_value = bars.max()
list_of_max_value.append(max_value)


bars1 = data_S.iloc[-6:-1]['high']
list_of_five_day_range.append(list(bars1))
max_value1 = bars1.max()
list_of_max_value.append(max_value1)

max_id = bars.max()
# print(list_of_bars[-6:-1])
print(data_S)

# [X,Y,Z] Z is the most recent with the list at [0] is the most recent data
print(f"{list_of_five_day_range} this is last 5 days of data")

# with the first number in the list is for the most recent first day high.
print(str(list_of_max_value)+" this is maxium number in last 5 days")

# when itterating through a pandas dataframe use this
open_value = spy_data.loc[num+1]["open"]

# this is how to get the range from a list
test_list = [1,2,3,4,5,6,7,8,9,10]
for i in test_list:
    if i > 2:
        three_data_range = test_list[i-3:i]
        print(three_data_range)
