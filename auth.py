from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
#from search_flights import browser


link = 'https://rc.gospodaprogrammisty.ru/'
my_email = 'nik.danilushkin@smartway.today'
my_password = 'jkc342'

def is_element_present(browser, what):
    try:
        browser.find_element_by_css_selector(what)
    except NoSuchElementException:
        return False
    return True

def test_auth():
    #with webdriver.Chrome() as browser:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        button_login = browser.find_element_by_css_selector("[data-qa='sign-in-home-button']")
        button_login.click()
        assert is_element_present(browser, "[data-qa='sign-in-text']"), 'не открылась форма авторизации'

        email = browser.find_element_by_css_selector("[data-qa='sign-in-email-input']")
        email.send_keys(my_email)
        password = browser.find_element_by_css_selector("[data-qa='sign-in-password-input']")
        password.send_keys(my_password)
        button_form = browser.find_element_by_css_selector("[data-qa='sign-in-form-button']")
        button_form.click()
        assert is_element_present(browser, "[data-qa='start-search-text']"), 'не получилось авторизоваться'
        return browser
        #browser.quit()
