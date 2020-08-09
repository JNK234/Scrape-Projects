from bs4 import BeautifulSoup as soup 
# from urllib.request import urlopen as uReq
import requests
# from notify_run import Notify
import smtplib
# from datetime import datetime
import time

my_url="https://www.flipkart.com/boat-rockerz-400-bluetooth-headset/p/itm14d0416b87d55?pid=ACCEJZXYKSG2T9GS&lid=LSTACCEJZXYKSG2T9GSVY4ZIC&marketplace=FLIPKART&spotlightTagId=BestvalueId_0pm%2Ffcn&srno=s_1_4&otracker=search&otracker1=search&fm=SEARCH&iid=39ae5135-c1ce-4bda-a149-d2a4043116fb.ACCEJZXYKSG2T9GS.SEARCH&ppt=sp&ppn=sp&ssid=gib7oidmq80000001595487606296&qH=7dcb216432638bcc"

r = requests.get(my_url)
soup_data = soup(r.text, 'html.parser')

print(type(r))