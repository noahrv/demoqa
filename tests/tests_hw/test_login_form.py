from pages.form_page import FormPage
from pages.elements_page import WebElement


def test_select_state_and_city(browser):

    form_page = FormPage(browser)
    form_page.visit()

    form_page.state.scroll_to_element()

    form_page.state.click()
    form_page.state_input.send_keys("NCR")
    form_page.state_input.send_keys("\n") # вот тут мне помогал гугл, поэтому я не уверена, что это правильно

    form_page.city.click()
    form_page.city_input.send_keys("Delhi")
    form_page.city_input.send_keys("\n") # и тут тоже

    state_text = WebElement(browser, "#state .css-1uccc91-singleValue").get_text()
    city_text = WebElement(browser, "#city .css-1uccc91-singleValue").get_text()

    assert state_text == "NCR"
    assert city_text == "Delhi"

