from source.finding_elements import *

print("Execution starting ...")


def test_webdriver_input_elements():
    print("Scenario 1: WebDriver methods, properties, WebElements methods (input fields)")
    url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
    open_website(url_inputs)
    back_forward()
    get_total_input_fields()


def test_checkbox():
    print("# Scenario 2: Handling CheckBox")
    url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
    open_website(url_checkbox)
    # create steps to test checkbox using selenium
    checkbox_test()


def test_eccomrece_product_example():
    print("# Scenario 3 : working with multiple elements, ecommerce website")
    # Scenario 3 : working with multiple elements, ecommerce website
    # go to this website and search the product
    print("scenario 3 started")
    website = "http://automationpractice.com/index.php"
    open_website(website)
    ecommerce_search()
    print("scenario 3 completed")


def test_amazone_example():
    print("# Scenario 4: amazon example, find_elements")
    amazon_example()


def test_drop_down():
    print("# Scenario 5: drop down list")
    drop_down_select()


def test_drop_down_multi_select():
    print("# Scenario 6: drop down multi select methods")
    drop_down_multi_select()


def test_js_alerts():
    print("# Scenario 7: handling the js alert")
    switch_to_alert()


def test_pop_upwindow():
    print("# Scenario 8: handling the popup window")
    switch_to_window()


def test_explicit_wait_methods():
    print("Scenario 9: explicit wait cases")
    explicit_wait_methods()


def drag_drop_action():
    print("Scenario 10")
    drag_drop_action()


def tes_mouse_move_to_element():
    print("Scenario 11:mouse actions methods")
    move_mouse_action()


print("closing the browser")
close_browser()
print("Steps are completed!")


