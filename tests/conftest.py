from base.webdriverfactory import *
import pytest


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, baseURL):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, baseURL)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--baseURL")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def baseURL(request):
    return request.config.getoption("--baseURL")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

