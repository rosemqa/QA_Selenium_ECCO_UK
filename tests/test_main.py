import allure
from pages.base_page import BasePage
from pages.product_page import ProductPage
from constants import URL


@allure.feature('Main page cases')
class TestMain:
    @allure.description('Recently viewed product appears in the recently viewed section')
    def test_recently_viewed_section(self, driver):
        main_page = BasePage(driver, URL.BASE_URL)
        main_page.open_page()
        assert main_page.is_recently_viewed_product_missing() is True, \
            'Recently viewed product is present'

        pdp = ProductPage(driver, URL.PRODUCT_PAGE)
        pdp.open_page()
        pdp.is_open()
        pdp.click_logo()

        main_page.is_open()
        assert main_page.is_recently_viewed_product_present() is True, \
            'Recently viewed product is missing'

    @allure.description('The product in the Recently Viewed section leads to relevant PDP')
    def test_open_recently_viewed_product(self, driver):
        main_page = BasePage(driver, URL.BASE_URL)
        main_page.open_page()

        pdp = ProductPage(driver, URL.PRODUCT_PAGE)
        pdp.open_page()
        pdp.is_open()
        pdp.click_logo()

        main_page.is_open()
        main_page.click_recently_viewed_product()

        pdp.is_open()
