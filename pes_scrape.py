from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/narasimhajwalapuram/Downloads/chromedriver')

driver.get('https://pesuacademy.com/Academy/')

driver.find_element_by_id('knowClsSection').click()




