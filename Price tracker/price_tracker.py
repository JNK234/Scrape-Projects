# This file is used to track price of desired item from  flipkart

from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
from notify_run import Notify
import smtplib
from datetime import datetime
import time


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
    subject = "Price drop Alert of "+ title
    # body = "Hey Amlan! \n The price of Phillips trimmer on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
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
    


#----Url----#

# my_url="https://www.flipkart.com/apple-iphone-se-red-64-gb/p/itm6e9443811d36a?pid=MOBFRFXHYMPBSB5H&lid=LSTMOBFRFXHYMPBSB5HVHY9KJ&marketplace=FLIPKART&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=40b47b1d-2855-4560-bc6d-645729659050.MOBFRFXHYMPBSB5H.SEARCH&ppt=sp&ppn=sp&qH=0b3f45b266a97d70"
# my_url="https://www.flipkart.com/apple-iphone-7-black-32-gb/p/itmen6daftcqwzeg?pid=MOBEMK62PN2HU7EE&lid=LSTMOBEMK62PN2HU7EEF7TO4A&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=07596c36-16f8-468b-b50a-2c930ef89ad6.MOBEMK62PN2HU7EE.SEARCH&ppt=sp&ppn=sp&ssid=xefcimmfpc0000001595233098784&qH=0b3f45b266a97d70"
# my_url="https://www.flipkart.com/the-intelligent-investor/p/itmfbqhvgjgsee2q?pid=9780062312686&lid=LSTBOK9780062312686FDPGWW&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&fm=SEARCH&iid=6d522443-aec0-40b5-beac-cb52531e8d24.9780062312686.SEARCH&ppt=sp&ppn=sp&ssid=7yxsrsc4000000001595248067076&qH=46652f9368fa66d0"
my_url="https://www.flipkart.com/boat-rockerz-400-bluetooth-headset/p/itm14d0416b87d55?pid=ACCEJZXYKSG2T9GS&lid=LSTACCEJZXYKSG2T9GSVY4ZIC&marketplace=FLIPKART&spotlightTagId=BestvalueId_0pm%2Ffcn&srno=s_1_4&otracker=search&otracker1=search&fm=SEARCH&iid=39ae5135-c1ce-4bda-a149-d2a4043116fb.ACCEJZXYKSG2T9GS.SEARCH&ppt=sp&ppn=sp&ssid=gib7oidmq80000001595487606296&qH=7dcb216432638bcc"
#----Code---#
def findPrice(desired_price):
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")

    title=page_soup.find("span",{"class":"_35KyD6"}).text
    # print(title)

    price=page_soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text
    # print(cleanValue(price))
    price_now=int(cleanValue(price))

    x=page_soup.findAll("li",{"class":"_2-riNZ"})
    spec=[]
    for i in x:
        spec.append(i.text)
    # print(spec)
    

    print("THE PRODUCT : ",str(title.strip()))
    print("THE CURRENT PRICE :",str(cleanValue(price).strip()))
    print("THE DESIRED PRICE :",str(desired_price))

    texxt="The price of "+title+" is dropped below "+ str(desired_price)+" to "+ str(price_now) + "."+" Proceed and book " + str(title) + " from flipkart quickly."

    if price_now<=desired_price:
        # notifyMe(texxt)
        send_mail(texxt,title)

        

count=0
desired_price=float(input("Enter the desired price to track :"))
while(True):
    print("Count :",count,"\n")
    findPrice(desired_price)
    print("\n")
    count=count+1
    time.sleep(10)

    


    









