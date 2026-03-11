from selenium.webdriver.common.by import By


class ProductPageLocators:
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Название товара на странице (в product_main)
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

    # Цена товара на странице (в product_main)
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # Сообщения после добавления в корзину:
    # 1) Первое сообщение: "<название товара> has been added to your basket."
    ADDED_PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")

    # 2) Инфо о стоимости корзины: "Your basket total is now <цена>"
    BASKET_TOTAL_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")