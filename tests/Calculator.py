from pages.basepage import BasePage
from utilities.teststatus import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class Calculator(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ts = Status(self.driver)

    @pytest.mark.run
    def test_Addition(self):
        self.verifyHeading()
        self.enterFirstNumber(3)
        self.selectOperator("ADDITION")
        self.enterSecondNumber(5)
        self.clickGoButton()
        self.verifyResult(8)

    @pytest.mark.run
    def test_Subtraction(self):
        self.verifyHeading()
        self.enterFirstNumber(10)
        self.selectOperator("SUBTRACTION")
        self.enterSecondNumber(5)
        self.clickGoButton()
        self.verifyResult(5)
