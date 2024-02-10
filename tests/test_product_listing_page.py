import allure
from pages.product_listing_page import PLP
from constants import URL


@allure.description('Test that sorting by price asc/desc is correct')
def test_sorting_by_price(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()

    page.click_sort_by()
    page.click_sort_by_price_asc()
    price_list = page.get_price_list()
    assert price_list == sorted(price_list), \
        'Sorting by price asc is not correct'
    page.click_sort_by()
    page.click_sort_by_price_desc()
    price_list = page.get_price_list()
    assert price_list == sorted(price_list, reverse=True), \
        'Sorting by price desc is not correct'


@allure.description(
    'Test that product total and color name in selected filter are correct after applying the color filter'
)
def test_apply_color_filter(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()

    page.click_color_filter()
    color_name = page.get_color_name_text_in_dropdown()
    color_amount = page.get_amount_value_in_color_dropdown()
    page.select_color()
    filtered_products_count = page.get_total_products_value()
    color_name_in_selected_filter = page.get_selected_filter_text()

    assert filtered_products_count == color_amount, \
        'Product total total is not correct after applying the color filter'
    assert color_name_in_selected_filter == color_name, \
        'Color name in selected filter does not match the selected color'


@allure.description('Test that Clear All button resets the filters')
def test_clear_all_button(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()

    unfiltered_products_count = page.get_total_products_value()
    page.click_color_filter()
    page.select_color()
    filtered_products_count = page.get_total_products_value()

    assert filtered_products_count < unfiltered_products_count, \
        'The same amount of filtered and unfiltered products'
    page.click_clear_all_button()
    products_count_after_resetting_filters = page.get_total_products_value()

    assert products_count_after_resetting_filters == unfiltered_products_count, \
        'The number of products after reset the filters does not match the number of unfiltered products'


@allure.description('Test Back to Top button')
def test_back_to_top_button(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()

    page.scroll_down_two_screen()
    page.assert_back_to_top_button_appears()
    page.click_back_to_top_button()
    page.assert_back_to_top_button_disappears()
    page.assert_page_scrolled_to_top()


@allure.description('Test price slider changes the min and max price')
def test_price_slider(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()
    page.click_price_filter()

    min_price_by_default = page.get_min_price_value_in_price_range()
    max_price_by_default = page.get_max_price_value_in_price_range()

    page.set_min_price()
    page.set_max_price()

    min_price = page.get_min_price_value_in_price_range()
    max_price = page.get_max_price_value_in_price_range()

    assert min_price_by_default < min_price, \
        'Price range is not changed after moving the min price slider'
    assert max_price_by_default > max_price, \
        'Price range is not changed after moving the max price slider'


@allure.description('Test that filtering by min and max price is correct')
def test_price_filter(driver):
    page = PLP(driver, URL.PLP)
    page.open_page()

    page.click_price_filter()
    page.set_min_price()
    page.set_max_price()

    min_price = page.get_min_price_value_in_price_range()
    max_price = page.get_max_price_value_in_price_range()

    page.click_sort_by()
    page.click_sort_by_price_asc()

    first_product_price = page.get_first_product_price()

    assert first_product_price >= min_price, \
        'The min price on PLP does not match the min price filter'

    page.click_sort_by()
    page.click_sort_by_price_desc()

    first_product_price = page.get_first_product_price()

    assert first_product_price <= max_price, \
        'The max price on PLP does not match the max price filter'
