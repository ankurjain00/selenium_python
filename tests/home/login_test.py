from pages.basepage import BasePage
from utilities.teststatus import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase, BasePage):

	@pytest.fixture(autouse=True)
	def classSetup(self, oneTimeSetUp):
		self.ts = Status(self.driver)

	@pytest.mark.run(order=2)
	def test_validLogin(self, email, password):
		self.login(email, password)
