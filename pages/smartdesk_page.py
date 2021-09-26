from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SmartdeskPage(BasePage):

    def search_flight(self):
        button_airline = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='smartdesk-search-panel-searchAirline']")
        button_airline.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[class='wrapper_1TzN header_1Ghb default_t7Ch']"), "не открылcя поиск АБ"
