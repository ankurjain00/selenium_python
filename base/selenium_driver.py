from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

	log = cl.customLogger(logging.DEBUG)

	def __init__(self, driver):
		self.driver = driver

	def screenShot(self, resultMessage):
		"""
		Takes screenshot of the current open web page
		"""
		fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
		screenshotDirectory = "../screenshots/"
		relativeFileName = screenshotDirectory + fileName
		currentDirectory = os.path.dirname(__file__)
		destinationFile = os.path.join(currentDirectory, relativeFileName)
		destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

		try:
			if not os.path.exists(destinationDirectory):
				os.makedirs(destinationDirectory)
			self.driver.save_screenshot(destinationFile)
			self.log.info("Screenshot save to directory: " + destinationFile)
		except:
			self.log.error("### Exception Occurred when taking screenshot")


	def getTitle(self):
		return self.driver.title

	def getByType(self, locatorType):
		locatorType = locatorType.lower()
		if locatorType == "id":
			return By.ID
		elif locatorType == "name":
			return By.NAME
		elif locatorType == "xpath":
			return By.XPATH
		elif locatorType == "css":
			return By.CSS_SELECTOR
		elif locatorType == "class":
			return By.CLASS_NAME
		elif locatorType == "link":
			return By.LINK_TEXT
		else:
			self.log.info("Locator type " + locatorType + " not correct/supported")
		return False

	def findElement(self, locator, locatorType="id"):
		element = None
		try:
			locatorType = locatorType.lower()
			byType = self.getByType(locatorType)
			element = self.driver.find_element(byType, locator)
			self.log.info("Element found with locator: " + locator + " and  locatorType: " + locatorType)
		except:
			self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
		return element

	def findElementList(self, locator, locatorType="id"):
		"""
		Get list of elements
		"""
		element = None
		try:
			locatorType = locatorType.lower()
			byType = self.getByType(locatorType)
			element = self.driver.find_elements(byType, locator)
			self.log.info("Element list found with locator: " + locator + " and  locatorType: " + locatorType)
		except:
			self.log.info("Element list not found with locator: " + locator + " and  locatorType: " + locatorType)
		return element

	def click(self, locator="", locatorType="id", element=None):
		"""
		Click on an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			element.click()
			self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
		except:
			self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)

	def sendKeys(self, data, locator="", locatorType="id", element=None):
		"""
		Send keys to an element
		Either provide element or a combination of locator and locatorType
		:rtype: object
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			element.send_keys(data)
			self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
		except:
			self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
			print_stack()

	def clearTextArea(self, locator="", locatorType="id", element=None):
		"""
		Send keys to an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			element.clear()
			self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
		except:
			self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
			print_stack()

	def selectByVisibleText(self, text, locator="", locatorType="id", element=None):
		"""
		Select an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			sel = Select(element)
			sel.select_by_visible_text(text)
			self.log.info("Select element with locator: " + locator + " locatorType: " + locatorType)
		except:
			self.log.info("Cannot Select the element with locator: " + locator + " locatorType: " + locatorType)
			print_stack()

	def selectByValue(self, value, locator="", locatorType="id", element=None):
		"""
		Select an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			sel = Select(element)
			sel.select_by_value(value)
			self.log.info("Select element with locator: " + locator + " locatorType: " + locatorType)
		except:
			self.log.info("Cannot Select the element with locator: " + locator + " locatorType: " + locatorType)
			print_stack()

	def getText(self, locator="", locatorType="id", element=None, info=""):
		"""
		Get 'Text' on an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator: # This means if locator is not empty
				self.log.debug("In locator condition")
				element = self.findElement(locator, locatorType)
			self.log.debug("Before finding text")
			text = element.text
			self.log.debug("After finding element, size is: " + str(len(text)))
			if len(text) == 0:
				text = element.get_attribute("innerText")
			if len(text) != 0:
				self.log.info("Getting text on element :: " + info)
				self.log.info("The text is :: '" + text + "'")
				text = text.strip()
		except:
			self.log.error("Failed to get text on element " + info)
			print_stack()
			text = None
		return text

	def isElementPresent(self, locator="", locatorType="id", element=None):
		"""
		Check if element is present
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			if element is not None:
				self.log.info("Element present with locator: " + locator + " locatorType: " + locatorType)
				return True
			else:
				self.log.info("Element not present with locator: " + locator + " locatorType: " + locatorType)
				return False
		except:
			print("Element not found")
			return False

	def isElementDisplayed(self, locator="", locatorType="id", element=None):
		"""
		Check if element is displayed
		Either provide element or a combination of locator and locatorType
		"""
		isDisplayed = False
		try:
			if locator:
				element = self.findElement(locator, locatorType)
			if element is not None:
				isDisplayed = element.is_displayed()
				self.log.info("Element is displayed with locator: " + locator + " locatorType: " + locatorType)
			else:
				self.log.info("Element not displayed with locator: " + locator + " locatorType: " + locatorType)
			return isDisplayed
		except:
			print("Element not found")
			return False

	def isElementEnable(self, locator="", locatorType="id", element=None):

		isEnable = False

		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			if element is not None:
				isEnable = element.is_enabled()
				self.log.info("Element is enable with locator: " + locator + " locatorType: " + locatorType)
			else:
				self.log.info("Element not enabled with locator: " + locator + " locatorType: " + locatorType)
			return isEnable

		except:
			print("Element not found")
			return False

	def elementPresenceCheck(self, locator, locatorType="id"):
		"""
		Check if element is present
		"""
		try:
			elementList = self.driver.find_elements(locatorType, locator)
			if len(elementList) > 0:
				self.log.info("Element present with locator: " + locator + " locatorType: " + str(locatorType))
				return True
			else:
				self.log.info("Element not present with locator: " + locator + " locatorType: " + str(locatorType))
				return False
		except:
			self.log.info("Element not found")
			return False

	def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
		element = None
		try:
			byType = self.getByType(locatorType)
			self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
			wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions={
				NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException})
			element = wait.until(EC.element_to_be_clickable((byType, locator)))
			self.log.info("Element appeared on the web page")
		except:
			self.log.info("Element not appeared on the web page")
			print_stack()
		return element

	def hoverOverelement(self, locator="", locatorType="id", element=None):
		"""
		Hover on an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement(locator, locatorType)
			hover = ActionChains(self.driver)
			hover.move_to_element(element).perform()
			self.log.info("Hover on element with locator: " + locator + " locatorType: " + locatorType)
			time.sleep(2)
		except:
			self.log.info("Cannot hover on the element with locator: " + locator + " locatorType: " + locatorType)
			print_stack()

	def webScroll(self, direction="up"):

		if direction == "up":
			# Scroll Up
			self.driver.execute_script("window.scrollBy(0, -1000);")

		if direction == "down":
			# Scroll Down
			self.driver.execute_script("window.scrollBy(0, 1000);")

	def scrollTo(self, element):
		location = element.getLocation()
		self.driver.execute_script("window.scrollTo(%d, %d);".format(location.x, location.y - 200))

	def isElementSelected(self, locator="", locatorType="id", element=None):
		"""
		Check if element is Selected
		"""
		isSelected = False
		try:
			if locator:  # This means if locator is not empty
				element = self.findElement (locator, locatorType)
			if element is not None:
				isSelected = element.is_selected()
				self.log.info("Element is selected with locator: " + locator + " locatorType: " + locatorType)
			else:
				self.log.info("Element not selected with locator: " + locator + " locatorType: " + locatorType)
			return isSelected
		except:
			print ("Element not found")
			return False

	def waitForPageToLoad(self):
		self.log.info("Checking if page is loaded.".format(self.driver.current_url))
		pageState = self.driver.execute_script('return document.readyState;')
		return pageState == 'complete'
