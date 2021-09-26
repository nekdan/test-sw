import pytest
import time
from selenium import webdriver
from pages.base_page import BasePage

import auth
from auth import test_auth

link = 'https://rc.gospodaprogrammisty.ru/'

test_auth()


def test_search_flight_one(browser):
    time.sleep(10)
    assert auth.is_element_present(browser, "[data-qa='start-search-text']"), 'не зашли в ЛК'
    button_airline = browser.find_element_by_css_selector("[data-qa='-searchAirline']")
    button_airline.click()
    assert auth.is_element_present(browser, "[class='wrapper_1TzN header_1Ghb default_t7Ch']"), 'не открылcя поиск АБ'
    time.sleep(5)
