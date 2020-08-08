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

def cleanData(lsst):
    for i in lsst:
        if i == '':
            lsst.remove(i)
    strr = '  ,  '.join(lsst)
    return strr

file.write('PRN  ,  SRN  ,  Name  ,  Class  ,  Section  ,  Cycle  ,  Department  ,  Branch  ,  Institute Name')
file.write('\n')

for i in range(25,27):
    if i<10:
        SRN = 'PES120180000{}'.format(i)
    elif i>=10 and i<100:
        SRN = 'PES12018000{}'.format(i)
    elif i>=100 and i<1000:
        SRN = 'PES1201800{}'.format(i)
    else:
        SRN = 'PES120180{}'.format(i)
        
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'knowClsSectionModalLoginId'))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'knowClsSectionModalLoginId'))).send_keys(SRN)
    driver.find_element_by_id('knowClsSectionModalSearch').click()

    time.sleep(1)
    page_html = driver.page_source
    page_soup = BeautifulSoup(page_html,'html.parser')

    data = page_soup.findAll("tr")

    for i in range(1,len(data)):
        data[i] = data[i].text.split('\n')
        strr = cleanData(data[i])
        file.write(strr)
        file.write('\n')


file.close()
