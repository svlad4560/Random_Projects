import smtplib

# sender_email = 'svlad4560@gmail.com'
# rec_email = ' sebithechihuahua@gmail.com'
# password = 'There890'
# message = 'test'
#
# server = smtplib.SMTP('smtplib.gmail.com',587)
# server.starttls()
# server.login(sender_email, password)
# print("login success")
# server.sendmail(sender_email,rec_email,message)
# print("sent")


li = ["svlad4560@gmail.com"] #list of email_id to send the mail

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("svlad@smbcap.com", "Trading121")
    message = "Message_you_need_to_send"
    s.sendmail("svlad4560@gmail.com", li[i], message)
    s.quit()
