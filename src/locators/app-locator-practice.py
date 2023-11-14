'''
Examples using different locators
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(By.NAME, 'email').send_keys('hello@example.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()

# Locators: CSS_SELECTOR, XPATH
# XPATH sintax: //tagname[@attribute='value'] example: //input[@type='submit']
# CSS_SELECTOR sintax: #id, .class_name, tag
# CSS_SELECTOR attributes sintax: tagname[attribute='value'] example: input[type='submit']

driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys('Omar')
driver.find_element(By.ID, 'inlineRadio1').click()
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

# Creating assertions
success_message = driver.find_element(By.CLASS_NAME, 'alert-success').text
assert 'Success' in success_message

# Selecting one element from a list of locators in page
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys('Hello')
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()


driver.quit()
