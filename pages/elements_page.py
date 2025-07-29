from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        # self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, 'div:nth-child(1)')

        self.text_footer = WebElement(driver, "footer span")

        self.text_please = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

        # self.text_elements = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        # self.icon = WebElement(driver, 'header > a > img')
        # self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        # self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div> ul > #item-0 > span')
        # self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div> ul > #item-1 > span')