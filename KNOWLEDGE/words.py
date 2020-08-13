from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen 
from urllib.request import Request
import smtplib
import time
from datetime import datetime



req = Request("https://www.graduateshotline.com/gre-word-list.html#x2")
page_html = urlopen(req).read()
page_soup = soup(page_html,"html.parser")

word_meanings = page_soup.find_all('tr')
# print(word_meanings[261].text.split('\n'))
# print(len(word_meanings))

file = open('words_list.txt','a')
for i in word_meanings:
    sent = i.text.split('\n')
    sentance = " : ".join(sent)
    file.write(sentance)
    file.write('\n')


file.close()