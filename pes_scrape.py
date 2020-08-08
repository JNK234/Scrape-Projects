from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests as req
import urllib.request
import time

driver = webdriver.Chrome('/Users/narasimhajwalapuram/Downloads/chromedriver')

file = open('List_details.csv','a')

driver.get('https://pesuacademy.com/Academy/')
driver.find_element_by_id('knowClsSection').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'knowClsSectionModalLoginId'))).send_keys('PES1201800625')
driver.find_element_by_id('knowClsSectionModalSearch').click()

time.sleep(1)
page_html = driver.page_source
page_soup = BeautifulSoup(page_html,'html.parser')

data = page_soup.findAll("tr")

for i in data:
    print(i.text)
    break


