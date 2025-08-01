import time
from pages.links import Links

def test_home_link_opens_new_tab(browser):
    page = Links(browser)
    page.open()

    assert page.home_link.get_text() == "Home"
    assert page.home_link.get_dom_attribute("href").rstrip("/") == "https://demoqa.com", "неверный href"
    # у меня изначально было без rstrip("/"), но без него тест падает

    assert len(browser.window_handles) == 1
    page.home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url.rstrip("/") == "https://demoqa.com", "открыта неверная вкладка"
