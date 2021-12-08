import pandas as pd
import time
df = pd.DataFrame()
# df.to_csv('quick.csv')

# time.sleep(10)
good_df = pd.read_csv('quick.csv')
new_list = []
for i in range(len(good_df.Tags)):

    print(type(good_df.iloc[i]["Tags"]))
    chunks = good_df.iloc[i]["Tags"].split(',')
    new_list.append(chunks)

for i in new_list:

    lengh_of = len(i)
    if lengh_of == 2:

    # for j in i:
    #     print("ya")
