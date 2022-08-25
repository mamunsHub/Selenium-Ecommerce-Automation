import time
import random
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# initializing web driver
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

#Open URL and maxiamize wiindow
driver.get('http://www.tutorialsninja.com/demo/')
driver.maximize_window()

# Selecting all phones
phones = driver.find_element(By.XPATH, "(//a[contains(text(),'Phones & PDAs')])[1]")
phones.click()

# Selecting Iphone
iphone = driver.find_element(By.XPATH, "(//a[normalize-space()='iPhone'])[1]")
iphone.click()
time.sleep(1)

#selecting first picture
first_pic = driver.find_element(By.XPATH, "(//img[@title='iPhone'])[1]")
first_pic.click()
time.sleep(2)

# total number of image finding
item_list = driver.find_element(By.XPATH, "(//ul[@class='thumbnails'])[1]")
items = item_list.find_elements(By.TAG_NAME, "li")
total_items = len(items) - 1

#next click selection
next_click = driver.find_element(By.XPATH, "(//button[@title='Next (Right arrow key)'])[1]")

#navigating to last picture and taking ss
for i in range(0, total_items):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')


#close image
close_image = driver.find_element(By.CSS_SELECTOR, "button[title='Close (Esc)']")
close_image.click()

#Input quantity
select_qty = driver.find_element(By.XPATH, "(//input[@id='input-quantity'])[1]")
select_qty.click()
time.sleep(2)

select_qty.clear()
time.sleep(1)
select_qty.send_keys('2')
time.sleep(1)

#Add to cart
cart = driver.find_element(By.ID, "button-cart")
cart.click()
time.sleep(3)

