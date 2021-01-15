import pandas as pd


list_one = [1,2,3,4,5,6,7,8]
df = pd.DataFrame(data=list_one)
# for nums in range(len(list_one)):
#     print(nums)
print(df)
print(df[1:4])
