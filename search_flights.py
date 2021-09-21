import pytest
import time
from selenium import webdriver

import auth
from auth import test_auth

link = 'https://rc.gospodaprogrammisty.ru/'
test_auth()

def test_search_flight_one():
    button_airline = auth.webdriver.Chrome.find_element_by_css_selector(auth.webdriver.Chrome, "[data-qa='-searchAirline']")
    button_airline.click()
    time.sleep(5)
    auth.webdriver.Chrome.quit()