from datetime import datetime
import allure
import pytest
from faker import Faker
from selenium import webdriver
from constants import URL, AuthData
from locators import AccountPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.checkout_delivery_page import CheckoutDeliveryPage


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome, firefox or edge'
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption('--browser_name')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--headless=new')

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")
    firefox_options.add_argument("--disable-dev-shm-usage")
    # firefox_options.add_argument('--width=1920')
    # firefox_options.add_argument('--height=1080')
    firefox_options.add_argument('--headless')

    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument('--window-size=1920,1080')
    # edge_options.add_argument("--start-maximized")
    # edge_options.add_argument("--window-position=1367,0")
    edge_options.add_argument('--headless=new')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        print('\nStart Chrome browser')
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=firefox_options)
        print('\nStart Firefox browser')
        driver.set_window_size(1920, 1080)
        # driver.maximize_window()
    elif browser_name == 'edge':
        driver = webdriver.Edge(options=edge_options)
        print('\nStart Edge browser')
    else:
        raise pytest.UsageError('--browser_name should be chrome, firefox or edge')
    yield driver
    attachment = driver.get_screenshot_as_png()
    allure.attach(attachment, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
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
    account_page = AccountPage(driver, URL.ACCOUNT_PAGE)
    account_page.is_open()


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


@pytest.fixture()
def add_product_to_basket(driver):
    """Add product to the basket from PDP and go to the basket"""
    page = ProductPage(driver, URL.PRODUCT_PAGE)
    page.open_page()
    page.is_open()
    page.select_available_size()
    page.click_add_to_basket_button()
    page.click_go_to_basket_button()


@pytest.fixture()
def go_to_checkout_delivery(driver, add_product_to_basket):
    """Add product to the basket from PDP, go to the basket, go to Checkout/Delivery page"""
    page = BasketPage(driver, driver.current_url)
    page.click_lower_checkout_button()


@pytest.fixture()
def go_to_checkout_summary(driver, go_to_checkout_delivery):
    """As a user enter billing address on the Checkout/Delivery page and go to Checkout/Summary page"""
    page = CheckoutDeliveryPage(driver, driver.current_url)
    page.enter_billing_address()
    page.select_accept_terms_checkbox()
    page.click_go_to_summary_button()
