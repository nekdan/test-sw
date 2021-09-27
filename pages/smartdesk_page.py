from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SmartdeskPage(BasePage):

    def search_flight(self):
        button_airline = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='smartdesk-search-panel-searchAirline']")
        button_airline.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='search-airline-text']"), "Не открылcя поиск АБ"


    def open_trips(self):
        button_trip = self.browser.find_element(By.LINK_TEXT, "Поездки")
        button_trip.click()
        assert self.presence_of_element_located(By.CSS_SELECTOR, ".wrapper_1TzN.header_1rz9"), "Не открылись поездки"

