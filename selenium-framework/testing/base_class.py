import pytest


@pytest.mark.fixtures("setup")
class TestBase:

    # Agredar el parámetro setup, que es el método que viene de conftest.py
    def test_should_be_google(self, setup):
        pass
