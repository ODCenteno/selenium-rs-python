import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text('Female')
#dropdown.select_by_value()


# Dinamic Dropdown
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, "autosuggest").send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')

for country in countries:
    if country.text == 'India':
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

driver.quit()
