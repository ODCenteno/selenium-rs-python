from selenium.webdriver.common.by import By


# Home Page
HOME_SHOP = (By.CSS_SELECTOR, "a[href*='shop']")


# SHOP Page
CARDS_LINK_CSS = (By.CSS_SELECTOR, ".card-title a")
CARD_BUY_BUTTON = (By.CSS_SELECTOR, ".card-footer button")
SHOP_CHECKOUT_BTN = (By.CSS_SELECTOR, "a[class*='btn-primary']")
