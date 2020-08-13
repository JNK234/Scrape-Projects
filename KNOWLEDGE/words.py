from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen 
from urllib.request import Request
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.graduateshotline.com/gre-word-list.html"
driver = webdriver.Chrome('/Users/narasimhajwalapuram/Downloads/chromedriver')
driver.get(url)


req = Request(url)
page_html = urlopen(req).read()
page_soup = soup(page_html,"html.parser")

# word_meanings = page_soup.find_all('tr')
# print(len(word_meanings))


# driver.find_element_by_id("loadx2").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loadx2"))).click()
time.sleep(2)
# driver.find_element_by_id("loadx3").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loadx3"))).click()
time.sleep(2)
# #########
# driver.find_element_by_id("loadx4").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loadx4"))).click()

time.sleep(3)
# driver.find_element_by_id("loadx5").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loadx5"))).click()

time.sleep(2)

source = driver.page_source
page_soup1 = soup(source,"lxml")

word_meanings = page_soup1.find_all('tr')
print(len(word_meanings))
# print(word_meanings[1310:])



# source = driver.page_source
# page_soup = soup(source,"lxml")

word_meanings = page_soup.find_all('tr')
print(len(word_meanings))
file = open('words_list.txt','a')
for i in word_meanings:
    sent = i.text.split('\n')
    sentance = " : ".join(sent)
    file.write(sentance)
    file.write('\n')


file.close()