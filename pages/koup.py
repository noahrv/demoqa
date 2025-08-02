from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Koup(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'http://the-internet.herokuapp.com/')
        self.link_add_locator = (By.LINK_TEXT, 'Add/Remove Elements')

    def visit(self):
        self.driver.get(self.base_url)

    def click_add_link(self):
        self.click(self.link_add_locator)

    def get_add_link_text(self):
        return self.get_text(self.link_add_locator)