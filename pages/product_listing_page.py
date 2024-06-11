import random
import time
import allure
from selenium.webdriver import ActionChains, Keys
from locators import PLPLocators
from .base_page import BasePage


class PLP(BasePage):

    # GETTERS
    def get_total_products_value(self):
        return int(self.find_element(PLPLocators.FILTERS_ITEMS_COUNT).text)

    def get_selected_filter_text(self):
        return self.find_element(PLPLocators.SELECTED_FILTER).text

    def get_color_name_text_in_dropdown(self):
        return self.find_elements(PLPLocators.FILTERS_COLOR_NAME)[1].text.split()[0]

    def get_amount_value_in_color_dropdown(self):
        """Get product amount for first color in the color dropdown"""
        return int(self.find_element(PLPLocators.FILTERS_COLOR_AMOUNT).text.lstrip('(').rstrip(')'))

    def get_first_product_price(self):
        return int(self.find_elements(PLPLocators.PRODUCT_PRICE)[0].text.split()[1].split('.')[0])

    def get_first_product_title(self):
        return self.find_elements(PLPLocators.PRODUCT_TITLE)[0].text

    def get_price_list(self):
        """Get prices of all products on PLP"""
        time.sleep(1)
        elements_list = self.find_elements(PLPLocators.PRODUCT_PRICE)
        price_list = [int(element.text.split()[1].split('.')[0]) for element in elements_list]
        return price_list

    def get_min_price_value_in_price_range(self):
        return int(self.find_element(PLPLocators.PRICE_RANGE_MIN).text.split()[1].split('.')[0])

    def get_max_price_value_in_price_range(self):
        return int(self.find_element(PLPLocators.PRICE_RANGE_MAX).text.split()[1].split('.')[0])

    # ACTIONS
    @allure.step('Click Color filter')
    def click_color_filter(self):
        self.find_element(PLPLocators.FILTERS_COLOR).click()
        time.sleep(1)
        print('Click Color filter')

    @allure.step('Click Price filter')
    def click_price_filter(self):
        self.find_element(PLPLocators.FILTERS_PRICE).click()
        print('Click Price filter')

    @allure.step('Select first color in the color filter')
    def select_color(self):
        self.find_elements(PLPLocators.FILTERS_COLOR_NAME)[1].click()
        time.sleep(1)
        print('Select first color in the color filter')

    @allure.step('Set the min price on the price slider')
    def set_min_price(self):
        time.sleep(1)
        min_price_dot = self.find_element(PLPLocators.PRICE_SLIDER_MIN)  # left slider handle
        ActionChains(self.driver) \
            .drag_and_drop_by_offset(min_price_dot, 50, 0) \
            .perform()
        print('Set the min price on the price slider')

    @allure.step('Set the max price on the price slider')
    def set_max_price(self):
        time.sleep(1)
        max_price_dot = self.find_element(PLPLocators.PRICE_SLIDER_MAX)  # right slider handle
        ActionChains(self.driver) \
            .drag_and_drop_by_offset(max_price_dot, -50, 0) \
            .perform()
        print('Set the max price on the price slider')

    @allure.step('Click Clear All button')
    def click_clear_all_button(self):
        self.find_element(PLPLocators.CLEAR_ALL_BTN).click()
        time.sleep(1)
        print('Click Clear All button')

    @allure.step('Click Sort By')
    def click_sort_by(self):
        self.find_element(PLPLocators.SORT_BY_DROPDOWN).click()
        time.sleep(1)
        print('Click Sort By')

    @allure.step('Click "Lowest Price" in the sorting menu')
    def click_sort_by_price_asc(self):
        self.find_element(PLPLocators.SORT_BY_PRICE_ASC).click()
        print('Click "Lowest Price" in the sorting menu')

    @allure.step('Click "Highest Price" in the sorting menu')
    def click_sort_by_price_desc(self):
        self.find_element(PLPLocators.SORT_BY_PRICE_DESC).click()
        print('Click "Highest Price" in the sorting menu')

    @allure.step('Click the add to favorites icon on the first product')
    def click_add_to_favorites(self):
        self.find_element(PLPLocators.ADD_TO_FAVORITE_ICON).click()
        print('Click the add to favorites icon on the first product')

    @allure.step('Scroll down two screen')
    def scroll_down_two_screen(self):
        ActionChains(self.driver) \
            .click() \
            .send_keys(Keys.PAGE_DOWN * 2) \
            .perform()
        print('Scroll down two screen')

    @allure.step('Click Back To Top button')
    def click_back_to_top_button(self):
        self.find_element(PLPLocators.BACK_TO_TOP_BTN).click()
        print('Click Back To Top button')

    @allure.step('Click random product in the product list')
    def select_product(self):
        rand = random.randint(0, 10)
        product_title = self.find_elements(PLPLocators.PRODUCT_TITLE)[rand]
        product_title_text = product_title.text
        product_price_value = int(self.find_elements(PLPLocators.PRODUCT_PRICE)[rand].text.split()[1].split('.')[0])
        self.find_element(PLPLocators.PRODUCT_ITEM).click()
        print('Click random product title in the product list')
        return product_title_text, product_price_value

    # ASSERTIONS
    @allure.step('Assert Back to Top button appears after scrolling down two screen on the page')
    def assert_back_to_top_button_appears(self):
        assert self.is_element_present(PLPLocators.BACK_TO_TOP_BTN), \
            'Back to Top button is missing'
        print('Back to Top button is present')

    @allure.step('Assert the page scrolls up to the top when clicking the Back to Top button')
    def assert_page_scrolled_to_top(self):
        page_y_offset = self.driver.execute_script('return window.pageYOffset;')
        assert page_y_offset == 0, \
            'The page does not scroll up when clicking Back To Top button'
        print('Page scrolled to the top')

    @allure.step('Assert Back to Top button disappears after clicking on it')
    def assert_back_to_top_button_disappears(self):
        assert self.is_disappeared(PLPLocators.BACK_TO_TOP_BTN), \
            'Back to Top button is still present after clicking on it'
        print('Back to Top button has disappeared')
