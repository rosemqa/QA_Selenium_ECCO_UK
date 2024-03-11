import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)
        if self.is_element_present(BasePageLocators.ACCEPT_ALL_COOKIES_BTN, timeout=1):
            self.accept_all_cookies()

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout) \
            .until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout) \
            .until(EC.presence_of_all_elements_located(locator), message=f"Can't find element by locator {locator}")

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def get_current_url(self):
        time.sleep(1)
        return self.driver.current_url

    # GETTERS
    def get_basket_icon_count_value(self):
        return int(self.find_element(BasePageLocators.BASKET_ICON_COUNT).text)

    def get_favorites_icon_count_value(self):
        return int(self.find_element(BasePageLocators.FAVOURITES_ICON_COUNT).text)

    # ACTIONS
    @allure.step('Refresh the page')
    def refresh_page(self):
        time.sleep(1)
        self.driver.refresh()
        print('Refresh the page')

    @allure.step('Click Logo')
    def click_logo(self):
        self.find_element(BasePageLocators.LOGO).click()
        print('Click Logo')

    @allure.step('Accept cookies')
    def accept_all_cookies(self):
        self.find_element(BasePageLocators.ACCEPT_ALL_COOKIES_BTN).click()
        print('Accept cookies')

    @allure.step('Click Profile icon')
    def click_profile_icon(self):
        self.find_element(BasePageLocators.PROFILE_ICON).click()
        print('Click Profile icon')

    @allure.step('Click Store finder icon')
    def click_store_finder_icon(self):
        self.find_element(BasePageLocators.STORE_FINDER_ICON).click()
        print('Click Store finder icon')

    @allure.step('Click Favorites icon')
    def click_favorites_icon(self):
        self.find_element(BasePageLocators.FAVORITES_ICON).click()
        print('Click Favorites icon')

    @allure.step('Click Basket icon')
    def click_basket_icon(self):
        self.find_element(BasePageLocators.BASKET_ICON).click()
        print('Click Basket icon')

    @allure.step('Click Search icon')
    def click_search_icon(self):
        self.find_element(BasePageLocators.SEARCH_ICON).click()
        print('Click Search  icon')

    # ASSERTIONS
    @allure.step('Assert the favourites icon count appears when adding a product to Favourites from PDP')
    def assert_favourites_icon_count_present(self):
        assert self.is_element_present(BasePageLocators.FAVOURITES_ICON_COUNT), \
            'Favourites icon count is missing'
        print('Favourites icon count is present')


