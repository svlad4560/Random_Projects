import datetime
import requests
import json
import pandas as pd
import smtplib
from email.message import EmailMessage

td_consumer_key = 'HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG'

def get_price_history(stocks,timeframe_big, num_of_days, timeframe , num_of_big_time):
    endpoint_price_history = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
    full_url_price_history = endpoint_price_history.format(stock_ticker=stocks,periodType=timeframe_big,period=num_of_days,frequencyType=timeframe,frequency=num_of_big_time)
    # endpoint_price_history.format(stock_ticker=stocks,periodType='year',period=1,frequencyType='daily',frequency=1)
    page = requests.get(url=full_url_price_history, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    data = pd.DataFrame(data=content)
    df_of_columns = data["candles"].apply(pd.Series)
    return df_of_columns

def email_alert( body, to):
    msg = EmailMessage()
    msg.set_content(body)
    # msg['subject'] = subject
    msg['to'] = to

    user = 'sebisalert@gmail.com'
    msg['from'] = user
    password = 'djmhxxqaufdxxbov'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit

basket_of_stocks = ['AMD','FB', 'AAPL', 'TSLA', 'SPY', 'QQQ']

def send_ma_update():
    for stock in basket_of_stocks:
        dataa = get_price_history(stock, 'year',1,"daily",1)
        data = list(dataa['close'])
        ma_5 = sum(data[-5:]) / len(data[-5:])
        ma_50 = sum(data[-50:]) / len(data[-50:])
        ma_253 = sum(data[-253:]) / len(data[-253:])
        variable = dataa[-1:]['close']

        if int(variable) < ma_5:
            email_alert(stock + " is lower than its 5 day MA. Its 5 day MA is: " + str(ma_5), '7752241146@tmomail.net')




        # print(str(ma_5)  +"  " +stock)
        # print(variable)


send_ma_update()
