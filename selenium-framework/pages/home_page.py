from selenium.webdriver.common.by import By
from utils.actions import PageActions
from utils import selectors as sel


class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.do = PageActions(self.driver)

    def click_shop_link(self):
        self.do.click(sel.HOME_SHOP)

    def search_card_by_name(self, item_name):
        cards = self.do.find_elements_by_CSS(sel.CARDS_LINK_CSS)
        i = -1

        for card in cards:
            i += 1
            cardText = card.text
            if cardText == item_name:
                self.do.click(sel.CARD_BUY_BUTTON)

        return cards

    def click_checkout_btn(self):
        self.do.click(sel.SHOP_CHECKOUT_BTN)
