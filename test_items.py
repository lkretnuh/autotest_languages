import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    button_add_to_basket = browser.find_element_by_css_selector(".btn-primary")
    assert button_add_to_basket != 0, "button add to basket doesn't visible or doesn't exist"
    time.sleep(10)