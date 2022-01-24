from selenium import webdriver
import os



driver = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
driver.get('https://www.google.com/images')

##search_box = driver.find_element_by_id('spch')
##search_box.send_keys("cars")
##search_box.send_keys(Keys.ENTER)
