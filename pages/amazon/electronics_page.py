import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class ElectronicsPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  LOCATORS
    _about_item = "//div[@id = 'feature-bullets']"

    #  ACTIONS
    def getItemText(self):
        return self.getElement(self._about_item).text

    #  FUNCTIONALITIES
    def item_page(self):
        self.getItemText()



