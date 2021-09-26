from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from pages.avia_page import AviaPage
from pages.smartdesk_page import SmartdeskPage

# from search_flights import browser

link = 'https://rc.gospodaprogrammisty.ru/'
my_email = 'testova@dn.ru'
my_password = '123456'


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    # login_link = "https://rc.gospodaprogrammisty.ru"
    page = BasePage(browser, link)
    page.open()
    page.login_page()
    page.authorization(my_email, my_password)


def test_search_flight_one(browser):
    page = SmartdeskPage(browser, link)
    page.search_flight()
    page_avia = AviaPage(browser, link)
    page_avia.city_selection_simple("Москва", "Екатеринбург")
    page_avia.departure_date(3)
    page_avia.search_button()
    page_avia.choose_airline_chekbox("Аэрофлот")

