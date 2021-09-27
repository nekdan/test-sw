import pytest
import time
from pages.base_page import BasePage
from pages.avia_page import AviaPage
from pages.cart_page import CartPage
from pages.trip_page import TripPage
from pages.smartdesk_page import SmartdeskPage


link = 'https://rc.gospodaprogrammisty.ru/'
my_email = 'testova@dn.ru'
my_password = '123456'


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = BasePage(browser, link)
    page.open()
    page.login_page()
    page.authorization(my_email, my_password)


def test_buy_air_certificate(browser):
    page = SmartdeskPage(browser, link)
    page.search_flight()
    page_avia = AviaPage(browser, link)
    page_avia.city_selection_simple("Москва", "Санкт-Петербург")
    page_avia.departure_date(7)
    page_avia.search_button()
    page_avia.choose_airline_chekbox("Победа")
    page_avia.add_to_cart()
    page_cart = CartPage(browser, link)
    page_cart.aviability_air_certificate()
    page_cart.price_check_air_certificate()
    page_cart.go_to_payment()
    page_cart.confirm_payment()
    page_trip = TripPage(browser, link)
    page_trip.check_air_certificate()
    page_trip.check_price_certificate()
    page_trip.check_ticket_number()
    page_trip.check_download_certificate()
    page_trip.check_employe_certificate()

def test_check_air_certificate_trip(browser):
    page = SmartdeskPage(browser, link)
    page.open_trips()
    page_trip = TripPage(browser, link)
    page_trip.find_last_trip()
    page_trip.open_last_trip()
    page_trip.check_air_certificate()
    page_trip.check_price_certificate()
    page_trip.check_ticket_number()
    page_trip.check_download_certificate()
    page_trip.check_employe_certificate()
