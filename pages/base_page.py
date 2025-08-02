import logging
from selenium.webdriver.common.by import By
from components.components import WebElement

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.viewport = WebElement(self.driver, "head > meta")

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def get_title(self):
       return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def alert(self):
        try:
            return self.driver.switch_to_alert
        except Exception as ex:
            logging.log(1, ex)
            return False

    def open(self):
        self.driver.get(self.base_url)

    def check_page_available(self):
        try:
            return self.driver.current_url == self.base_url
        except Exception as e:
            print(f"Ошибка при проверке доступности страницы: {e}")
            return False

