"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
	Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import utilities.custom_logger as cl
import logging
from utilities.teststatus import Status

class BasePage(SeleniumDriver):

	log= cl.customLogger(logging.DEBUG)

	def __init__(self, driver):
		"""
		Inits BasePage class

		Returns:
			None
		"""
		super(BasePage, self).__init__(driver)
		self.driver = driver
		self.util = Util()
		self.ts = Status(self.driver)

	#locators
	_signinButton = "nav-link-yourAccount"			# id
	_emailField = "ap_email"						# id
	_continueButton = "continue"					# id
	_passwordField = "ap_password"					# id
	_loginButton = "signInSubmit"					# id
	_editLogin = "span.a-color-secondary"			# css
	_invalidemail = "span.a-list-item"				# css

	def verifyPageTitle(self, titleToVerify):
		"""
		Verify the page Title

		Parameters:
			titleToVerify: Title on the page that needs to be verified
		"""
		try:
			actualTitle = self.getTitle()
			return self.util.verifyTextContains(actualTitle, titleToVerify)
		except:
			self.log.error("Failed to get page title")
			print_stack()
			return False

	def clickSigninButton(self):
		"""
		Clicks on the Sign in Button of the Application
		"""
		self.waitForElement(locator=self._signinButton,locatorType="id")
		self.elementClick(locator=self._signinButton,locatorType="id")

	def enterEmail(self, email):
		"""
		Enters the email address of the user
		:param email: user's registered email address
		"""
		self.clearTextArea(locator=self._emailField,locatorType="id")
		self.sendKeys(email,locator=self._emailField,locatorType="id")

	def enterPassword(self, password):
		"""
		Enters the valid password of the user
		:param password: registered user's password
		"""
		self.clearTextArea(locator=self._passwordField, locatorType="id")
		self.sendKeys(password,locator=self._passwordField,locatorType="id")

	def clickLoginButton(self):
		"""
		Clicks on Login button of the login form
		"""
		self.elementClick(locator=self._loginButton, locatorType="id")

	def clickContinueButton(self):
		"""
		Clicks on Continue button of the login form
		"""
		self.elementClick(locator=self._continueButton,locatorType="id")

	def verifyInvalidEmail(self):
		self.clickContinueButton()
		result = self.isElementPresent(locator=self._invalidemail,locatorType="css")
		self.ts.markFinal("Invalid Email", result, "Invalid Email Message not displayed")

	def verifyInvalidPassword(self):
		result = self.isElementPresent(locator=self._editLogin,locatorType="css")
		self.ts.markFinal("Invalid Password", result, "Invalid Password Message not displayed")

	def verifyLoginSuccessful(self):
		"""
		Verifies User Login
		:return: Logs success or failures in automation.log
		"""
		self.clickSigninButton()
		result = self.isElementPresent(locator=self._editLogin,locatorType="css")
		self.ts.markFinal("Valid Login", result, "Login Verification Unsuccessful")

	def login(self, email, password):
		"""
		Login in to the Application
		:param email: user's registered email address
		:param password: registered user's password
		:return: Logs success or failures in automation.log
		"""
		self.enterEmail(email)
		self.clickContinueButton()
		self.enterPassword(password)
		self.clickLoginButton()
