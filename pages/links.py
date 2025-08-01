from pages.base_page import BasePage
from components.components import WebElement

class Links(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/links")
        self.home_link = WebElement(driver, "#simpleLink", "css")
