from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

# import time
#
#
# def test_footer_text(browser):
#     demo_qa_page = DemoQA(browser)
#     demo_qa_page.visit()
#     time.sleep(2)
#     footer = browser.find_element(By.CSS_SELECTOR, 'footer span')
#     assert footer.text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#
#
# def test_center_text_on_elements_page(browser):
#     demo_qa_page = DemoQA(browser)
#     demo_qa_page.visit()
#     time.sleep(2)
#     browser.find_element(By.CSS_SELECTOR, 'div.card').click()
#     center_text = browser.find_element(By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6').text
#     assert center_text == 'Please select an item from left to start practice.'

def test_check_footer(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text_please(browser):
    demo_qa_page = DemoQA(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    assert el_page.text_please.get_text() == 'Please select an item from left to start practice.'
