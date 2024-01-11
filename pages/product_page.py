import allure
from selenium.webdriver import ActionChains, Keys

from .base_page import BasePage
from locators import ProductPageLocators, BasePageLocators


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

    def get_product_image_src(self):
        return self.find_element(ProductPageLocators.PRODUCT_IMAGE).get_attribute('src')

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

    @allure.step('Select the second color in the color selector')
    def select_second_color(self):
        self.find_elements(ProductPageLocators.COLOR_SELECTOR_ITEM)[1].click()
        print('Select the second color in the color selector')

    @allure.step('Click Add To Basket button')
    def click_add_to_basket_button(self):
        self.find_element(ProductPageLocators.ADD_TO_BASKET_BTN).click()
        print('Click Add To Basket button')

    @allure.step('Click "Click & Collect" button')
    def click_click_and_collect_button(self):
        self.find_element(ProductPageLocators.CLICK_AND_COLLECT_BTN).click()
        print('Click "Click & Collect" button')

    @allure.step('Click Add to Favorites button')
    def click_add_to_favorites_button(self):
        self.find_element(ProductPageLocators.ADD_TO_FAVORITES_BTN).click()
        print('Click Add to Favorites button')

    @allure.step('Move the mouse from Add to favorites button to the right')
    def move_mouse_to_right(self):
        action = ActionChains(self.driver)
        action \
            .move_by_offset(15, 0) \
            .perform()
        print('Move the mouse from Add to favorites button to the right')

    @allure.step('Click Go To Basket button in the mini basket')
    def click_go_to_basket_button(self):
        self.find_element(ProductPageLocators.MINI_BASKET_GO_TO_BASKET_BTN).click()
        print('Click Go To Basket button in the mini basket')

    @allure.step('Click Keep Shopping button in the mini basket')
    def click_keep_shopping_button(self):
        self.find_element(ProductPageLocators.MINI_BASKET_KEEP_SHOPPING_BTN).click()
        print('Click Keep Shopping button in the mini basket')

    @allure.step('Click Size Guide button')
    def click_size_guide_button(self):
        self.find_element(ProductPageLocators.SIZE_GUIDE_BTN).click()
        print('Click Size Guide button')

    # ASSERTIONS
    @allure.step('Assert the Size Guide modal opens when clicking the size guide link')
    def assert_size_guide_modal_opens(self):
        assert self.is_element_present(ProductPageLocators.SIZE_GUIDE_MODAL), \
            'Size Guide modal is missing'
        print('Size Guide modal is present')

    @allure.step('Assert the Add Size button is present in the Size Guide modal')
    def assert_add_size_button_present_in_size_guide(self):
        assert self.is_element_present(ProductPageLocators.SIZE_GUIDE_ADD_SIZE_BTN), \
            'Add Size button is missing in the Size Guide modal'
        print('Add Size button is present in the Size Guide modal')

    @allure.step('Assert Add to favorites tooltip appears when clicking on Add To Favorites button')
    def assert_add_to_favorites_tooltip_appears(self):
        assert self.is_element_present(ProductPageLocators.ADD_TO_FAVORITES_TOOLTIP), \
            'Add to favorites tooltip does not appear when clicking on Add To Favorites button'
        print('Add to favorites tooltip appears')

    @allure.step('Assert Add to favorites tooltip does not disappear after 1 sec')
    def assert_add_to_favorites_tooltip_disappears(self):
        assert self.is_disappeared(ProductPageLocators.ADD_TO_FAVORITES_TOOLTIP), \
            'Add to favorites tooltip does not disappear after 1 sec'
        print('Add to favorites tooltip disappear after 1 sec')
