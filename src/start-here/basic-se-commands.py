from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

# Common methods used in selenium
driver.maximize_window()
driver.get('https://www.google.com/')

# navigation
driver.back()
driver.refresh()
driver.forward()

print(driver.title)
print(driver.current_url)

driver.close()