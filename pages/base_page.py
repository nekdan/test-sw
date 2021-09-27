from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import auth
from auth import *

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def login_page(self):
        button_login = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='sign-in-home-button']")
        button_login.click()
        assert self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='sign-in-text']"), 'не открылась форма авторизации'

    def authorization(self, my_email, my_password):
        email = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='sign-in-email-input']")
        email.send_keys(my_email)
        password = self.browser.find_element_by_css_selector("[data-qa='sign-in-password-input']")
        password.send_keys(my_password)
        button_form = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='sign-in-form-button']")
        button_form.click()
        assert self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='start-search-text']"), 'не получилось авторизоваться'


    def presence_of_element_located(self, how, what, timeout=80):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
