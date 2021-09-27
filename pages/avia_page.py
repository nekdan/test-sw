import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.utilities_methods import date_input_there, date_input_back
from selenium.webdriver.common.action_chains import ActionChains


class AviaPage(BasePage):

    def city_selection_simple(self, city1, city2):
        departure_city = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='search-airline-panel-city-from']")
        departure_city.send_keys(city1)
        time.sleep(2)
        departure_city.send_keys(Keys.ENTER)

        arrival_city = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='search-airline-panel-city-to']")
        arrival_city.send_keys(city2)
        time.sleep(2)
        arrival_city.send_keys(Keys.ENTER)


    def departure_date(self, number):
        #time.sleep(3)
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='search-airline-panel-date-from']"), \
            'Не нашли дату вылета туда'
        date_need = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='search-airline-panel-date-from']")
        date_need.send_keys(str(date_input_there(number)))


    def search_button(self):
        search_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='search-airline-panel-search-button']")
        search_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='search-airline-best-airlines']"), \
            "Поиск авиабилетов не запущен"
        assert self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='search-airline-items']"), "Пустая выдача"

    def choose_airline_chekbox(self, airline):
        airline_chekbox = self.browser.find_element(
            By.XPATH, f"//label[@data-qa='search-filters-airline-company']//div[text() = '{airline}']")
        actions = ActionChains(self.browser)
        actions.move_to_element(airline_chekbox).perform()
        airline_chekbox.click()
        assert self.is_element_present(
            By.XPATH, f"//div[@data-qa='search-airline-aircompany-includes']//div[text() = '{airline}']"), "Фильтр по АК не выбран"


    def add_to_cart(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='search-airline-button-cart']")
        actions = ActionChains(self.browser)
        actions.move_to_element(add_button).perform()
        add_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='search-button-cart-notification']"), \
            "Нотификация добавления не появилась"
        to_cart_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='header-cart']")
        to_cart_button.click()


