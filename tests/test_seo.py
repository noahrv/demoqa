from pages.demoqa import DemoQA

def test_check_title_demo(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'