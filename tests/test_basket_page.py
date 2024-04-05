import allure
from pages.basket_page import BasketPage
from constants import URL, Basket


@allure.description('Test that a product can be deleted from the basket')
def test_delete_product_from_basket(driver, check, add_product_to_basket):
    page = BasketPage(driver, URL.BASKET_PAGE)

    page.click_remove_button()

    with check:
        page.assert_continue_shopping_button_is_present()
    with check:
        assert page.get_empty_basket_message_text() == Basket.EMPTY_BASKET_MSG, \
            'Empty basket message is not correct'
    with check:
        page.assert_basket_icon_count_is_missing()


@allure.description('Test that pickup store can be selected, Choose store button changes to Change store')
def test_choose_pickup_store(driver, check, add_product_to_basket):
    page = BasketPage(driver, URL.BASKET_PAGE)

    page.select_click_and_collect_delivery()

    with check:
        assert page.get_choose_store_button_text() == Basket.CHOOSE_STORE_BTN_TEXT, \
            'Choose store button text is not correct'

    page.click_choose_store_button()
    page.click_select_store_button_in_modal()

    with check:
        assert page.get_pickup_store_name_text() == page.get_modal_pickup_store_name(), \
            'Store name in the Click & Collect section is not equal to selected store name'

    page.refresh_page()

    with check:
        assert page.get_choose_store_button_text() == Basket.CHANGE_STORE_BTN_TEXT, \
            'Change store button text is not correct'


@allure.description('Check error messages for empty and not valid voucher code')
@allure.tag('negative')
def test_redeem_empty_code(driver, check, add_product_to_basket):
    voucher_code = 123
    page = BasketPage(driver, URL.BASKET_PAGE)

    page.click_redeem_button()

    with check:
        assert page.get_voucher_code_error() == Basket.EMPTY_VOUCHER_CODE_MSG, \
            'Empty voucher code message is not correct'

    page.enter_voucher_code(voucher_code)
    page.click_redeem_button()

    with check:
        assert page.get_voucher_code_error() == Basket.NOT_VALID_VOUCHER_CODE_MSG, \
            'Not valid voucher code message is not correct'


@allure.description('That that product tittle (link) leads to relevant PDP')
def test_product_link_leads_to_pdp(driver, add_product_to_basket):
    page = BasketPage(driver, URL.BASKET_PAGE)

    page.click_product_title()

    assert page.get_current_url() == URL.PRODUCT_PAGE, \
        'Product title link does not lead to relevant product page '


@allure.description('Teat that Continue shopping button in the empty basket leads to the home page')
def test_continue_shopping_leads_to_home_page(driver):
    page = BasketPage(driver, URL.BASKET_PAGE)
    page.open_page()

    page.click_continue_shopping_button()

    assert page.get_current_url() == URL.BASE_URL, \
        "Continue shopping button does not lead to the home page"
