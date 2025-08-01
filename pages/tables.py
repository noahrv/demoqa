from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/webtables")
        self.btn_add = WebElement(driver, "#addNewRecordButton", "css")
        self.btn_submit = WebElement(driver, "#submit", "css")
        self.modal = WebElement(driver, "#userForm", "css")

        self.input_first_name = WebElement(driver, "#firstName", "css")
        self.input_last_name = WebElement(driver, "#lastName", "css")
        self.input_email = WebElement(driver, "#userEmail", "css")
        self.input_age = WebElement(driver, "#age", "css")
        self.input_salary = WebElement(driver, "#salary", "css")
        self.input_department = WebElement(driver, "#department", "css")

        self.next_button = WebElement(driver, "div.-next > button", "css")
        self.prev_button = WebElement(driver, "div.-previous > button", "css")
        self.page_info = WebElement(driver, "div.-pageInfo > span", "css")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_force(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @property
    def table_rows(self):
        return WebElement(self.driver, "div.rt-tr-group", "css")

    @property # без property чёт не работало
    def edit_buttons(self):
        return WebElement(self.driver, "span[title='Edit']", "css")

    @property
    def delete_buttons(self):
        return WebElement(self.driver, "span[title='Delete']", "css")

    def get_all_rows_text(self):
        return [row.text for row in self.table_rows.find_elements() if row.text.strip()]

    def fill_form(self, first, last, email, age, salary, department):
        self.input_first_name.send_keys(first)
        self.input_last_name.send_keys(last)
        self.input_email.send_keys(email)
        self.input_age.send_keys(age)
        self.input_salary.send_keys(salary)
        self.input_department.send_keys(department)

    def clear_form(self):
        self.input_first_name.clear()
        self.input_last_name.clear()
        self.input_email.clear()
        self.input_age.clear()
        self.input_salary.clear()
        self.input_department.clear()

    def delete_row_by_text(self, text):
        rows = self.table_rows.find_elements()
        delete_buttons = self.delete_buttons.find_elements()
        for i, row in enumerate(rows):
            if text in row.text:
                delete_buttons[i].click()
                break
