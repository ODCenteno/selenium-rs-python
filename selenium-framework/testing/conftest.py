import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

BASE_URL = "https://rahulshettyacademy.com/angularpractice/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Select browser in CLI with: --browser  (default)",
        choices=("firefox", "safari", "chrome")
    )


@pytest.fixture(scope="class")
def setup(request):
    # Obteniendo el parámetro del CLI para el navegador elegido
    browser = request.config.getoption("browser")

    if browser == "chrome":
        service = ChromeService()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f'Browser {browser} not supported.')

    driver.implicitly_wait(5)
    driver.get(BASE_URL)
    driver.maximize_window()

    # Asignamos el driver a la instancia request para utilizarlo en las Test classes
    # Una instancia request se genera automáticamente con pytest.fixture
    request.cls.driver = driver
    yield
    driver.quit()
