import time
from faker import Faker
from base.base_class import Base


class Cart_page(Base):

    # Locators
    page_title = "//h1[contains(@class,'page-header__title')]"
    decrease_button = "//span[contains(@class,'decrease')]" #кнопка минуса, для понижения количества товара
    cart_product_title = "//div[@class='product-name']/a"
    cart_product_price = "//div[@class='product-price']/span/bdi"
    subtotal_price = "//th[normalize-space(text())='Subtotal']//..//bdi"
    total_price = "//th[normalize-space(text())='Total']//..//bdi"
    calculate_shipping = "//a[@class ='shipping-calculator-button']" #Кнопка подсчёта доставки Calculate shipping
    cart_update_message = "//div[@class = 'woocommerce-message']"
    shipping_state_input = "//input[@id='calc_shipping_state']"  # поле области проживания
    shipping_city_input = "//input[@id='calc_shipping_city']"#поле город проживания
    shipping_postcode_input = "//input[@id='calc_shipping_postcode']" # поле почтового индекса
    update_shipping_button = "//button[@name='calc_shipping']"  # кнопка применить внесённые данные доставки
    shipping_costs_updated_text = "//div[@class='woocommerce-info']"
    checkout_button = "//a[contains(@class, 'checkout-button')]"  # кнопка checkout_button
    fake = Faker("en_US")

    def checkout_page_actions(self,title_and_price):
        self.assert_url("https://test-shop.qa.studio/cart/")
        print(self.driver.title)
        self.assert_word(self.element_find(self.page_title),"Корзина")
        self.element_click(self.decrease_button)
        print("Количество товара убавляется на 1")
        self.assert_word(self.element_find(self.cart_update_message),"Cart updated.")
        print("Ожидание статуса корзины Cart updated.")

        # Проверяем изначальные названия и цену со страницы магазина
        self.assert_word(self.element_find(self.cart_product_title), title_and_price[0])
        self.assert_word(self.element_find(self.cart_product_price), title_and_price[1])
        self.assert_word(self.element_find(self.subtotal_price), title_and_price[1])
        self.assert_word(self.element_find(self.total_price), title_and_price[1])
        #
        time.sleep(3)
        self.element_click(self.calculate_shipping)
        print("Нажатие кнопки Сalculate shipping и раскрытие полей доставки")
        self.element_send_keys(self.shipping_state_input,self.fake.state())
        print("Заполняем поле State")
        self.element_send_keys(self.shipping_city_input,self.fake.city())
        print("Заполняем поле City")
        self.element_send_keys(self.shipping_postcode_input,self.fake.postalcode())
        print("Заполняем поле Postal Code")
        self.element_click(self.update_shipping_button)
        print("Нажатие кнопки Update для подсчёта доставки")
        self.assert_word(self.element_find(self.shipping_costs_updated_text), "Shipping costs updated.")
        self.get_screenshot("cart")
        self.element_click(self.checkout_button)
        print("Нажатие кнопки checkout")