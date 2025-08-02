from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KoupAdd(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'http://the-internet.herokuapp.com/')
        self.btn_add_locator = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
        self.btns_delete_locator = (By.CLASS_NAME, 'added-manually')

    def equal_url(self):
        return self.driver.current_url == 'http://the-internet.herokuapp.com/add_remove_elements/'

    def click_add_button(self):
        self.click(self.btn_add_locator)

    def get_add_button_text(self):
        return self.get_text(self.btn_add_locator)

    def get_add_button_onclick(self):
        return self.get_attribute(self.btn_add_locator, 'onclick')

    def click_delete_buttons(self):
        while self.elements_exist(self.btns_delete_locator):
            self.click(self.btns_delete_locator)

    def get_delete_buttons_count(self):
        return self.elements_count(self.btns_delete_locator)

    def get_first_delete_button_text(self):
        return self.get_text(self.btns_delete_locator)

    def get_all_delete_buttons_texts(self):
        return [el.text for el in self.find_all(self.btns_delete_locator)]