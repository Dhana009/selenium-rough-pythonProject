import random
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#webdriver
driver = webdriver.Chrome('D:/selenium_drivers/chromedriver.exe')

driver.get('https://images.google.co.in/')

input_box = driver.find_element_by_xpath('//*[@id="APjFqb"]')
input_box.click()
input_box.send_keys('apple')
time.sleep(1)

search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()
time.sleep(1)

for i in range(1,10):
    image1 = driver.find_element_by_xpath('//div[@class=" bRMDJf islir"]')
    image1.click()
    print(i)
    time.sleep(1)

    first_pic = driver.find_element_by_xpath('//img[@class="r48jcc pT0Scc iPVvYb"]')
    print(first_pic.get_attribute('src'))
    time.sleep(1)