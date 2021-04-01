import datetime
import requests
import json
import pandas as pd
import smtplib
from email.message import EmailMessage

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

email_alert('Task Scheduler works', '7758468699@messaging.sprintpcs.com')

def send_ma_update():
    for stock in basket_of_stocks:
        dataa = get_price_history(stock, 'year',1,"daily",1)
        data = list(dataa['close'])
        ma_5 = sum(data[-5:]) / len(data[-5:])
        ma_50 = sum(data[-50:]) / len(data[-50:])
        ma_253 = sum(data[-253:]) / len(data[-253:])
        variable = dataa[-1:]['close']

        if int(variable) < ma_5:
            # ATAT [insert 10-digit number]@txt.att.net
            # sprint [insert 10-digit number]@messaging.sprintpcs.com
            #T-mobile [insert 10-digit number]@tmomail.net
            # verizon [insert 10-digit number]@vtext.com
            email_alert(stock + " is lower than its 5 day MA. Its 5 day MA is: " + str(ma_5), '7752241146@tmomail.net')
