def find_correct_numbers(above_high_close, range_75_to_high_close, range_50_to_75, range_25_to_50, range_low_to_25):
    if above_high_close > (range_75_to_high_close and range_50_to_75 and range_25_to_50 and range_low_to_25):
        print("best chances of success if when it is gapping up above a high")
    if range_75_to_high_close  > ( above_high_close and range_50_to_75 and range_25_to_50 and range_low_to_25):
        print("best chances of success if when it is gapping up in the 75 percent range")
    if range_50_to_75 > ( above_high_close and range_75_to_high_close and range_25_to_50 and range_low_to_25):
        print("best chances of success if when it is gapping up in the 50 to 75 percent range")
    if  range_25_to_50 > ( above_high_close and range_75_to_high_close and range_50_to_75  and range_low_to_25):
        print("best chances of success if when it is gapping up in the 25 to 50 percent range")
    if  range_low_to_25 > ( above_high_close and range_75_to_high_close and range_50_to_75  and range_25_to_50):
        print("best chances of success if when it is gapping up in the low to 25 percent range")
