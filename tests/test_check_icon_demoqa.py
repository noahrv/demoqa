from pages.demoqa import DemoQA

def test_check_icon(browser):
    demoqa_qa_page = DemoQA(browser)
    demoqa_qa_page.visit()
    demoqa_qa_page.click_on_the_icon()
    assert demoqa_qa_page.equal_url()
    assert demoqa_qa_page.exist_icon()