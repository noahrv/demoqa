import pytest
from pages.modal_dialogs import ModalDialogsPage
from components.components import WebElement
from selenium.webdriver.common.by import By


def test_modal_dialogs(browser):
    modal_page = ModalDialogsPage(browser)
    modal_page.open()

    if False: # а если тут "if not modal_page.check_page_available():", то тест скипается
        pytest.skip("Страница недоступна")

    small_modal_btn = WebElement(browser, "#showSmallModal")
    large_modal_btn = WebElement(browser, "#showLargeModal")

    assert small_modal_btn.is_visible()
    assert large_modal_btn.is_visible()

    small_modal_btn.click()
    small_modal = WebElement(browser, "div.fade.modal.show")
    assert small_modal.is_visible()

    close_btn = WebElement(browser, "#closeSmallModal")
    close_btn.click()
    assert not small_modal.is_visible()

    large_modal_btn.click()
    large_modal = WebElement(browser, "div.fade.modal.show")
    assert large_modal.is_visible()

    close_btn = WebElement(browser, "#closeLargeModal")
    close_btn.click()
    assert not large_modal.is_visible()