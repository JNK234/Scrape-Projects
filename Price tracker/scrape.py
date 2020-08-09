from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
# from notify_run import Notify

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


my_url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"_3liAhj"})
# print(len(containers))
# print(soup.prettify(containers[0]))
for container in containers:    
    print(container.div.img["alt"])
    price=container.findAll("div",{"class":"_1uv9Cb"})
    print(price[0].text)
    rating=container.findAll("div",{"class":"hGSR34"})
    print(rating[0].text)
    print("\n\n")


# notify = Notify()
# notify.send('Hi there!')


