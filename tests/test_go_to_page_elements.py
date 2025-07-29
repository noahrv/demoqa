from pages.demoqa import DemoQA

def test_go_to_page_elements(browser):
    demoqa_qa_page = DemoQA(browser)

    demoqa_qa_page.visit()
    assert demoqa_qa_page.equal_url()