import allure
import time
from config.generator import generated_address
from constants import URL, AuthData
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.checkout_delivery_page import CheckoutDeliveryPage
from pages.checkout_summary_page import CheckoutSummaryPage
from pages.login_page import LoginPage
from pages.product_listing_page import PLP
from pages.product_page import ProductPage


@allure.feature('Buy product user flow')
class TestUserFlow:
    @allure.description('Select a product on PLP and place an order as a registered user')
    def test_buy_product_as_registered_user(self, driver, check):
        address = generated_address()

        main_page = BasePage(driver, URL.BASE_URL)
        main_page.open_page()
        main_page.click_profile_icon()

        login_page = LoginPage(driver, URL.LOGIN_PAGE)
        login_page.enter_email(AuthData.LOGIN_EMAIL)
        login_page.enter_password(AuthData.LOGIN_PASSWORD)
        login_page.click_sign_in_button()
        time.sleep(2)

        account_page = AccountPage(driver, URL.ACCOUNT_PAGE)
        account_page.is_open()
        account_page.select_random_mega_menu_category()

        plp = PLP(driver, driver.current_url)
        plp_product_title, plp_product_price = plp.select_product()

        pdp = ProductPage(driver, URL.PRODUCT_PAGE)
        pdp.select_available_size()
        pdp.click_add_to_basket_button()
        pdp_product_title = pdp.get_product_title_text()
        pdp_product_size = pdp.get_product_size_text()
        pdp_product_price = pdp.get_product_price_value()
        pdp_product_color = pdp.get_product_color_text()
        mini_basket_total = pdp.get_mini_basket_total_value()
        with check:
            assert plp_product_title == pdp_product_title, 'Product name on PLP and on PDP is different'
        with check:
            assert plp_product_price == pdp_product_price, 'Product price on PLP and on PDP is different'
        pdp.click_go_to_basket_button()

        basket_page = BasketPage(driver, URL.BASKET_PAGE)
        basket_page.is_open()
        basket_product_title = basket_page.get_product_name_text()
        basket_product_color = basket_page.get_product_color_text()
        basket_product_size = basket_page.get_product_size_text()
        basket_product_price = basket_page.get_product_price_value()
        basket_total_price = basket_page.get_total_price_value()
        with check:
            assert pdp_product_title == basket_product_title, 'Product name on PDP and in Basket is different'
        with check:
            assert pdp_product_color == basket_product_color, 'Product color on PDP and in Basket is different'
        with check:
            assert pdp_product_size == basket_product_size, 'Product size on PDP and in Basket is different'
        with check:
            assert pdp_product_price == basket_product_price, 'Product price on PDP and in Basket is different'
        with check:
            assert basket_total_price == mini_basket_total, 'Total in the Basket and mini basket is different'
        basket_page.click_lower_checkout_button()

        delivery_page = CheckoutDeliveryPage(driver, URL.CHECKOUT_DELIVERY_PAGE)
        delivery_page.is_open()
        delivery_page.enter_billing_address_street(address.street)
        delivery_page.enter_billing_address_number(address.building_number)
        delivery_page.enter_billing_address_post_code(address.post_code)
        delivery_page.enter_billing_address_city(address.city)
        delivery_page.select_accept_terms_checkbox()
        delivery_page.click_go_to_summary_button()

        summary_page = CheckoutSummaryPage(driver, URL.CHECKOUT_SUMMARY_PAGE)
        summary_page.is_open()
        summary_product_title = summary_page.get_product_name_text()
        summary_product_color = summary_page.get_product_color_text()
        summary_product_size = summary_page.get_product_size_text()
        summary_product_price = summary_page.get_product_price_value()
        summary_total_price = summary_page.get_total_price_value()
        with check:
            assert basket_product_title == summary_product_title, 'Product name in Basket and in Summary is different'
        with check:
            assert basket_product_color == summary_product_color, 'Product color in Basket and in Summary is different'
        with check:
            assert basket_product_size == summary_product_size, 'Product size in Basket and in Summary is different'
        with check:
            assert basket_product_price == summary_product_price, 'Product price in Basket and in Summary is different'
        with check:
            assert basket_total_price == summary_total_price, 'Total price in Basket and in Summary is different'
        summary_page.select_card_payment_method()
        summary_page.click_go_to_payments_details_button()

        assert URL.CARD_PAYMENT_PAGE in summary_page.get_current_url(2), \
            'User is nor redirected to payment page'
