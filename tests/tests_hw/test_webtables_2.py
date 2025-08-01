import time
from pages.tables import Tables
from selenium.webdriver.common.by import By


def test_pagination_behavior(browser):
    table_page = Tables(browser)
    table_page.visit()

    # вот этот кусочек я подглядела в интернетах, вроде бы рабочий
    browser.execute_script("""
        const select = document.querySelector('select[aria-label="rows per page"]');
        if (select) {
            select.value = "5";
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """)
    time.sleep(1)

    prev_button = browser.find_element(By.CSS_SELECTOR, ".-previous button")
    next_button = browser.find_element(By.CSS_SELECTOR, ".-next button")
    assert prev_button.get_attribute("disabled")
    assert next_button.get_attribute("disabled")

    for i in range(3):
        table_page.btn_add.click()
        table_page.clear_form()
        table_page.fill_form(f"Test{i}", f"User{i}", f"user{i}@mail.com", "30", "1000", "Dept")
        table_page.btn_submit.click()
        time.sleep(1)

    page_info = browser.find_element(By.CLASS_NAME, "-pageInfo").text
    assert "2" in page_info

    next_button = browser.find_element(By.CSS_SELECTOR, ".-next button")
    assert not next_button.get_attribute("disabled")

    table_page.scroll_to_element(next_button)
    next_button.click()
    time.sleep(1)

    current_page = browser.find_element(By.CSS_SELECTOR, ".-pageJump > input").get_attribute("value")
    assert current_page == "2"

    prev_button = browser.find_element(By.CSS_SELECTOR, ".-previous button")
    table_page.scroll_to_element(prev_button)
    prev_button.click()
    time.sleep(1)

    current_page = browser.find_element(By.CSS_SELECTOR, ".-pageJump > input").get_attribute("value")
    assert current_page == "1"