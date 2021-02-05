test_list = [1,2,3,4,5,6,7,8,9,10]
for i in test_list:
    if i > 4:
        three_data_range = test_list[i-5:i]
        if len(three_data_range) != 5:
            break
        print(three_data_range)
