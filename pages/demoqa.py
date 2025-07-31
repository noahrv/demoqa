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
            self.find_element(locator='#app > header >a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        return self.find_element(locator='#app > header >a').click()

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False