import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class LandingPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  LOCATORS
    _hamburger = "//a[@id='nav-hamburger-menu']"
    _tv_electronics = "//div[.='TV, Appliances, Electronics']"
    _tv = "//a[@href='/gp/browse.html?node=1389396031&ref_=nav_em_sbc_tvelec_television_0_2_9_2']"

    #  ACTIONS
    def clickHamburger(self):
        self.elementClick(self._hamburger)

    def clickTvElectronics(self):
        self.elementClick(self._tv_electronics)

    def clickTV(self):
        self.elementClick(self._tv)

    #  FUNCTIONALITIES
    def filter_item(self):
        self.clickHamburger()
        self.clickTvElectronics()
        self.clickTV()

