import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


#default URL
URL = f'http://127.0.0.1:54306/wd/hub'

@pytest.fixture
def get_driver_local(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def wd_driver(request):
    browser = request.param

    if browser == "chrome":
        capabilities = webdriver.ChromeOptions()
    elif browser == 'firefox':
        capabilities = webdriver.FirefoxOptions()

    driver = webdriver.Remote(
        command_executor=URL,
        options=capabilities
    )

    driver.implicitly_wait(2)
    yield driver
    driver.quit()



