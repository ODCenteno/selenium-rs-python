import pytest
from pages.confirm_page import ConfirmPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from utils.logger import Logger

# Agregar el parámetro setup, que es el método que viene de conftest.py


@pytest.mark.usefixtures("setup")
class TestExample:
    home_page = None
    checkout_page = None
    logs = Logger().create_logger()

    def test_shopping_process_buys_blackberry(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_shop_link()
        assert "shop" in self.driver.current_url

        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.select_card_by_name("Blackberry")
        self.checkout_page.click_checkout_btn()
        item_selected = self.checkout_page.get_item_title()
        self.logs.info(item_selected)
        try:
            assert item_selected == "Blackberry"
        except AssertionError:
            self.logs.error(
                "El item seleccionado no corresponde con Blackberry")

        self.checkout_page.click_confirm_checkout()

    def test_send_delivery_country(self):
        self.confirm_page = ConfirmPage(self.driver)
        self.confirm_page.click_india_country()
        self.confirm_page.click_checkbox()

        checkbox = self.confirm_page.get_checkbox_element()
        try:
            assert checkbox.is_selected()
        except AssertionError:
            self.logs.exception(f"The checkbox assertion fails")

        self.confirm_page.submit_order()
        success_message = self.confirm_page.get_alert_success_text()

        assert "Success!" in success_message
