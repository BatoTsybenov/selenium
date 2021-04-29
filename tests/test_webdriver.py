from source.finding_elements import *

print("Execution starting ...")
<<<<<<< HEAD

print("Scenario 1: WebDriver methods, properties, WebElements methods (input fields)")
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()

print("# Scenario 2: Handling CheckBox")
=======
# Scenario 1: WebDriver methods, properties, WebElements methods (input fields)
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()

# Scenario 2: Handling CheckBox
>>>>>>> origin/master
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()

<<<<<<< HEAD
print("# Scenario 3 : working with multiple elements, ecommerce website")
=======
# Scenario 3 : working with multiple elements, ecommerce website
>>>>>>> origin/master
# go to this website and search the product
print("scenario 3 started")
website = "http://automationpractice.com/index.php"
open_website(website)
ecommerce_search()
print("scenario 3 completed")
<<<<<<< HEAD

print("# Scenario 4: amazon example, find_elements")
# amazon_example()


print("# Scenario 5: drop down list")
drop_down_select()

print("# Scenario 6: drop down multi select methods")
drop_down_multi_select()

print("# Scenario 7: handling the js alert")
switch_to_alert()

print("# Scenario 8: handling the popup window")
switch_to_window()

print("Scenario 9: explicit wait cases")
explicit_wait_methods()

print("closing the browser")
close_browser()
print("Steps are completed!")

=======
close_browser()

# Scenario 4: amazon example, find_elements
amazon_example()
print("Steps are completed!")
>>>>>>> origin/master
