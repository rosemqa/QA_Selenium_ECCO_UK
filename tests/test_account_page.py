import allure
import pytest
from faker import Faker
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from constants import URL, AuthData, AccountAlerts


@allure.epic('Account pages cases')
class TestAccountPage:
    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Precondition: login to account """
        page = LoginPage(driver, URL.LOGIN_PAGE)
        page.open_page()

        page.enter_email(AuthData.LOGIN_EMAIL)
        page.enter_password(AuthData.LOGIN_PASSWORD)
        page.click_sign_in_button()
        account_page = AccountPage(driver, URL.ACCOUNT_PAGE)
        account_page.is_open()

    @allure.description('Test if the user can log out')
    def test_sign_out(self, driver):
        page = AccountPage(driver, URL.ACCOUNT_PAGE)
        page.click_sign_out_button()

        login_page = LoginPage(driver, driver.current_url)
        login_page.assert_sign_in_btn_is_present()
        assert URL.LOGIN_PAGE in login_page.get_current_url(), \
            'User is not redirected to login page URL'

    @allure.description('Test if the date displayed in the data picker matches the selected date')
    def test_date_picker(self, driver):
        default_day = 'dd'

        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        day_initial_value = page.get_date_picker_day_value()

        if day_initial_value != default_day:
            page.click_day_picker()
            page.select_random_day()
            page.click_month_picker()
            page.select_random_month()
            page.click_year_picker()
            page.select_random_year()
        else:
            page.click_day_picker()
            page.select_random_day()
            page.select_random_month()
            page.select_random_year()

        selected_day = page.get_day_to_choose_in_days_dropdown()
        selected_moth = page.get_month_to_choose_in_months_dropdown()
        selected_year = page.get_year_to_choose_in_years_dropdown()

        date_picker_day = page.get_date_picker_day_value()
        date_picker_month = page.get_date_picker_month_value()
        date_picker_year = page.get_date_picker_year_value()
        assert date_picker_day == selected_day, \
            'The day displayed in the date picker does not match the selected day'
        assert date_picker_month == selected_moth, \
            'The month displayed in the date picker does not match the selected month'
        assert date_picker_year == selected_year, \
            'The year displayed in the date picker does not match the selected year'

    @allure.description('Test if date in the data picker can be cleared')
    def test_clear_date_picker(self, driver):
        default_day = 'dd'
        default_month = 'mm'
        default_year = 'yyyy'

        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        day_initial_value = page.get_date_picker_day_value()

        if day_initial_value != default_day:
            page.click_day_picker()
            page.select_random_day()
            page.click_month_picker()
            page.select_random_month()
            page.click_year_picker()
            page.select_random_year()
        else:
            page.click_day_picker()
            page.select_random_day()
            page.select_random_month()
            page.select_random_year()

        page.click_clear_link()

        assert page.get_date_picker_day_value() == default_day, \
            'Picker day value is not cleared'
        assert page.get_date_picker_month_value() == default_month, \
            'Picker month value is not cleared'
        assert page.get_date_picker_year_value() == default_year, \
            'Picker year value is not cleared'

    @allure.description('Test if user data can be saved on the Edit page')
    def test_save_user_data(self, driver, check):
        fake = Faker('en_GB')
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        phone_number = str(fake.random_number(digits=11))

        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        page.clear_first_name_field()
        page.enter_first_name(first_name)
        page.clear_last_name_field()
        page.enter_last_name(last_name)
        page.clear_phone_number_field()
        page.enter_phone_number(phone_number)
        page.click_clear_link()
        page.click_day_picker()
        page.select_random_day()
        page.select_random_month()
        page.select_random_year()

        selected_day = page.get_date_picker_day_value()
        selected_month = page.get_date_picker_month_value()
        selected_year = page.get_date_picker_year_value()

        page.click_save_user_details_button()
        page.refresh_page()
        with check:
            assert page.get_first_name_text() == first_name, \
                'First name is not saved on the edit page'
        with check:
            assert page.get_last_name_text() == last_name, \
                'Last name is not saved on the edit page'
        with check:
            assert page.get_phone_number_value() == phone_number, \
                'Phone number is not saved on the edit page'
        with check:
            assert page.get_date_picker_day_value() == selected_day, \
                'Day is not saved on the edit page'
        with check:
            assert page.get_date_picker_month_value() == selected_month, \
                'Month is not saved on the edit page'
        with check:
            assert page.get_date_picker_year_value() == selected_year, \
                'Year is not saved on the edit page'

    @allure.description('Test if info message appears/disappears after updating the user info')
    def test_updated_user_info_message(self, driver):
        fake = Faker('en_GB')
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        phone_number = str(fake.random_number(digits=11))

        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        page.clear_first_name_field()
        page.enter_first_name(first_name)
        page.clear_last_name_field()
        page.enter_last_name(last_name)
        page.clear_phone_number_field()
        page.enter_phone_number(phone_number)
        page.click_save_user_details_button()

        assert page.get_updated_user_info_text() == AccountAlerts.UPDATED_INFO_TEXT, \
            'Updated user info text is not correct'
        page.assert_updated_info_msg_disappears()

    @allure.description('Test edit user info with empty fields')
    @allure.tag('negative')
    def test_edit_with_empty_fields(self, driver):
        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        page.clear_first_name_field()
        page.clear_last_name_field()
        page.clear_email_field()
        page.clear_phone_number_field()
        page.click_save_user_details_button()

        assert page.get_first_name_alert_text() == AccountAlerts.EDIT_EMPTY_FIRSTNAME_ALERT, \
            'Empty first name alert text is not correct'
        assert page.get_last_name_alert_text() == AccountAlerts.EDIT_EMPTY_LASTNAME_ALERT, \
            'Empty last name alert text is not correct'
        assert page.get_email_alert_text() == AccountAlerts.EDIT_EMPTY_EMAIL_ALERT, \
            'Empty email alert text is not correct'
        assert page.get_phone_number_alert_text() == AccountAlerts.EDIT_EMPTY_PHONE_NUMBER_ALERT, \
            'Empty phone number alert text is not correct'

    @allure.description('Test edit user info with incorrect email format and phone number not in numbers')
    @allure.tag('negative')
    def test_edit_with_incorrect_format(self, driver):
        email = 'www.com'
        phone_number = 'wwwwwwww123'
        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        page.clear_email_field()
        page.enter_email(email)
        page.clear_phone_number_field()
        page.enter_phone_number(phone_number)
        page.click_save_user_details_button()

        assert page.get_email_alert_text() == AccountAlerts.EDIT_INCORRECT_EMAIL_FORMAT_ALERT, \
            'Incorrect email format alert is not correct'
        assert page.get_phone_number_alert_text() == AccountAlerts.EDIT_INCORRECT_PHONE_NUMBER_FORMAT_ALERT, \
            'Incorrect phone number format alert is not correct'

    @allure.description('Test edit user info with incorrect phone number length')
    @allure.tag('negative')
    def test_edit_with_incorrect_phone_number_length(self, driver):
        phone_number = '123456'
        page = AccountPage(driver, URL.EDIT_USER_PAGE)
        page.open_page()

        page.clear_phone_number_field()
        page.enter_phone_number(phone_number)
        page.click_save_user_details_button()

        assert page.get_phone_number_alert_text() == AccountAlerts.EDIT_INCORRECT_PHONE_NUMBER_LENGTH_ALERT, \
            'Incorrect phone number length alert is not correct'
