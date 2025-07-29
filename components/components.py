from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        self.driver = driver
        self.by = by
        self.locator = locator

    def click(self):
        self.driver.find_element(self.by, self.locator).click()

    def get_text(self):
        return self.driver.find_element(self.by, self.locator).text

    def is_displayed(self):
        return self.driver.find_element(self.by, self.locator).is_displayed()