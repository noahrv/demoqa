from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alertButton = WebElement(self.driver, "#alertButton")
        self.confirmButton = WebElement(self.driver, "#confirmButton")
        self.confirmResult = WebElement(self.driver, "#confirmResult")
        self.promptButton = WebElement(self.driver, "#promptButton")
        self.promptResult = WebElement(self.driver, "#promptResult")