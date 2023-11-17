import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestExample:

    def __init__(self) -> None:
        self.home_page = HomePage(self.driver)

    # Agredar el parámetro setup, que es el método que viene de conftest.py
    def test_shopping_process_buys_blackberry(self):
        self.home_page.click_shop_link()
        self.home_page.search_card_by_name("Blackberry")
        self.home_page.click_checkout_btn()
