import time
import allure
import random
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        with allure.step(f"Open {self.url} page"):
            self.driver.get(self.url)
            if self.is_element_present(BasePageLocators.ACCEPT_ALL_COOKIES_BTN, timeout=1):
                self.accept_all_cookies()

    def is_open(self, timeout=1):
        time.sleep(timeout)
        with allure.step(f"Page {self.url} is open"):
            assert self.get_current_url() == self.url, \
                f'Expected url {self.url} is not open, actual url {self.get_current_url()}'
        # try:
        #     WebDriverWait(self.driver, timeout).until(EC.url_to_be(self.url))
        # except TimeoutException:
        #     return False
        # return True

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

    def get_current_url(self, timeout=1):
        time.sleep(timeout)
        return self.driver.current_url

    def move_to_element(self, locator):
        """Move cursor to element"""
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).perform()

    def sroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # GETTERS
    def get_basket_icon_count_value(self):
        return int(self.find_element(BasePageLocators.BASKET_ICON_COUNT).text)

    def get_favorites_icon_count_value(self):
        return int(self.find_element(BasePageLocators.FAVOURITES_ICON_COUNT).text)

    def get_search_field_placeholder_text(self):
        return self.find_element(BasePageLocators.SEARCH_FIELD).get_attribute('placeholder')

    def get_search_total_products_value(self):
        """Get product count in the Show All button"""
        return int(self.find_element(BasePageLocators.GLOBAL_SEARCH_SHOW_ALL_BTN).text.split('(')[1].rstrip(')'))

    def get_no_products_found_message_text(self):
        return self.find_element(BasePageLocators.NO_PRODUCTS_MSG).text

    # ACTIONS
    @allure.step('Refresh the page')
    def refresh_page(self):
        time.sleep(1)
        self.driver.refresh()
        print('Refresh the page')

    @allure.step('Open link')
    def open_link(self, link):
        self.driver.get(link)
        print(f'Open link {link}')

    @allure.step('Click Logo')
    def click_logo(self):
        self.find_element(BasePageLocators.LOGO).click()
        print('Click Logo')

    @allure.step('Click random category in the navigation mega menu (except "Bags" and "Explore")')
    def select_random_mega_menu_category(self):
        self.find_elements(BasePageLocators.MEGA_MENU_CATEGORY)[random.randint(0, 6)].click()
        print('Click random category in the navigation mega menu')

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

    @allure.step('Enter search query in the search field')
    def enter_search_query(self, search_query):
        self.find_element(BasePageLocators.SEARCH_FIELD).send_keys(search_query)
        print('Enter search query in the search field')

    @allure.step('Click Show All button in the Global Search window')
    def click_show_all_button(self):
        self.find_element(BasePageLocators.GLOBAL_SEARCH_SHOW_ALL_BTN).click()
        print('Click Show All button in the Global Search window')

    @allure.step('Click Close Search icon')
    def click_close_search_icon(self):
        self.find_element(BasePageLocators.CLOSE_SEARCH_ICON).click()
        print('Click Close Search icon')

    @allure.step('Click recently viewed product')
    def click_recently_viewed_product(self):
        self.find_element(BasePageLocators.RECENTLY_VIEWED_PRODUCT).click()
        print('Click recently viewed product')

    # ASSERTIONS
    @allure.step('Assert the favourites icon count appears when adding a product to Favourites from PDP')
    def assert_favourites_icon_count_present(self):
        assert self.is_element_present(BasePageLocators.FAVOURITES_ICON_COUNT), \
            'Favourites icon count is missing'
        print('Favourites icon count is present')

    @allure.step('Assert favourites icon count disappears after removing a product from Favourites')
    def assert_favourites_icon_count_is_missing(self):
        assert self.is_not_element_present(BasePageLocators.FAVOURITES_ICON_COUNT, timeout=1), \
            'Favourites icon count is present after removing a product from Favourites'
        print('Favourites icon count is missing')

    @allure.step('Assert the basket icon count appears when adding a product to basket')
    def assert_basket_icon_count_present(self):
        assert self.is_element_present(BasePageLocators.BASKET_ICON_COUNT), \
            'Basket icon count is missing'
        print('Basket icon count is present')

    @allure.step('Assert basket icon count disappears after removing a product from basket')
    def assert_basket_icon_count_is_missing(self):
        assert self.is_not_element_present(BasePageLocators.BASKET_ICON_COUNT, timeout=1), \
            'Basket icon count is present after removing a product from the basket'
        print('Basket icon count is missing')

    @allure.step('Assert the search field is closed after clicking the close icon')
    def assert_search_field_closed(self):
        assert self.is_disappeared(BasePageLocators.SEARCH_FIELD, timeout=2), \
            'Search field is not closed'
        print('Search field is closed')

    @allure.step('Check the recently viewed product is missing')
    def is_recently_viewed_product_missing(self):
        return self.is_not_element_present(BasePageLocators.RECENTLY_VIEWED_PRODUCT)

    @allure.step('Check the recently viewed product is present')
    def is_recently_viewed_product_present(self):
        return self.is_element_present(BasePageLocators.RECENTLY_VIEWED_PRODUCT)
