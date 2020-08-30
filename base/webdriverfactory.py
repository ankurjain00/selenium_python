"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser, baseURL):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        baseURL = "http://juliemr.github.io/protractor-demo/"

        self.browser = browser
        self.baseURL = baseURL
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        options = Options()
        options.add_argument('--proxy-bypass-list=*')
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--no-sandbox")
        chromedriver = "chromedriver.exe"

        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chromeoptions":
            # Set chrome driver
            driver = webdriver.Chrome(chromedriver,chrome_options=options)
        else:
            driver = webdriver.Firefox()
            # Maximize the window
            driver.maximize_window()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Loading browser with app URL
        driver.get(self.baseURL)

        return driver