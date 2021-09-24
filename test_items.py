from time import sleep
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_items(browser):
    browser.get(link)
    sleep(5)
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'add-to-basket button not found'
