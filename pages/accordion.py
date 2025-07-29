from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1_heading = WebElement(driver, '#section1Heading')
        self.section1_content = WebElement(driver, '#section1Content > p')
        self.section2_heading = WebElement(driver, '#section2Heading')
        self.section2_content_p1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section2_content_p2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3 = WebElement(driver, '#section3Heading')
        self.section3_content = WebElement(driver, '#section3Content > p')