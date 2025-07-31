import time
from pages.demoqa import DemoQA

def test_size(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(3)
    browser.set_window_size(1000, 1000)