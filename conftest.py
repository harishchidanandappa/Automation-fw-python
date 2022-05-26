from selenium import webdriver
import pytest
from Data.config_data import FE_TestData


@pytest.fixture()
def setUp():
    yield


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("running one time setup")
    if browser == 'firefox':
        url = "https://wegodeliver.here.com/"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False)
        driver = webdriver.Firefox(executable_path=FE_TestData.geckodriver_path,
                                   firefox_profile=profile)
        driver.maximize_window()
        driver.implicitly_wait(1)

        driver.get(url)
        print("running tests on FF")
    else:
        url = "https://wegodeliver.here.com/"
        driver = webdriver.Chrome()
        # chrome_options = webdriver.ChromeOptions()
        driver.get(url)
        print("running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("running one time teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
