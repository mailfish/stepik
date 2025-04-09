import time

from faker import Faker
from base.base_class import Base


class Delivery_info_page(Base):

    # Locators
    first_name = "//input[@id='billing_first_name']"
    last_name = "//input[@id='billing_last_name']"
    billing_address = "//input[@id='billing_address_1']"
    billing_phone = "//input[@id='billing_phone']"
    billing_email = "//input[@id='billing_email']"
    order_comments = "//textarea[@id='order_comments']"
    place_order_btn = "//button[@id='place_order']"
    delivery_product_title = "//span[@class = 'product-name']"
    delivery_product_price = "//td[@class='product-total']//bdi"
    subtotal_price = "//tr[@class='cart-subtotal']//bdi"
    total_price = "//tr[@class='order-total']//bdi"
    text_1 = "//div[@class='payment_box payment_method_cod']"

    page_title = "//h1[@class='page-header__title ']"
    #
    fake = Faker("en_US")


    # Actions
    def fill_delivery_page(self,title_and_price):
        #
        self.assert_url("https://test-shop.qa.studio/checkout/")
        self.assert_word(self.element_find(self.page_title),"Оформение заказа")
        time.sleep(2)
        self.assert_word(self.element_find(self.text_1),"Оплата наличными при доставке заказа.")

        # Проверяем изначальные названия и цену со страницы магазина
        time.sleep(2)
        self.assert_word(self.element_find(self.delivery_product_title), title_and_price[0])
        self.assert_word(self.element_find(self.delivery_product_price), title_and_price[1])
        self.assert_word(self.element_find(self.subtotal_price), title_and_price[1])
        self.assert_word(self.element_find(self.total_price), title_and_price[1])

        #Заполняем поля
        self.element_send_keys(self.first_name,self.fake.first_name())
        self.element_send_keys(self.last_name,self.fake.last_name())
        self.element_send_keys(self.billing_address,self.fake.address())
        self.element_send_keys(self.order_comments,"Billing comment")
        self.element_send_keys(self.billing_phone,self.fake.basic_phone_number())
        self.element_send_keys(self.billing_email,self.fake.email())

        #Делаем скрин
        self.get_screenshot("checkout")
        # Кликаем Place Order кнопку
        time.sleep(2)
        self.element_click(self.place_order_btn)
        print("# Кликаем Place Order кнопку")