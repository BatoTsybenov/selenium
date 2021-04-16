# Finding elements:
# -by name,
# id,
# class name,
# xpath,
# css selector,
# text link,
# partial link test

from selenium import webdriver
#import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#driver.maximize_window()

url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.get(url)
print("now clicking the 'No thanks' button")
#time.sleep(2)
driver.find_element_by_link_text('No, thanks!').click()
# driver.close()
#driver.quit()

# find the Enter message a ,b
# enter 20,30
# bvalue_input.send_keys("30")
# avalue_input.send_keys("20")
avalue_input = driver.find_element_by_id('sum1').send_keys("20")
bvalue_input = driver.find_element_by_id('sum2').send_keys("30")
# click
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sum_button = driver.find_element_by_link_text("Get Total").click()
sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")

print("Steps are completed nah")

