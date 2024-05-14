import allure
from faker import Faker
from pages.checkout_delivery_page import CheckoutDeliveryPage
from pages.checkout_summary_page import CheckoutSummaryPage
from constants import URL, CheckoutDeliveryAlerts, CheckoutSummaryAlerts


@allure.description('Unable to go from Delivery to Summary page without filling the billing address')
@allure.tag('negative')
def test_go_to_summary_with_empty_address(driver, check, login, go_to_checkout_delivery):
    page = CheckoutDeliveryPage(driver, URL.CHECKOUT_DELIVERY_PAGE)

    page.click_go_to_summary_button()

    with check:
        assert page.get_billing_street_error_text() == CheckoutDeliveryAlerts.EMPTY_STREET_ALERT
    with check:
        assert page.get_billing_number_error_text() == CheckoutDeliveryAlerts.EMPTY_NUMBER_ALERT
    with check:
        assert page.get_billing_post_code_error_text() == CheckoutDeliveryAlerts.EMPTY_POST_CODE_ALERT
    with check:
        assert page.get_billing_city_error_text() == CheckoutDeliveryAlerts.EMPTY_CITY_ALERT


@allure.description('Billing address added on checkout/delivery page is displayed correctly on checkout/summary page')
def test_add_billing_address(driver, check, login, go_to_checkout_delivery):
    fake = Faker('en_GB')
    street = fake.street_name()
    number = fake.building_number()
    post_code = fake.postcode()
    city = fake.city()
    delivery_page = CheckoutDeliveryPage(driver, URL.CHECKOUT_DELIVERY_PAGE)

    delivery_page.enter_billing_address_street(street)
    delivery_page.enter_billing_address_number(number)
    delivery_page.enter_billing_address_post_code(post_code)
    delivery_page.enter_billing_address_city(city)
    delivery_page.click_go_to_summary_button()

    assert delivery_page.get_current_url() == URL.CHECKOUT_SUMMARY_PAGE, \
        'Go to Summary button does not lead to checkout/summary page'

    summary_page = CheckoutSummaryPage(driver, driver.current_url)

    summary_address = summary_page.get_billing_address_text()
    summary_postal_code = summary_page.get_billing_postal_code_text()

    with check:
        assert summary_address == f'{street} {number}', \
            'Check the street and the building number on the checkout/summary page'
    with check:
        assert summary_postal_code == f'{post_code} {city}', \
            'Check the post code and city on the checkout/summary page'


@allure.description('Can edit billing address on the checkout/delivery page')
def test_edit_billing_address(driver, check, login, go_to_checkout_delivery):
    fake = Faker('en_GB')
    street = fake.street_name()
    number = fake.building_number()
    post_code = fake.postcode()
    city = fake.city()
    delivery_page = CheckoutDeliveryPage(driver, URL.CHECKOUT_DELIVERY_PAGE)

    delivery_page.enter_billing_address()
    delivery_page.click_go_to_summary_button()

    summary_page = CheckoutSummaryPage(driver, driver.current_url)

    summary_page.click_change_billing_address_link()

    assert summary_page.get_current_url() == URL.CHECKOUT_DELIVERY_PAGE, \
        'Change billing address link does not lead to checkout/delivery page'

    delivery_page.clear_billing_address_street()
    delivery_page.clear_billing_address_number()
    delivery_page.clear_billing_address_post_code()
    delivery_page.clear_billing_address_city()
    delivery_page.enter_billing_address_street(street)
    delivery_page.enter_billing_address_number(number)
    delivery_page.enter_billing_address_post_code(post_code)
    delivery_page.enter_billing_address_city(city)
    delivery_page.click_go_to_summary_button()

    edited_summary_address = summary_page.get_billing_address_text()
    edited_summary_postal_code = summary_page.get_billing_postal_code_text()

    with check:
        assert edited_summary_address == f'{street} {number}', \
            'Check the street and the building number on the checkout/summary page'
    with check:
        assert edited_summary_postal_code == f'{post_code} {city}', \
            'Check the post code and city on the checkout/summary page'


@allure.description('Unable to go to payment page without accepting terms on the checkout/summary page')
@allure.tag('negative')
def test_go_to_payment_without_accepting_terms(driver, check, login, go_to_checkout_summary):
    page = CheckoutSummaryPage(driver, URL.CHECKOUT_SUMMARY_PAGE)

    page.select_card_payment_method()
    page.click_go_to_payments_details_button()

    assert page.get_accept_consent_error() == CheckoutSummaryAlerts.ACCEPT_CONSENT_ALERT, \
        'Accept consent error text is not correct'


@allure.description('Terms and conditions modal can be open and closed on Summary page, modal title text is correct')
def test_terms_and_conditions_modal(driver, check, login, go_to_checkout_summary):
    terms_and_conditions_title_text = 'Terms of Use'
    page = CheckoutSummaryPage(driver, URL.CHECKOUT_SUMMARY_PAGE)

    page.click_terms_and_conditions_link()

    page.assert_consent_modal_opens()
    with check:
        page.assert_consent_modal_title_is_present()
        assert page.get_consent_modal_title_text() == terms_and_conditions_title_text, \
            'Terms and conditions title text is not correct'
    page.click_close_consent_modal_icon()
    page.assert_consent_modal_closed()


@allure.description('Privacy policy modal can be open and closed on the Summary page, modal title text is correct')
def test_privacy_policy_modal(driver, check, login, go_to_checkout_summary):
    privacy_policy_title_text = 'Privacy Policy'
    page = CheckoutSummaryPage(driver, URL.CHECKOUT_SUMMARY_PAGE)

    page.click_accept_privacy_policy_link()

    page.assert_consent_modal_opens()
    with check:
        page.assert_consent_modal_title_is_present()
        assert page.get_consent_modal_title_text() == privacy_policy_title_text, \
            'Privacy policy title text is not correct'
    page.click_close_consent_modal_icon()
    page.assert_consent_modal_closed()
