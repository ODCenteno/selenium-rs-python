import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.fixtures("setup")
class TestExample:

    # Agredar el parámetro setup, que es el método que viene de conftest.py
    def test_should_be_google(self, setup):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]").click()
        assert "doodles" in self.driver.current_url
