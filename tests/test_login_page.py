import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from constants import URL, LoginAlerts, AuthData


@allure.suite('Login')
@allure.description('Test login with email (Happy path)')
def test_login_with_email(driver):
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(AuthData.LOGIN_EMAIL)
    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_sign_in_button()

    account_page = AccountPage(driver, driver.current_url)
    assert page.get_current_url() == URL.ACCOUNT_PAGE, \
        'Account URL is not correct, probably user is not logged in'
    account_page.assert_greeting_title_is_present()


@allure.suite('Login')
@allure.description('Test login with empty email field')
@allure.tag('negative')
def test_login_with_empty_email(driver):
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_sign_in_button()

    alert_text = page.get_email_alert_text()
    assert alert_text == LoginAlerts.EMPTY_EMAIL_ALERT, \
        'Empty email alert text is not correct'


@allure.suite('Login')
@allure.description('Test login with empty password field')
@allure.tag('negative')
def test_login_with_empty_password(driver):
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(AuthData.LOGIN_EMAIL)
    page.click_sign_in_button()

    alert_text = page.get_password_alert_text()
    assert alert_text == LoginAlerts.EMPTY_PASSWORD_ALERT, \
        'Empty password alert text is not correct'


@allure.suite('Login')
@allure.description('Test login with_incorrect email format')
@allure.tag('negative')
def test_login_with_incorrect_email_format(driver):
    email = 'www_mail.com'

    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(email)
    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_sign_in_button()

    alert_text = page.get_email_alert_text()
    assert alert_text == LoginAlerts.INCORRECT_EMAIL_FORMAT_ALERT, \
        'Incorrect email format alert is not correct'


@allure.suite('Login')
@allure.description('Test login with email not registered as account')
@allure.tag('negative')
def test_login_with_unregistered_email(driver):
    email = 'w123www$@mail.com'

    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(email)
    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_sign_in_button()

    alert_text = page.get_email_alert_text()
    assert alert_text == LoginAlerts.LOGIN_FAILED, \
        'Failed login alert is not correct'


@allure.suite('Login')
@allure.description('Test Show/Hide password function')
def test_show_hide_password(driver):
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_show_password_button()

    page.assert_password_is_not_masked()
    page.assert_show_password_button_changed_to_hide()

    page.click_hide_password_button()

    page.assert_password_is_masked()
    page.assert_hide_password_button_changed_to_show()
