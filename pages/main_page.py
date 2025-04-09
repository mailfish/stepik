import time
from base.base_class import Base


class Main_Page(Base):


    # Locators
    select_filter = "//span[@class='text-filter']" # Фильтр товаров
    select_category = "//span[@class='products-filter__filter-name filter-name' and text() = 'Категория']" # Фильтр категория
    products_filter_option_sofa = "//span[@class='products-filter__option-name name' and text() = 'Диваны']" # Галочка "диваны"
    select_category_brand = "//span[@class='products-filter__filter-name filter-name' and text() = 'Бренды']"  # Фильтр Бренды
    products_filter_option_brand = "//span[@class='products-filter__option-name name' and text() = 'Balmain']" # Галочка название бренда "Balmain"
    accept_filter_btn = "//button[@value='Filter']"  # Применить фильтр
    product_card = "//img[@class ='attachment-woocommerce_thumbnail size-woocommerce_thumbnail']" # Карточка товара для навигации на него и подсвечивания скрытых элементов
    product_card_title = "//h2[@class='woocommerce-loop-product__title']"
    product_card_price = "//span[@class='woocommerce-Price-amount amount']"
    add_to_cart = "//span[@class='add-to-cart-text loop_button-text']/../../a"  # Кнопка Добавить товар в корзину
    increase_button = "//span[contains(@class,'increase')]" #кнопка плюсик, для добавления количества товара
    cart_btn = "//a[@class ='button wc-forward razzi-button']"  # Кнопка Корзина
    logo_text = "//span[@class ='logo-dark']"
    product_title = ()
    product_price = ()

    def open_main_page(self):
        url = 'https://test-shop.qa.studio/'
        self.driver.get(url)
        self.driver.maximize_window()

    #Methods
    def select_product(self):
        # Работа со страницей
        print(self.driver.title)
        assert 'https://test-shop.qa.studio/' == self.driver.current_url
        assert self.element_find(self.logo_text).text == 'QA Studio', "Текст страницы не совпадает"

        # Фильтр товаров
        self.element_click(self.select_filter)
        print("Раскрываем Фильтр")
        self.element_is_displayed(self.select_category)
        print("Пpоверяем отображение элемента Категория")
        self.element_click(self.select_category)
        print("Раскрываем фильтр Категория")
        self.element_click(self.products_filter_option_sofa)
        print("Ставим галочка Диваны")
        self.element_is_displayed(self.select_category_brand)
        self.element_click(self.select_category_brand)
        print("Раскрываем Фильтр Бренды")
        self.element_click(self.products_filter_option_brand)
        print("Ставим галочка Balmain")
        self.element_click(self.accept_filter_btn)
        print("Клик на кнопке Filter")      # применяем фильтр

        # Работа с элементом товара
        self.product_title = self.element_text(self.product_card_title)  # Получаем название товара с титульной страницы
        self.product_price = self.element_text(self.product_card_price)  # Получаем цену товара с титульной страницы
        self.move_to_element(self.product_card)
        print("Навигируемся на товар для появления элемента 'Добавить в корзину'")
        self.element_click(self.add_to_cart)
        print("Клик на кнопку добавить в корзину")
        self.element_click(self.increase_button)
        print("Клик на количество товаров +1")
        self.get_screenshot("main_page")    #Делаем скриншот
        self.element_click(self.cart_btn)
        print("Клик на кнопку View Cart")

    def get_title_and_price(self):
        return (self.product_title, self.product_price)