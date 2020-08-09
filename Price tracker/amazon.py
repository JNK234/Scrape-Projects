from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
from notify_run import Notify
import smtplib
import time
from datetime import datetime


# url="https://www.amazon.in/Intelligent-Investor-English-Paperback-2013/dp/0062312685/ref=sr_1_2?crid=1JPD2V9VAZZNG&dchild=1&keywords=intelligent+investor&qid=1595240928&sprefix=intelligen%2Caps%2C290&sr=8-2"
# url="https://www.amazon.in/Ikigai-H%C3%A9ctor-Garc%C3%ADa/dp/178633089X/ref=sr_1_3?dchild=1&keywords=books&qid=1595322735&sr=8-3"
# url="https://www.amazon.in/Subtle-Art-Not-Giving/dp/0062641549/ref=sr_1_4?dchild=1&keywords=books&qid=1595322735&sr=8-4"
url="https://www.amazon.in/Super-Rockerz-400-Bluetooth-Headphones/dp/B01FSYQ3XA/ref=sxin_8_ac_d_rm?ac_md=0-0-d2lyZWxlc3MgaGVhZHBob25lcyBib2F0-ac_d_rm&crid=FTWPF024AL8U&cv_ct_cx=wireless+headphones+boat&dchild=1&keywords=wireless+headphones+boat&pd_rd_i=B01FSYQ3XA&pd_rd_r=e3970f28-2452-4cf5-86fc-0022ca04b646&pd_rd_w=AYR3o&pd_rd_wg=erkVK&pf_rd_p=580d695e-ff07-4f3c-b5a8-e4f33d09401d&pf_rd_r=MBMMKKTEGVS0XYM8KEH0&psc=1&qid=1595487506&sprefix=wireless+h%2Caps%2C327&sr=1-1-fe323411-17bb-433b-b2f8-c44f2e1370d4"
#-----Functions list--------#

def cleanValue(amount):
    amount=amount.replace("₹","")
    amount=amount.replace(",","")
    amount=amount.replace(" ","")
    return amount

def notifyMe(texxt):
    notify = Notify()
    notify.send(texxt)

def send_mail(texxt,title):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('developer.jnk@gmail.com','fobrlbwlhgiedpnn')
    subject = "Price drop Alert of "+ str(title)
    body=texxt
    msg = f"Subject: {subject} \n\n {body} ".encode('utf-8').strip()
    # msg = u' '.join((subject, body)).encode('utf-8').strip()

    server.sendmail(
    'njwalapuram82@gmail.com',
    'jwalapuramnarasimha@gmail.com',
    msg
    )
    print("HEY Narasimha, EMAIL HAS BEEN SENT SUCCESSFULLY.")
    server.quit()
    exit()

def checkPrice(desired_price):
    uClient=uReq(url)
    page_html1=uClient.read()
    uClient.close()
    page_soup=soup(page_html1,"html.parser")

    title=page_soup.find(id="productTitle").get_text()
    # print(title.strip())

    price=page_soup.find(id="priceblock_ourprice").get_text()
    # print(price.strip())
    price_now=float(cleanValue(price))

    # desired_price=500

    print("THE PRODUCT : ",str(title).strip())
    print("THE CURRENT PRICE :",str(price_now).strip())
    print("THE DESIRED PRICE :",str(desired_price))

    texxt="The price of "+title+" is dropped below "+ str(desired_price)+" to "+ str(price_now) + ".Proceed and book "+str(title)+" from AMAZON quickly!!"


    if price_now<=desired_price:
        # notifyMe(texxt)
        send_mail(texxt,title)

count=0
desired_price=float(input("Enter the desired price to track :"))
while(True):
    print("Count :",count,"\n")
    checkPrice(desired_price)
    print("\n")
    count=count+1
    time.sleep(10)

