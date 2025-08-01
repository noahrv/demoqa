from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.model_dialog = WebElement(driver, 'body > div.fade.model.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')

        self.state = WebElement(driver, '#state')
        self.state_input = WebElement(driver, '#react-select-3-input')
        self.city = WebElement(driver, '#city')
        self.city_input = WebElement(driver, '#react-select-4-input')
