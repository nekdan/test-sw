import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.utilities_methods import date_input_there, date_input_back
from selenium.webdriver.common.action_chains import ActionChains


class CartPage(BasePage):
    def aviability_air_certificate(self):
        description_certificate = 'Заказать справку-подтверждение совершенного перелёта (+350 рублей)'
        header_tooltip = 'Заменяет посадочный талон для бухгалтерии.'
        assert self.browser.find_elements(By.CSS_SELECTOR, ".certificate_content_UR3X .wrapper_1YB- img")[-1], \
            "Не найдена картинка для тултипа"
        #Не получается взять текст из div
        #top_tooltip = self.browser.find_elements(By.CSS_SELECTOR, ".certificate_content_UR3X .wrapper_lsVc .tooltip_3Wwl")[-2].text
        #rint(f"--ТУЛТИП=({top_tooltip})")
        #assert top_tooltip == header_tooltip, f"e: {top_tooltip}"
        assert self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='cart-air-certificate-checkbox']"), \
            "Нет чекбокса о покупке сертификата"
        text_certificate = self.browser.find_elements(By.CSS_SELECTOR, ".content_3idD .certificate_content_UR3X")[
            -1].text
        assert text_certificate != description_certificate, \
            f"не=: {text_certificate}={description_certificate}"


    def price_check_air_certificate(self):
        original_price_cart = int(
            self.browser.find_elements(By.CSS_SELECTOR, "[data-qa='cart-price-item']")[-1].text.replace(" ", ""))
        price_air_certificate = 350
        time.sleep(1)
        certificate_chekbox = self.browser.find_elements(By.CSS_SELECTOR, "[data-qa='cart-air-certificate-checkbox']")[-1]
        certificate_chekbox.click()
        time.sleep(1)
        new_price_cart = int(
            self.browser.find_elements(By.CSS_SELECTOR, "[data-qa='cart-price-item']")[-1].text.replace(" ", ""))
        assert new_price_cart == original_price_cart + price_air_certificate, \
            f"Цена билета изменилась не на 350 рублей, а на {original_price_cart - price_air_certificate}"
        time.sleep(2)
        certificate_chekbox.click()
        time.sleep(1)
        new_price_cart = int(
            self.browser.find_elements(By.CSS_SELECTOR, "[data-qa='cart-price-item']")[-1].text.replace(" ", ""))
        assert new_price_cart == original_price_cart, \
            f"Цена билета отличается от начальной на {new_price_cart - original_price_cart}"
        certificate_chekbox.click()

    def go_to_payment(self):
        buy_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='cart-price-button']")
        buy_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='cart-checkout-title']"), "Не перешли на страницу оплаты"

    def confirm_payment(self):
        confirm_checkbox = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='cart-checkout-finish-accept-rules']")
        confirm_checkbox.click()
        payment_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='cart-checkout-finish-buy']")
        payment_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='cart-booking']"), \
            "Процесс бронирования не запущен"
        if self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='cart-checkout-success-pay-title']"):
            print("Поездка оплачена")
            return True
        elif self.presence_of_element_located(By.CSS_SELECTOR, "[data-qa='cart-checkout-success-pay-title-need-confirmation']"):
            print("Созданы метаданные по поездке")
            return True
        else:
            print("Произошла ошибка при покупке")
            return False

    def clean_all_ticket(self):
        self.browser.execute_script("window.scrollTo(0,0);")
        clean_button = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='cart-delete-all-title']")
        clean_button.click()
        confirm_clean = self.browser.find_element(By.CSS_SELECTOR, "[data-qa='cart-delete-all-modal-success']")
        confirm_clean.click()
        assert self.is_element_present(By.CSS_SELECTOR, "[data-qa='cart-empty']"), \
            "Корзина не очищена"