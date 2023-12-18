import allure
from .base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    # GETTERS
    def get_product_title_text(self):
        return self.find_element(ProductPageLocators.PRODUCT_TITLE).text

    def get_product_size_text(self):
        return self.find_element(ProductPageLocators.AVAILABLE_SIZE).text

    def get_product_price_value(self):
        return int(self.find_element(ProductPageLocators.PRODUCT_PRICE).text.split()[1].split('.')[0])

    def get_product_color_text(self):
        return self.find_element(ProductPageLocators.PRODUCT_COLOR).text

    def get_mini_basket_product_title_text(self):
        return self.find_element(ProductPageLocators.MINI_BASKET_PRODUCT_TITLE).text

    def get_mini_basket_product_price_value(self):
        return int(self.find_element(ProductPageLocators.MINI_BASKET_PRODUCT_PRICE).text.split()[1].split('.')[0])

    def get_mini_basket_product_color_text(self):
        return self.find_element(ProductPageLocators.MINI_BASKET_PRODUCT_COLOR).text

    def get_mini_basket_product_size_text(self):
        return self.find_element(ProductPageLocators.MINI_BASKET_PRODUCT_SIZE).text

    def get_mini_basket_product_count_value(self):
        return int(self.find_element(ProductPageLocators.MINI_BASKET_NUMBER_OF_ITEMS).text.rsplit(' ', 1)[1])

    def get_mini_basket_total_value(self):
        return int(self.find_element(ProductPageLocators.MINI_BASKET_TOTAL).text.split()[1].split('.')[0])

    # ACTIONS
    @allure.step('Select available size')
    def select_available_size(self):
        self.find_element(ProductPageLocators.AVAILABLE_SIZE).click()
        print('Select available size')

    @allure.step('Click Add To Basket button')
    def click_add_to_basket_button(self):
        self.find_element(ProductPageLocators.ADD_TO_BASKET_BTN).click()
        print('Click Add To Basket button')
