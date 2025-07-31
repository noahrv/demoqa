import time
from pages.text_box import TextBox
from components.components import WebElement


def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    full_name = 'Kentaro Miura'
    current_address = '2-12-8 Otowa, Bunkyo-ku, Tokyo 112-0013, Japan'

    text_box_page.name.send_keys(full_name)
    text_box_page.current_address.send_keys(current_address)
    text_box_page.btn_submit.click_force()
    time.sleep(3)

    output_name_text = WebElement(text_box_page.driver, '#output #name').get_text()
    output_address_text = WebElement(text_box_page.driver, '#output #currentAddress').get_text()

    assert output_name_text == 'Name:' + full_name
    assert output_address_text == 'Current Address :' + current_address