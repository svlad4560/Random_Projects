# from Google import Create_Service
import smtplib
import time
from selenium import webdriver
from email.message import EmailMessage

# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

# driver.get('https://www.myntcannabis.com/')
# time.sleep(5)
#
# print(driver.find_element_by_class_name("brand__link"))


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
# this is the correct way to have the statement
# email_alert("test test", '7758468699@messaging.sprintpcs.com')
# if __name__ == '__main__':
    # email_alert("this was sent with python", '7758468699@messaging.sprintpcs.com')

random = [0,1,2,3,4,5,6,7,8,9,10]
# new = [(first[num:num+ 3]) for num in range(0, len(first), 3)]
for num in random:
    new_list = [(random[num:num+ 3]) for num in range(0, len(random), 3)]

    # if len(new_list) < 3:
    #     break
    print(new_list)
# print(test1)
