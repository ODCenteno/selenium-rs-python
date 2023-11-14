from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ride_btn = (By.XPATH, '//button[normalize-space()="Call a taxi"]')
    comfort_icon = (By.CSS_SELECTOR, 'div[class="tcard-icon"] img[alt="Comfort"]')
    phone_input = (By.CLASS_NAME, 'np-text')
    phone_popup_input = (By.ID, 'phone') # Verificar valor
    phone_next_button = (By.XPATH, '//div[@class="buttons"]/button[normalize-space()="Siguiente"]')
    code_input = (By.ID, 'code')
    confirm_pn_button = (By.XPATH, '//button[normalize-space()="Confirmar"]')
    payment_selector = (By.CLASS_NAME, 'pp-value')
    add_card_checkbox = (By.CSS_SELECTOR, '.pp-checkbox')
    card_num_input = (By.ID, 'number')
    card_code_input = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    card_confirm_button = (By.XPATH, "//div[@class='pp-buttons']/button[@type='submit']")
    pay_modal_quit_btn = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return f"UrbanRoutesPage(driver={self.driver})"

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_taxi_service(self):
        self.driver.find_element(*self.ride_btn).click()

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_icon).click()
