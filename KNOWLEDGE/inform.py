import smtplib
from datetime import datetime
import time
import re

file = open('words_list.txt','r')
words = file.readlines()

# print(words)
# for i in words:
#     if '\n' in i:
#         i = i.replace('\n','')
#     print(i)

def createFormat():
    print("...")



def send_mail(texxt):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('developer.jnk@gmail.com','fobrlbwlhgiedpnn')
    subject = "Vocab Training"
    body=texxt
    msg = f"Subject: {subject} \n\n {body} ".encode('utf-8').strip()

    server.sendmail(
    'njwalapuram82@gmail.com',
    'jwalapuramnarasimha@gmail.com',
    msg
    )
    print("HEY Narasimha, EMAIL HAS BEEN SENT SUCCESSFULLY.")
    server.quit()
    exit()

