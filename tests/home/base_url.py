from selenium import webdriver
from pages.amazon.landing_page import LandingPage
from pages.amazon.televisions_page import TelevisionsPage
from pages.amazon.electronics_page import ElectronicsPage
import unittest


class FilterTest(unittest.TestCase):
    base_url = "https://www.amazon.in/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(base_url)

    def test_about_item(self):

        current_handle = self.driver.current_window_handle
        search_item = LandingPage(self.driver)
        search_item.filter_item()
        pick_brand = TelevisionsPage(self.driver)
        pick_brand.filter_item("Price: High to Low")
        handles = self.driver.window_handles
        for handle in handles:
            if handle not in current_handle:
                self.driver.switch_to.window(handle)
        about = ElectronicsPage(self.driver)
        about.item_page()
        self.driver.quit()