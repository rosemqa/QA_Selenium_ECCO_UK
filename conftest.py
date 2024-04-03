import time

import pytest
from faker import Faker
from selenium import webdriver
from constants import URL, AuthData
from locators import AccountPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    print('\nStart Chrome browser')
    driver.maximize_window()
    yield driver
    driver.quit()
    print('\nQuit browser')


@pytest.fixture()
def login(driver):
    """Login to account"""
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(AuthData.LOGIN_EMAIL)
    page.enter_password(AuthData.LOGIN_PASSWORD)
    page.click_sign_in_button()
    time.sleep(1)


@pytest.fixture()
def add_billing_address(driver):
    """Add the billing address on the Address Book page if address not added yet"""
    page = AccountPage(driver, URL.BILLING_ADDRESS_BOOK_PAGE)
    page.open_page()
    if page.is_element_present(AccountPageLocators.ADD_ADDRESS_BTN):
        faker = Faker('en_GB')
        street = faker.street_name()
        house_number = faker.building_number()
        post_code = faker.postcode()
        city = faker.city()

        page.click_add_address_button()
        page.enter_billing_address_street(street)
        page.enter_billing_address_number(house_number)
        page.enter_billing_address_post_code(post_code)
        page.enter_billing_address_city(city)
        page.click_save_billing_address_button()


@pytest.fixture()
def delete_billing_address(driver):
    """Delete the billing address on the Address Book page after the test"""
    yield
    page = AccountPage(driver, URL.BILLING_ADDRESS_BOOK_PAGE)
    page.open_page()
    page.click_delete_address_button()
    page.confirm_address_deletion()
