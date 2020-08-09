from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver=webdriver.Chrome("/usr/local/bin/chromedriver-2")

url = "https://pesuacademy.com/Academy/"

file = open("OUTPUTS/list.txt",'a')

fields = ['PRN' , 'SRN' , 'Name' , 'Class' ,'Section' , 'Cycle', 'Department', 'Branch' ,'Institute Name']

def writeData(lsst):
    lsst = list(filter(lambda a: a != '',lsst))
    sentance = " , ".join(lsst)
    file.write(sentance)
    file.write("\n")

driver.get(url)
driver.find_element_by_id("knowClsSection").click()

writeData(fields)

for i in range(2000,2051):
    if i<10:
        SRN = "PES120180000{}".format(i)
    elif i<100 and i>=10:
        SRN = "PES12018000{}".format(i)
    elif i>=100 and i<1000:
        SRN = "PES1201800{}".format(i)
    elif i>=1000:
        SRN = "PES120180{}".format(i)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "knowClsSectionModalLoginId"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "knowClsSectionModalLoginId"))).send_keys(SRN)
    driver.find_element_by_id("knowClsSectionModalSearch").click()


    time.sleep(1)

    page_source = driver.page_source

    page_soup=soup(page_source,"lxml")

    tableData = page_soup.find_all("tr")
    for i in range(1,len(tableData)):
        writeData(tableData[i].text.split("\n"))



file.close()