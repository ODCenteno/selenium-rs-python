from selenium.webdriver.common.by import By
from utils.actions import PageActions
from utils import selectors as sel
from pages.checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.do = PageActions(self.driver)

    def click_shop_link(self):
        self.do.click(sel.HOME_SHOP)
