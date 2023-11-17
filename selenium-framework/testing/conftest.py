import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.google.com")
    driver.maximize_window()

    # Asignamos el driver a la instancia request para utilizarlo en las Test classes
    # Una instancia request se genera automáticamente con pytest.fixture
    request.cls.driver = driver
    yield
    driver.quit()
