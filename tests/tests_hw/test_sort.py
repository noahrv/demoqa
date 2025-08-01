import time
from pages.tables import Tables

def test_table_sorting_by_headers(browser):
    tables_page = Tables(browser)
    tables_page.open()

    headers = tables_page.get_headers()

    for header in headers:
        header_text = header.text.strip()
        if not header_text:
            continue

        class_before = header.get_attribute("class")
        header.click()
        time.sleep(1)

        class_after = header.get_attribute("class")
        assert class_before != class_after, f"сортировка по '{header_text}' не сработала"

        header.click()
        time.sleep(1)

        class_after_second_click = header.get_attribute("class")
        assert class_after != class_after_second_click, f"вторая сортировка по '{header_text}' не изменилась"
