from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a service and browser instance
service_obj = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Visit a web page and finish interaction
driver.get('http://uitestingplayground.com/home')

# Basic locators
# ID, XPATH, CSS_SELECTOR, CLASS_NAME, TAG_NAME, NAME atribute, linkText

# Evaluate the page title
title_h1 = driver.find_element(By.TAG_NAME, 'h1').text
assert 'UI Test Automation' in title_h1

driver.find_element(By.XPATH, '//*[@id="overview"]/div/div[2]/div[4]/h3/a').click()
input_page_title = driver.find_element(By.CSS_SELECTOR, 'body > section > div > h3').text
assert 'Text Input' == input_page_title


driver.quit()