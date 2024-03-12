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


@allure.description('Test that product count and Total in the mini basket is calculated correctly for two products')
def test_add_two_products_to_mini_cart(driver):
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()
    page.select_available_size()
    page.click_add_to_basket_button()
    page.click_keep_shopping_button()
    page.select_available_size()
    page.click_add_to_basket_button()

    mini_cart_product_price = page.get_mini_basket_product_price_value()
    product_count_in_mini_basket = page.get_mini_basket_product_count_value()
    mini_basket_total = page.get_mini_basket_total_value()

    assert product_count_in_mini_basket == 2, \
        'Product count in the mini basket is not 2'
    assert mini_basket_total == mini_cart_product_price * 2, \
        'Mini basket Total is not equal to the sum of the prices'


@allure.description('Test the Size Guide link opens the size guide modal, Add Size button is present in the modal')
def test_size_guide_modal_opens(driver):
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()
    page.click_size_guide_button()
    page.assert_size_guide_modal_opens()
    page.assert_add_size_button_present_in_size_guide()


@allure.description('Test that product image changes when a different (second) color selected')
def test_image_changes_when_different_color_selected(driver):
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()

    default_image_src = page.get_product_image_src()

    page.select_second_color()
    current_image_src = page.get_product_image_src()

    assert current_image_src != default_image_src, \
        'Product Image  is not changed after selecting a different color'


@allure.description(
    'Test that Favorites count value is correct and Add to favorites tooltip appears/disappears when adding a product '
    'to favorites as a guest'
)
def test_add_to_favorites(driver):
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()

    page.click_add_to_favorites_button()

    page.assert_favourites_icon_count_present()
    favorites_count_value = page.get_favorites_icon_count_value()

    page.assert_add_to_favorites_tooltip_appears()
    page.move_mouse_to_right()
    page.assert_add_to_favorites_tooltip_disappears()
    assert favorites_count_value == 1, \
        'Favorites count value is not equal to 1 after adding one product to favorites'
