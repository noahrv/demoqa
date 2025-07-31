from pages.form_page import FormPage


def test_placeholder_and_validation(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'

    pattern = form_page.user_email.get_dom_attribute('pattern')

    assert pattern == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()

    assert 'was-validated' in browser.find_element('id', 'userForm').get_attribute('class')
