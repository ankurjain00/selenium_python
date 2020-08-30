"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
	Class Calculator(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from utilities.util import Util
import utilities.custom_logger as cl
import logging
from utilities.teststatus import Status
import time

class BasePage(SeleniumDriver):
	log = cl.customLogger(logging.DEBUG)

	def __init__(self, driver):
		"""
		Init BasePage class

		Returns:
			None
		"""
		super(BasePage, self).__init__(driver)
		self.driver = driver
		self.util = Util()
		self.ts = Status(self.driver)

	def calculatorHeading(self): return self.getText("h3", "css")

	def enterFirstNumber(self, value):
		self.sendKeys(value, "[class^='input-small']:nth-child(1)", "css")

	def enterSecondNumber(self, value):
		self.sendKeys(value, "[class^='input-small']:nth-child(3)", "css")

	def selectOperator(self, operator): self.selectByValue(operator, "[ng-model='operator']", "css")

	def clickGoButton(self): self.click("gobutton", "id")

	def result(self):
		time.sleep(2)
		return self.getText("[class^='ng-scope'] td:nth-child(3)", "css")

	def verifyHeading(self):
		self.waitForPageToLoad()
		assert self.calculatorHeading() == "Super Calculator"

	def verifyResult(self, result):
		assert self.result() == str(result)
