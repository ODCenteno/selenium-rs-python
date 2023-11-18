import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

BASE_URL = "https://rahulshettyacademy.com/angularpractice/"

driver = None


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
    """Setup method that controls the setup and teardown of the browser.

    Args:
        request: used from pytest to return the browser configuration

    Browser options: Chrome, Firefox, Safari
    """
    global driver
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
