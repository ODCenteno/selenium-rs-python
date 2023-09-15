from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://rahulshettyacademy.com/client/auth/login')


driver.quit()