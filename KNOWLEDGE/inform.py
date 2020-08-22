import smtplib
from datetime import datetime
import time
import re

timenow = datetime.now().strftime("%H:%M:%S")

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

file = open('words_list.txt','r')
words = file.readlines()

word_list = []

for i in range(0,len(words),10):
    lsst = []
    lsst.append(words[i:i+10])
    word_list.append(lsst)
    
def createFormat(word_list):
    mail_post = """Here is the set of words and meanings....\n\n"""

    word_list = word_list[0]
    for i in range(len(word_list)):
        strr = str(i +1) +". "+ word_list[i]
        mail_post = mail_post + strr

    return mail_post

for i in word_list:
    mail_post = createFormat(i)
    send_mail(mail_post)
    time.sleep(10)
    




