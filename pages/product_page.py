from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    # нажимаем кнопку добавить в корзину
    def add_product_to_basket(self):
        button = self.wait_for_visible(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    # получаем название товара со страницы
    def get_product_name(self):
        name = self.wait_for_visible(ProductPageLocators.PRODUCT_NAME)
        return name.text.strip()

    # получаем цену товара
    def get_product_price(self):
        price = self.wait_for_visible(ProductPageLocators.PRODUCT_PRICE)
        return price.text.strip()

    # получаем название товара из сообщения
    def get_added_product_name_from_message(self):
        name = self.wait_for_visible(ProductPageLocators.ADDED_PRODUCT_NAME_IN_MESSAGE)
        return name.text.strip()

    # получаем сумму корзины из сообщения
    def get_basket_total_from_message(self):
        total = self.wait_for_visible(ProductPageLocators.BASKET_TOTAL_IN_MESSAGE)
        return total.text.strip()

    # проверяем что название товара совпадает
    def should_be_correct_product_name_in_message(self):

        page_name = self.get_product_name()
        message_name = self.get_added_product_name_from_message()

        assert page_name == message_name, "название товара не совпадает"

    # проверяем что цена товара совпадает с ценой корзины
    def should_be_correct_product_price_in_basket(self):

        page_price = self.get_product_price()
        basket_total = self.get_basket_total_from_message()

        assert page_price == basket_total, "цена товара и корзины не совпадает"

    # проверяем что success сообщение отсутствует
    def should_not_be_success_message(self):

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "появилось сообщение об успехе, хотя не должно"

    # проверяем что сообщение исчезает
    def success_message_should_disappear(self):

        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "сообщение не исчезло"