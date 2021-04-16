from time import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
sleep(5)

browser.get("https://google.com")

search_text_box = browser.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration")
search_text_box.send_keys(Keys.RETURN)
sleep(5)

search_text_box2 = browser.find_element_by_name("q")
search_text_box2.clear()
sleep(10)
browser.close()
print("completed!!!!")
