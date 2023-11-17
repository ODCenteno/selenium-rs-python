import time
from selenium.webdriver.common.by import By
from utils.actions import PageActions
from utils import selectors as sel


class CheckoutPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.do = PageActions(self.driver)

    def get_cards_titles(self):
        card_titles = self.do.find_elements_by_CSS(sel.CARD_TITLE)
        return card_titles

    def select_card_by_name(self, item_name):
        cards = self.get_cards_titles()
        i = -1

        for card in cards:
            i += 1
            card_text = card.text
            print(card_text)
            if card_text == item_name:
                self.driver.find_elements(*sel.CARD_BUY_BUTTON)[i].click()
        return cards

    def click_checkout_btn(self):
        self.do.click(sel.SHOP_CHECKOUT_BTN)

    def get_item_title(self):
        return self.do.get_text(sel.ITEM_H4)

    def click_confirm_checkout(self):
        self.do.click(sel.CONFIRM_CHECKOUT_BTN)
