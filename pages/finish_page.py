import time
from base.base_class import Base

class Finish_page(Base):

    page_title = "//h1[@class='page-header__title ']"
    status = "//div[@class='order-title' and text()= 'Status:']/../span"
    order_amount = "//div[@class='order-title']/../span/span"
    text_1 = "//*[contains(text(),'Оплата наличными при доставке заказа.')]"
    delivery_product_title = "//div[@class = 'product-content']/a"
    delivery_product_price = "//td[@class='product-total']//bdi"
    subtotal_price = "//th[text()='Subtotal:']/../td"
    total_price = "//th[text()='Total:']/../td"
    shipping  = "//th[text()='Shipping:']/../td"
    payment_method = "//th[text()='Payment method:']/../td"


    # Actions
    def finish(self, product_title_and_price):
        self.assert_word(self.element_find(self.page_title), "Оформение заказа")
        self.assert_word(self.element_find(self.text_1), "Оплата наличными при доставке заказа.")
        self.assert_word(self.element_find(self.status), 'Processing')

        print("Начинаем проверять название продукта")
        self.assert_word(self.element_find(self.delivery_product_title), product_title_and_price[0])
        print("Начинаем проверять сумму в заказе")
        self.assert_word(self.element_find(self.order_amount), product_title_and_price[1])
        print("Начинаем проверять цену в subtotal")
        self.assert_word(self.element_find(self.subtotal_price), product_title_and_price[1])
        self.assert_word(self.element_find(self.shipping), 'Free shipping')
        self.assert_word(self.element_find(self.payment_method), 'Оплата при доставке')
        print("Начинаем проверять цену в total")
        self.assert_word(self.element_find(self.total_price), product_title_and_price[1])


        # Оформение заказа
        # Thank you. Your order has been received.
        # Оплата наличными при доставке заказа.
        self.get_screenshot("finish")