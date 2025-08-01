import time
from pages.alerts import Alerts
from components.components import WebElement
from selenium.webdriver.common.by import By


def test_timer_alert(browser):
    alerts_page = Alerts(browser)
    alerts_page.open()

    timer_alert_btn = WebElement(browser, "#timerAlertButton")
    assert timer_alert_btn.is_visible()

    timer_alert_btn.click()
    time.sleep(5)

    alert = browser.switch_to.alert
    assert alert.text == "This alert appeared after 5 seconds"
    alert.accept()