import numpy as np
import random
import pandas as pd
random_list = []
for i in range(0,100):
    n = random.randint(1,100)
    random_list.append(n)

print(len(random_list))

# df = pd.DataFrame(random_list)
# df.to_csv('stake.csv')

df_g = pd.read_csv('stake.csv')
# df_g.to_csv('test.csv')
print(df_g)
avg = df_g['0'].mean()
times_above_value = [x if x >= 25 else 0 for x in df_g['0']]
print((times_above_value))
df_g['times_above'] = times_above_value

df_g.to_csv('test.csv')

# print(df_g)
if :

    # TODO:


    if :
        todo
