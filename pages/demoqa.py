from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement
from selenium.common.exceptions import NoSuchElementException


class DemoQA(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.btn_elements = WebElement(driver, 'div.card:nth-child(1)')
        self.text_footer = WebElement(driver, 'footer span')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True