import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)
        self.accept_necessary_cookies()

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout) \
            .until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout) \
            .until(EC.presence_of_all_elements_located(locator), message=f"Can't find element by locator {locator}")

    # GETTERS
    def get_basket_icon_count_value(self):
        return int(self.find_element(BasePageLocators.BASKET_ICON_COUNT).text)

    # ACTIONS
    @allure.step('Click Logo')
    def click_logo(self):
        self.find_element(BasePageLocators.LOGO).click()
        print('Click Logo')

    @allure.step('Accept cookies')
    def accept_necessary_cookies(self):
        self.find_element(BasePageLocators.ACCEPT_NECESSARY_COOKIES_BTN).click()
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

    @allure.step('Click Back To Top button')
    def click_back_to_top_button(self):
        self.find_element(BasePageLocators.BACK_TO_TOP_BTN).click()
        print('Click Back To Top button')


