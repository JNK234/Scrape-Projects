from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests as req
import urllib.request
import time

driver = webdriver.Chrome('/Users/narasimhajwalapuram/Downloads/chromedriver')

file = open('student_details.csv','a')

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

# lsst =["PES1201800646","PES1201800453","PES1201801794","PES1201801893 ","PES1201800480","PES1201801174","PES1201801323","PES1201800636","PES1201802148","PES1201801080","PES1201801697","PES1201802097","PES1201801310","PES1201800514 ","PES1201800516","PES1201800564","PES1201801108","PES1201800478","PES1201800484","PES1201800765","PES1201801941 ","PES1201800466 ","PES1201801959","PES1201801521","PES1201801335 ","PES1201801756","PES1201801751","PES1201801076","PES1201800625","PES1201800685","PES1201800503","PES1201801768","PES1201801985","PES1201802036","PES1201801717","PES1201802067","PES1201801736","PES1201800920 ","PES1201800428","PES1201801083","PES1201800624","PES1201800798","PES1201801346","PES1201801508 ","PES1201801105","PES1201801997","PES1201800355","PES1201801510","PES1201800501","PES1201801036"]

for i in range(1923,2100):
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
