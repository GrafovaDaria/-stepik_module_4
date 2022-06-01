import time

def test_button_add_to_cart(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    assert browser.find_element_by_css_selector("#add_to_basket_form button")