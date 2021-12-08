import math

# this is for the ATR stop calculator
# j= 0
# while j in range(3):
#     atr = input(" What is the stocks ATR? " )
#     atr = float(atr)
#     ATR_setpup = '''
#     25% of ATR: '''+ str(round((atr)*.25,2))+ '''
#     50% of ATR: '''+ str(round((atr)*.5,2)) +'''
#     75% of ATR: '''+ str(round((atr)*.75,2))
#
#     print(ATR_setpup)

# this is for stop calculator
i = 0
while i in range(2):

    test_input = 500

    trading_risks = input(str(" What is your stop loss? " ))
    trading_risks = float(trading_risks)
    how_i_want_it = '''
    Intraday | ''' + str(test_input) + '''
    Trading  | ''' + str(trading_risks) + '''

    _______________
    5%       | ''' + str((round((test_input * .05)/ trading_risks))) + '''
    _______________
    10%      | ''' + str((round((test_input * .10)/ trading_risks))) + '''
    _______________
    20%      | ''' + str((round((test_input * .20)/ trading_risks))) + '''
    _______________
    30%      | ''' + str((round((test_input * .30)/ trading_risks))) + '''
    _______________
    40%      | ''' + str((round((test_input * .40)/ trading_risks))) + '''

    '''

    print(how_i_want_it)
# list_of = [1,2,3,4,5,6]
# print(list_of[:len(list_of)-1])
