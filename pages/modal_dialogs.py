from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, 'header > a > img')
        self.submenu_buttons = WebElement(driver, 'div.element-list.show > ul > li')