from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options


# import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.techwithtim.net")
# options = Options()
# options.add_argument("-disable-notifications")
# browser = webdriver.Chrome('your path', chrome_options=options)
# driver.find_element_by_link_text('No, thanks!').is_displayed().click()
link = driver.find_element_by_xpath("//li[@id='menu-item-402']").click()
xmark = driver.find_element_by_xpath("//div[@id='dismiss-button']").click()
# alert_obj = driver.switch_to.alert
# alert_obj.dismiss()
# alert = driver.switch_to.alert
# alert.accept()
# link = driver.find_element_by_id("276").click()
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()
#     driver.back()
#     driver.back()
#     driver.back()
# except:
#     driver.quit()
