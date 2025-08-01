import time
from pages.tables import Tables


def test_add_edit_delete_record(browser):
    table_page = Tables(browser)
    table_page.visit()

    table_page.btn_add.click()
    assert table_page.modal.exist()

    table_page.btn_submit.click()
    assert table_page.modal.exist()

    table_page.fill_form("Guts", "Gutsovich", "guts@mail.com", "24", "5000", "Warrior")
    table_page.btn_submit.click()

    rows_text = table_page.get_all_rows_text()
    assert any("Guts" in row for row in rows_text)

    rows = table_page.table_rows.find_elements()
    edit_buttons = table_page.edit_buttons.find_elements()

    for i, row in enumerate(rows):
        if "Guts" in row.text:
            table_page.scroll_to_element(edit_buttons[i])
            table_page.click_force(edit_buttons[i])
            break

    table_page.clear_form()
    table_page.fill_form("Griffith", "Griffithovich", "griffith@mail.com", "24", "6000", "King")
    table_page.btn_submit.click()

    rows_text = table_page.get_all_rows_text()
    assert any("Griffith" in row for row in rows_text)
    assert not any("Guts" in row for row in rows_text)

    rows = table_page.table_rows.find_elements()
    delete_buttons = table_page.delete_buttons.find_elements()

    for i, row in enumerate(rows):
        if "Griffith" in row.text:
            table_page.scroll_to_element(delete_buttons[i])
            table_page.click_force(delete_buttons[i])
            break

    time.sleep(1)
    rows_text = table_page.get_all_rows_text()
    assert not any("Griffith" in row for row in rows_text)

