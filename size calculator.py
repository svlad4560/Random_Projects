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

    test_input = 100
    trading_risks = input(str(" What is your stop loss? " ))
    trading_risks = float(trading_risks)
    how_i_want_it = '''
    Intraday | ''' + str(test_input) + '''
    Trading  | ''' + str(trading_risks) + '''
    _______________
    10%      | ''' + str((round((test_input * .10)/ trading_risks))) + '''
    _______________
    20%      | ''' + str((round((test_input * .20)/ trading_risks))) + '''
    _______________
    30%      | ''' + str((round((test_input * .30)/ trading_risks))) + '''
    _______________
    40%      | ''' + str((round((test_input * .40)/ trading_risks))) + '''
    _______________
    50%      | ''' + str((round((test_input * .50)/ trading_risks))) + '''
    _______________
    60%      | ''' + str((round((test_input * .60)/ trading_risks))) + '''
    _______________
    70%      | ''' + str((round((test_input * .70)/ trading_risks))) + '''
    _______________
    80%      | ''' + str((round((test_input * .80)/ trading_risks))) + '''
    _______________
    90%      | ''' + str((round((test_input * .90)/ trading_risks))) + '''
    '''

    print(how_i_want_it)
