import pandas as pd
import statistics
a = 5
b = 10
list_one = [1,2,3,4,5,6,7,8]
df = pd.DataFrame(data=list_one)
# for nums in range(len(list_one)):
#     print(nums)
for num in range(len(list_one)):
    sm = []
    if num > 2:
        some =  list_one[num:num+3]
        print(some)
        sm.append(some)

print(sm)
print(type(sm))

range_value = df[1:4]
# print(max(list_one[1:-4]))
# print(list_one[1:4])
# print(list_one[1:-4])
