import allure
from pages.base_page import BasePage
from pages.product_listing_page import PLP
from constants import URL, Search


@allure.feature('Search product cases')
class TestSearch:
    @allure.description('Check placeholder text. Search field can be closed')
    def test_search_field(self, driver, check):
        base_page = BasePage(driver, URL.BASE_URL)
        base_page.open_page()

        base_page.click_search_icon()
        placeholder_text = base_page.get_search_field_placeholder_text()
        with check:
            assert placeholder_text == Search.SEARCH_FIELD_PLACEHOLDER_TEXT, \
                'Placeholder text in the search field is not correct'
        base_page.click_close_search_icon()

        base_page.assert_search_field_closed()

    @allure.description('Positive search leads to the correct search resul page, check the total products found')
    def test_positive_search(self, driver, check):
        search_query = 'sneakers'

        base_page = BasePage(driver, URL.BASE_URL)
        base_page.open_page()

        base_page.click_search_icon()

        base_page.enter_search_query(search_query)
        total_products_found = base_page.get_search_total_products_value()
        base_page.click_show_all_button()
        with check:
            assert base_page.get_current_url() == f'https://gb.ecco.com/en-GB/Search?searchText={search_query}', \
                'Show All button does not lead to correct URL '

        search_result_page = PLP(driver, driver.current_url)

        assert total_products_found == search_result_page.get_total_products_value(), \
            'Total products value on the global search window and on the search result page is different'

    @allure.description('Check error message for negative search')
    @allure.tag('negative')
    def test_negative_search(self, driver):
        search_query = 'WWW'

        page = BasePage(driver, URL.BASE_URL)
        page.open_page()

        page.click_search_icon()
        page.enter_search_query(search_query)

        assert page.get_no_products_found_message_text() == Search.NO_PRODUCTS_FOUND_MESSAGE, \
            'No products found message is not correct'
