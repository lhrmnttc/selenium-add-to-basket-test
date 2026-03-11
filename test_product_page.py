import pytest
from pages.product_page import ProductPage


# проверяем добавление товара для разных promo ссылок
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",

    # тут известный баг сайта, поэтому тест помечаем как ожидаемо падающий
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail(reason="known bug")
    ),

    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])

def test_guest_can_add_product_to_basket(browser, link):

    # открываем страницу товара
    page = ProductPage(browser, link)
    page.open()

    # добавляем товар в корзину
    page.add_product_to_basket()

    # решаем капчу
    page.solve_quiz_and_get_code()

    # проверяем что название товара совпадает
    page.should_be_correct_product_name_in_message()

    # проверяем что цена корзины совпадает с ценой товара
    page.should_be_correct_product_price_in_basket()


# проверка обычной промо ссылки
def test_guest_can_add_product_to_basket_new_year(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_correct_product_name_in_message()
    page.should_be_correct_product_price_in_basket()


# проверяем что сообщение об успехе не появляется просто так
def test_guest_cant_see_success_message(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


# проверяем что после добавления товара нет лишнего success сообщения
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    page.should_not_be_success_message()


# проверяем что сообщение исчезает
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    page.success_message_should_disappear()