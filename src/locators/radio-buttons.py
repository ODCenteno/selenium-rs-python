import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

radios = driver.find_elements(By.XPATH, '//input[@type="radio"]')

for radio in radios:
    if radio.get_attribute('value') == 'radio2':
        radio.click()
        assert radio.is_selected()
        break

time.sleep(2)
driver.close()
