from pages.basepage import BasePage
from utilities.teststatus import Status
import unittest
import pytest
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class LoginTests(unittest.TestCase, BasePage):

	@pytest.fixture(autouse=True)
	def classSetup(self, oneTimeSetUp):
		self.ts = Status(self.driver)

	@pytest.mark.run(order=1)
	@data(getCSVData("testdata.csv","invalidemail"))
	@unpack
	def test_InvalidEmail(self, email):
		self.clickSigninButton()
		self.enterEmail(email)
		self.verifyInvalidEmail()

	@pytest.mark.run(order=2)
	@data(getCSVData("testdata.csv","validemail","validpassword"))
	@unpack
	def test_validLogin(self, email, password):
		self.login(email, password)
		self.verifyLoginSuccessful()
