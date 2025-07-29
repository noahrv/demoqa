from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

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
