from pages.modal_dialogs import ModalDialogsPage
from pages.demoqa import DemoQA


class TestModalDialogs:
    def test_modal_elements(self, browser):
        modal_page = ModalDialogsPage(browser)
        modal_page.visit()

        assert modal_page.submenu_buttons.check_counts_elements(5)

    def test_navigation_modal(self, browser):
        modal_page = ModalDialogsPage(browser)
        demo_page = DemoQA(browser)

        modal_page.visit()

        modal_page.refresh()

        modal_page.icon.click()

        demo_page.back()

        browser.set_window_size(900, 400)

        demo_page.forward()

        assert demo_page.equal_url()

        assert browser.title == 'DEMOQA'

        browser.set_window_size(1000, 1000)