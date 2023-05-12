import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# webdriver
driver = webdriver.Chrome('D:/selenium_drivers/chromedriver.exe')

driver.get('https://images.google.co.in/')

# enter search query
input_box = driver.find_element_by_name('q')
input_box.click()
input_box.send_keys('apple')
time.sleep(1)

# click search button
search = driver.find_element_by_xpath('//*[@id="sbtc"]/button')
search.click()
time.sleep(1)

# click on first image
first_image = driver.find_element_by_css_selector('.rg_i')
first_image.click()
time.sleep(1)

# get source link of image
source_link = driver.find_element_by_css_selector('.n3VNCb.iJqzI.n3VNCb.iJqzI.aXOy0e.xKddTc.MZy1Rb')
print(source_link.get_attribute('src'))

# close browser
driver.quit()
