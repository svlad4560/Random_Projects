

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
    page = requests.get(url=full_url_price_history, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    data = pd.DataFrame(data=content)
    df_of_columns = data["candles"].apply(pd.Series)
    return df_of_columns


data_S = get_price_history("DIS")
pd.set_option("display.max_rows", None, "display.max_columns", None)

##  how come this doesn't drop the coulms?
data_S.drop(columns=['high', 'low'])

print(data_S)


## Is there any way to make it loop to the length of the data frame?
## How come when I change the range() number it also changes the end value of gap_up count?
##I can't use the range_count varaible as a max loop

# so then the last row is the values for yesterdays trading day
def count_gap_ups(data):
    # data is the get_price_history
    # data['open'].iloc[-254] this is how to get the last value
    open_search_value = 251
    close_search_value = 250
    gap_up_count = 0
    range_count =len(data_S)

    for num in range(252):
        open_value = data_S.iloc[open_search_value]["open"]
        close_value = data_S.iloc[close_search_value]["close"]
        if open_value > close_value:
            gap_up_count += 1
        open_value -= 1
        close_search_value -= 1

    return gap_up_count
