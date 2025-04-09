import pytest

from pages.cart_page import Cart_page
from pages.delivery_info_page import Delivery_info_page
from pages.finish_page import Finish_page
from pages.main_page import Main_Page


def test_buy_product(set_up, driver):

    # login = Login_page(driver)
    # login.authorization()

    mp = Main_Page(driver)
    mp.open_main_page()
    mp.select_product()
    #
    cp = Cart_page(driver)
    cp.checkout_page_actions(mp.get_title_and_price())
    #
    cip = Delivery_info_page(driver)
    cip.fill_delivery_page(mp.get_title_and_price())
    #
    f = Finish_page(driver)
    f.finish(mp.get_title_and_price())