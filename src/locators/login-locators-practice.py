from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

user = {
    'first_name': 'daniel',
    'last_name': 'Johanes',
    'email':'demo@gmail.com',
    'password': 'Hello@1234',
    'phone_number': '+123456789',
    'new_password': 'ByeBye@1234'
}

service = Service(
    '/Users/omarcenteno/main-Docs/QA-Dev/selenium-drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)


def visit_main_page():
    driver.get('https://rahulshettyacademy.com/client/')


def login(new_user):
    driver.find_element(By.XPATH, '//input[@placeholder="email@example.com"]').send_keys(new_user['email'])
    driver.find_element(By.CSS_SELECTOR, '#userPassword').send_keys(new_user['password'])
    driver.find_element(By.ID, 'login').click()



def register_new_account(new_user):
    driver.find_element(By.LINK_TEXT, 'Register here').click()
    driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys(new_user['first_name'])
    driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys(new_user['last_name'])
    driver.find_element(By.XPATH, '//input[@placeholder="email@example.com"]').send_keys(new_user['email'])
    driver.find_element(By.XPATH, '//input[@placeholder="enter your number"]').send_keys(new_user['phone_number'])
    driver.find_element(By.ID, 'placeholder').send_keys(new_user['password'])


def recover_password(user):
    driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email address"]').send_keys(user['email'])
    driver.find_element(By.XPATH, '//input[@id="userPassword"]').send_keys(user['new_password'])
    driver.find_element(By.XPATH, '//input[@id="confirmPassword"]').send_keys(user['new_password'])
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

visit_main_page()
recover_password(user)

driver.quit()
