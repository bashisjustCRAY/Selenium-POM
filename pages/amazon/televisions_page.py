import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
import time

class TelevisionsPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  LOCATORS
    _brand = "//span[.='Samsung']"
    _sort = "//select[@data-action='a-dropdown-select']"
    _led_tv = "//div[@data-cel-widget = 'search_result_2']"

    #  ACTIONS
    def clickBrand(self):
        self.elementClick(self._brand)

    def selectFilter(self, option):
        self.selectElement(option, self._sort)

    def clickLEDTV(self):
        self.elementClick(self._led_tv)

    #  FUNCTIONALITIES
    def filter_item(self, option):
        self.clickBrand()
        time.sleep(2)
        self.selectFilter(option)
        time.sleep(2)
        self.clickLEDTV()