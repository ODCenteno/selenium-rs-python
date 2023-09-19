import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
name = 'Daniel'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
time.sleep(2)
alert = driver.switch_to.alert
alert_text = alert.text
assert name in alert_text
alert.accept()

driver.quit()
