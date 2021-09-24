from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# from search_flights import browser

link = 'https://rc.gospodaprogrammisty.ru/'
my_email = 'nik.danilushkin@smartway.today'
my_password = 'jkc342'

def is_element_present(browser, what):
    try:
        browser.find_element_by_css_selector(what)
    except NoSuchElementException:
        return False
    return True

def login_page(browser):
    button_login = browser.find_element_by_css_selector("[data-qa='sign-in-home-button']")
    button_login.click()
    assert is_element_present(browser, "[data-qa='sign-in-text']"), 'не открылась форма авторизации'

def email_send(browser):
    email = browser.find_element_by_css_selector("[data-qa='sign-in-email-input']")
    email.send_keys(my_email)

def password_send(browser):
    password = browser.find_element_by_css_selector("[data-qa='sign-in-password-input']")
    password.send_keys(my_password)

def test_auth():
    # with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    login_page(browser)
    email_send(browser)
    password_send(browser)

    button_form = browser.find_element_by_css_selector("[data-qa='sign-in-form-button']")
    button_form.click()
    assert is_element_present(browser, "[data-qa='start-search-text']"), 'не получилось авторизоваться'
    return browser
    # browser.quit()
