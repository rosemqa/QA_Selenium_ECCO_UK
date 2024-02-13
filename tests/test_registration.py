import allure
from pages.registration_page import RegistrationPage
from pages.account_page import AccountPage
from constants import URL, RegistrationAlerts
from faker import Faker


@allure.suite('Registration')
@allure.description('Test register a new user (Happy path)')
@allure.tag('positive')
def test_registration(driver):
    fake = Faker('en_US')
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()

    page = RegistrationPage(driver, URL.REGISTER_PAGE)
    page.open_page()

    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_email(email)
    page.enter_password(password)
    page.confirm_password(password)
    page.select_male_gender()
    page.accept_terms()
    # page.click_create_account_button()
    account_page = AccountPage(driver, driver.current_url)
    greeting_title_text = account_page.get_greeting_title_text()

    assert first_name in greeting_title_text, \
        'First name in the greeting title is not correct'
    assert driver.current_url == URL.ACCOUNT_PAGE, \
        'Account URL is not correct'


@allure.suite('Registration')
@allure.description('Test alert text for empty fields')
@allure.tag('negative')
def test_registration_with_empty_fields(driver):
    page = RegistrationPage(driver, URL.REGISTER_PAGE)
    page.open_page()
    page.click_create_account_button()

    assert page.get_first_name_alert_text() == RegistrationAlerts.EMPTY_FIRSTNAME_ALERT, \
        'Alert text for empty first name field is not correct'
    assert page.get_last_name_alert_text() == RegistrationAlerts.EMPTY_LASTNAME_ALERT, \
        'Alert text for empty last name field is not correct'
    assert page.get_email_alert_text() == RegistrationAlerts.EMPTY_EMAIL_ALERT, \
        'Alert text for empty email field is not correct'
    assert page.get_password_alert_text() == RegistrationAlerts.EMPTY_PASSWORD_ALERT, \
        'Alert text for empty password field is not correct'
    assert page.get_confirm_password_alert_text() == RegistrationAlerts.CONFIRM_PASSWORD_ALERT, \
        'Alert text for empty confirm password field is not correct'
    assert page.get_accept_terms_alert_text() == RegistrationAlerts.ACCEPT_TERMS_ALERT, \
        'Alert text if terms not accepted is not correct'


@allure.suite('Registration')
@allure.description('Test alert text for fields with incorrect data format')
@allure.tag('negative')
def test_alert_text_for_incorrect_data_format(driver):
    page = RegistrationPage(driver, URL.REGISTER_PAGE)
    page.open_page()

    incorrect_email_format = 'www.mail.com'
    incorrect_password_format = '123456'

    page.enter_email(incorrect_email_format)
    page.enter_password(incorrect_password_format)
    page.click_create_account_button()

    assert page.get_email_alert_text() == RegistrationAlerts.INCORRECT_EMAIL_FORMAT_ALERT, \
        'Alert text for incorrect email format is not correct'
    assert page.get_password_alert_text() == RegistrationAlerts.INCORRECT_PASSWORD_FORMAT_ALERT, \
        'Alert text for incorrect password format is not correct'


@allure.suite('Registration')
@allure.description('Test alert text for too short password')
@allure.tag('negative')
def test_alert_text_for_short_password(driver):
    page = RegistrationPage(driver, URL.REGISTER_PAGE)
    page.open_page()

    short_password = '123a'

    page.enter_password(short_password)
    page.click_create_account_button()

    assert page.get_password_alert_text() == RegistrationAlerts.SHORT_PASSWORT_ALERT, \
        'Alert text for too short password is not correct'


@allure.suite('Registration')
@allure.description('Test that "here" link opens the terms window')
def test_terms_link(driver):
    page = RegistrationPage(driver, URL.REGISTER_PAGE)
    page.open_page()

    page.click_terms_link()
    page.assert_terms_window_is_present()
