from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TripPage(BasePage):
    def find_last_trip(self):
        assert self.browser.find_elements(By.CSS_SELECTOR, ".item_BeJL")[0], "Не найдена поездка"
        assert self.browser.find_elements(By.CSS_SELECTOR, ".icon_3Lut .wrapper_1YB- img")[1], "У поездки нет иконки справки"


    def open_last_trip(self):
        last_trip = self.browser.find_elements(By.CSS_SELECTOR, ".item_BeJL")[0]
        last_trip.click()
        assert self.browser.find_element(By.CSS_SELECTOR, ".active_items_3Ctq"), "Поездка не загрузилась"


    def check_air_certificate(self):
        name_certificate = 'Справка о совершенном перелете'
        assert self.browser.find_element(By.CSS_SELECTOR, ".wrapper_1TzN.reference_texet_FJLQ.default_t7Ch"), \
            "В поездке не найдена справка о перелёте"
        header_certificate = self.browser.find_element(By.CSS_SELECTOR, ".wrapper_1TzN.reference_texet_FJLQ.default_t7Ch").text
        assert name_certificate == header_certificate, "Название справки отличается"


    def check_price_certificate(self):
        price_air_certificate = 350
        price_certificate_trip = int(self.browser.find_elements(
            By.CSS_SELECTOR, ".price_3Zvg [class ='wrapper_1TzN default_t7Ch']")[-1].text)
        assert price_certificate_trip == price_air_certificate, \
            f"Неверная стоимость справки: {price_certificate_trip} вместо {price_air_certificate}"


    def check_ticket_number(self):
        ticket_number = self.browser.find_element(By.CSS_SELECTOR, ".document_1llf .wrapper_1TzN").text[6:-1]
        blank_certificate_number = self.browser.find_element(
            By.CSS_SELECTOR, ".wrap_39Lu [class='wrapper_1TzN default_t7Ch']").text[14:29]
        assert ticket_number == blank_certificate_number, "Номер бланка справки отличается от номера билета"
        certificate_to_ticket = self.browser.find_element(
            By.CSS_SELECTOR, ".flight_certificate_wrap_7YIf .wrapper_1TzN.gray_Y9qc").text[17:-1]
        assert ticket_number == certificate_to_ticket, "Номер справки к билету отличается от номера билета"


    def check_download_certificate(self):
        tooltip = 'Справку можно будет скачать после совершения полета'
        assert self.is_element_present(By.CSS_SELECTOR, ".button_3aNJ.textual_8lTC.disabled_1u5v"), \
            "Кнопка Скачать справку активна или отсутствует"
        download_certificate = self.browser.find_element(By.CSS_SELECTOR, ".button_3aNJ.textual_8lTC.disabled_1u5v")
        actions = ActionChains(self.browser)
        actions.move_to_element(download_certificate).perform()
        download_certificate_hover = self.browser.find_element(
            By.CSS_SELECTOR, ".flight_certificate_wrap_7YIf .wrapper_1TzN.tooltip_content_2uTn").text
        assert tooltip == download_certificate_hover, "Неверный тултип у кнопки Скачать справку"


    def check_employe_certificate(self):
        employe_ticket = self.browser.find_elements(By.CSS_SELECTOR, ".wrapper_1TzN.text_V1L0.default_t7Ch")[0].text
        employe_certificate = self.browser.find_elements(By.CSS_SELECTOR, ".wrapper_1TzN.text_V1L0.default_t7Ch")[1].text
        assert employe_ticket == employe_certificate, "Разные сотрудники в билете и в справке"





