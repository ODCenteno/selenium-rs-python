from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a service and browser instance
service_obj = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Visit a web page and finish interaction
driver.get('https://www.google.com/')
driver.close()