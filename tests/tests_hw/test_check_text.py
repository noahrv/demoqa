import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


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