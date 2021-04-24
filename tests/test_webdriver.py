from source.finding_elements import *

print("Execution starting ...")
# Scenario 1: WebDriver methods, properties, WebElements methods (input fields)
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()

# Scenario 2: Handling CheckBox
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()

# Scenario 3 : working with multiple elements, ecommerce website
# go to this website and search the product
print("scenario 3 started")
website = "http://automationpractice.com/index.php"
open_website(website)
ecommerce_search()
print("scenario 3 completed")
close_browser()

# Scenario 4: amazon example, find_elements
amazon_example()
print("Steps are completed!")