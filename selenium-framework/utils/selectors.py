from selenium.webdriver.common.by import By


# Home Page
HOME_SHOP = (By.CSS_SELECTOR, "a[href*='shop']")


# SHOP Page
CARD_TITLE = (By.CSS_SELECTOR, ".card-title a")
CARD_BUY_BUTTON = (By.CSS_SELECTOR, ".card-footer button")
SHOP_CHECKOUT_BTN = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
ITEM_H4 = (By.TAG_NAME, 'h4')
CONFIRM_CHECKOUT_BTN = (By.XPATH, "//button[@class='btn btn-success']")

# Confirm Page
COUNTRY_INPUT = (By.ID, "country")
COUNTRY_INDIA = (By.LINK_TEXT, "India")
CHECKBOX_CONTAINER = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
CHECKBOX = (By.ID, "checkbox2")
SUBMIT_BTN = (By.CSS_SELECTOR, "[type='submit']")
SUCCESS_ALERT = (By.CSS_SELECTOR, "[class*='alert-success']")
