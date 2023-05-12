import random
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#webdriver
driver = webdriver.Chrome('D:/selenium_drivers/chromedriver.exe')

driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()


phones = driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phones.click()
time.sleep(1)

iphone = driver.find_element_by_xpath('//a[text()="Palm Treo Pro"]')
iphone.click()
time.sleep(1)

first_pic = driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(1)

next_Click = driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')

max_pages = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/figure/figcaption/div/div[2]")
a = max_pages.text.split(' ')
max_number = int(a[2])
print('max_pages',max_number)

close_button = driver.find_element_by_xpath('// button[ @ title = "Close (Esc)"]')

for i in range(0,max_number):
    if i != max_number-1:
        next_Click.click()
        time.sleep(1)
    else:
        driver.save_screenshot('screenshot#'+ str(random.randint(0,101)) + '.png')
        close_button.click()

#quantity
quantity = driver.find_element_by_id('input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

add_to_cart = driver.find_element_by_id("button-cart")
add_to_cart.click()

laptops = driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptops).perform()
laptop_2 = driver.find_element_by_xpath('//a[text()="Show AllLaptops & Notebooks"]')
laptop_2.click()

laptop_page = driver.find_element_by_xpath('//a[text()="HP LP3065"]')
laptop_page.click()

add_to_button_2 = driver.find_element_by_xpath('//button[@id = "button-cart"]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(1)

laptop_calendar = driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
laptop_calendar.click()

month_year = driver.find_element_by_xpath('//th[@class ="picker-switch"]')
next_button_calendar = driver.find_element_by_xpath('//th[@class ="next"]')

while month_year.text != 'December 2022':
    next_button_calendar.click()

date_button = driver.find_element_by_xpath('//td[text()="31"]')
date_button.click()
time.sleep(2)

add_to_button_2.click()

go_to_cart = driver.find_element_by_id('cart-total')
go_to_cart.click()
time.sleep(2)

checkout = driver.find_element_by_xpath('//p[@class = "text-right"]/a[2]')
checkout.click()
time.sleep(2)

guest = driver.find_element_by_xpath('//input[@value="guest"]')
guest.click()
time.sleep(1)

continue_button = driver.find_element_by_id('button-account')
continue_button.click()
time.sleep(1)

billing_details_top = driver.find_element_by_xpath('//a[text() = "Step 2: Billing Details "]')
billing_details_top.location_once_scrolled_into_view
time.sleep(1)

first_name = driver.find_element_by_id('input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_name')

last_name = driver.find_element_by_id('input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('last-name')

email = driver.find_element_by_id('input-payment-email')
email.click()
time.sleep(1)
email.send_keys('dhan@gmail.com')

telephone = driver.find_element_by_id('input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('846846541654')
billing_details_top.location_once_scrolled_into_view

company = driver.find_element_by_id('input-payment-company')
company.click()
time.sleep(1)
company.send_keys('company')

address_1 = driver.find_element_by_id('input-payment-address-1')
address_1.click()
time.sleep(1)
address_1.send_keys('address-1')

city = driver.find_element_by_id('input-payment-city')
city.click()
time.sleep(1)
city.send_keys('city-1')

postcode = driver.find_element_by_id('input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('515615')

country = driver.find_element_by_id('input-payment-country')
dropdown = Select(country)
dropdown.select_by_index(87)
time.sleep(2)

region = driver.find_element_by_id('input-payment-zone')
dropdown = Select(region)
dropdown.select_by_visible_text('Berlin')
time.sleep(2)

address_button_continue = driver.find_element_by_id('button-guest')
address_button_continue.click()
time.sleep(1)

address_button_delivery = driver.find_element_by_id('button-shipping-method')
address_button_delivery.click()
time.sleep(1)

terms = driver.find_element_by_xpath('//input[@name = "agree"]')
terms.click()
time.sleep(1)

address_button_payment = driver.find_element_by_id('button-payment-method')
address_button_payment.click()
time.sleep(1)

confirm_order =driver.find_element_by_id('button-confirm')
confirm_order.click()
time.sleep(1)

































