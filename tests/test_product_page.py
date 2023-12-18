import time
import allure
from pages.product_page import ProductPage
from constants import URL


@allure.description(
    'Test that title, size, color and price of product added to cart on PDP and in the mini cart are the same'
)
def test_add_product_to_mini_cart(driver):
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()
    page.select_available_size()
    page.click_add_to_basket_button()

    pdp_product_title = page.get_product_title_text()
    pdp_product_size = page.get_product_size_text()
    pdp_product_price = page.get_product_price_value()
    pdp_product_color = page.get_product_color_text()
    mini_cart_product_title = page.get_mini_basket_product_title_text()
    mini_cart_product_size = page.get_mini_basket_product_size_text()
    mini_cart_product_price = page.get_mini_basket_product_price_value()
    mini_cart_product_color = page.get_mini_basket_product_color_text()
    mini_cart_total = page.get_mini_basket_total_value()

    assert pdp_product_title == mini_cart_product_title, \
        'Product name on PDP and in the mini cart is different'
    assert pdp_product_size == mini_cart_product_size, \
        'Product size on PDP and in the mini cart is different'
    assert pdp_product_price == mini_cart_product_price, \
        'Product price on PDP and in the mini cart is different'
    assert pdp_product_color == mini_cart_product_color, \
        'Product color on PDP and in the mini cart is different'
    assert mini_cart_total == mini_cart_product_price, \
        'Total in the mini cart and product price are different'
