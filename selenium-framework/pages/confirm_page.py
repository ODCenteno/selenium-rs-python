from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.actions import PageActions
from utils import selectors as sel


class ConfirmPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.do = PageActions(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def send_country_to_deliver(self, country_text):
        self.do.type_text(sel.COUNTRY_INPUT, country_text)
        country_item = self.wait.until(
            EC.presence_of_all_elements_located(sel.COUNTRY_INDIA))
        return country_item

    def click_india_country(self):
        self.send_country_to_deliver("ind")
        self.do.click(sel.COUNTRY_INDIA)

    def click_checkbox(self):
        self.do.click(sel.CHECKBOX_CONTAINER)

    def get_checkbox_element(self):
        return self.do.get_element(sel.CHECKBOX)

    def submit_order(self):
        self.do.click(sel.SUBMIT_BTN)

    def get_alert_success_text(self):
        return self.do.get_text(sel.SUCCESS_ALERT)
