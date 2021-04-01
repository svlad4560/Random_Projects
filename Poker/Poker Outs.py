test_list = [1,2,3,4,5,6,7,8,9,10]
for i in test_list:
    if i > 2:
        three_data_range = test_list[i-3:i]
        print(three_data_range)
