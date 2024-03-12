import time
import allure
import pytest
from pages.account_page import AccountPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from constants import URL, AuthData, AccountAlerts


@allure.epic('Add/delete to/from Favourites cases')
class TestFavourites:
    @pytest.fixture()
    def login(self, driver):
        """Precondition: login to account """
        page = LoginPage(driver, URL.LOGIN_PAGE)
        page.open_page()

        page.enter_email(AuthData.LOGIN_EMAIL)
        page.enter_password(AuthData.LOGIN_PASSWORD)
        page.click_sign_in_button()
        time.sleep(1)

    @pytest.fixture()
    def add_to_favorites(self, driver):
        """Precondition: add product to Favourites from PDP"""
        page = ProductPage(driver, URL.PRODUCT_PAGE)
        page.open_page()
        page.click_add_to_favorites_button()
        page.click_favorites_icon()

    @pytest.fixture()
    def delete_from_favourites(self, driver):
        """Teardown: remove the product from Favourites"""
        yield
        print('\nTeardown:')
        page = AccountPage(driver, URL.MY_FAVOURITES_PAGE)
        if page.get_current_url() != URL.MY_FAVOURITES_PAGE:
            page.open_page()
        page.click_delete_favourite_button()
        page.confirm_deletion_in_the_modal()

    @allure.description('Test As a user, add product to Favorites from PDP and check the favorites page')
    def test_add_to_favourites_from_pdp_as_user(self, driver, login, delete_from_favourites):
        pdp = ProductPage(driver, URL.PRODUCT_PAGE)
        pdp.open_page()

        pdp_prodict_name = pdp.get_product_title_text()
        pdp_product_color = pdp.get_product_color_text()
        pdp_product_price = pdp.get_product_price_value()

        pdp.click_add_to_favorites_button()
        pdp.click_favorites_icon()

        fav_page = AccountPage(driver, driver.current_url)

        fav_page_title = fav_page.get_favourites_page_title_text()
        fav_prodict_name = fav_page.get_favourites_product_name_text()
        fav_product_color = fav_page.get_favourites_product_color_text()
        fav_product_price = fav_page.get_favourites_product_price_value()

        assert fav_page_title == AccountAlerts.MY_FAVOURITES_TITLE_TEXT, \
            'Favourites page title text is not correct'
        assert pdp_prodict_name == fav_prodict_name, \
            'Product name on the PDP and on the favorites page is different'
        assert pdp_product_color == fav_product_color, \
            'Product color on the PDP and on the favorites page is different'
        assert pdp_product_price == fav_product_price, \
            'Product price on the PDP and on the favorites page is different'

    @allure.description('Test As a guest, add product to Favorites from PDP and check the favorites page')
    def test_add_to_favourites_from_pdp_as_guest(self, driver):
        pdp = ProductPage(driver, URL.PRODUCT_PAGE)
        pdp.open_page()
        pdp.click_add_to_favorites_button()
        pdp.click_favorites_icon()

        fav_page = AccountPage(driver, driver.current_url)
        fav_page_title = fav_page.get_favourites_page_title_text()
        assert fav_page_title == AccountAlerts.GUEST_FAVOURITES_TITLE_TEXT, \
            'Favourites page title text is not correct'
        fav_page.assert_sign_in_button_is_present()

    @allure.description('Test if a product can be removed from Favorites on the favourites page')
    def test_delete_from_favourites(self, driver, login, add_to_favorites):
        page = AccountPage(driver, driver.current_url)

        page.click_delete_favourite_button()
        page.confirm_deletion_in_the_modal()

        assert page.get_empty_favourites_message_text() == AccountAlerts.EMPTY_FAVORITES_MESSAGE, \
            'Empty favorites message is not correct'
        page.assert_favourites_icon_count_is_missing()

    @allure.description('Test "Share you favourites" link')
    def test_share_favourites(self, driver, login, add_to_favorites, delete_from_favourites):
        page = AccountPage(driver, driver.current_url)

        prodict_name = page.get_favourites_product_name_text()
        product_color = page.get_favourites_product_color_text()
        product_price = page.get_favourites_product_price_value()

        page.click_share_favourites_button()

        link = page.get_share_link_text()
        page.open_link(link)

        see_page_title = page.get_favourites_page_title_text()
        see_prodict_name = page.get_favourites_product_name_text()
        see_product_color = page.get_favourites_product_color_text()
        see_product_price = page.get_favourites_product_price_value()

        assert see_page_title == AccountAlerts.SEE_MY_FAVOURITES_TITLE_TEXT, \
            'See My Favourites page title text is not correct'
        assert prodict_name == see_prodict_name, \
            'Product name on the Favorites and on the See My Favorites page is different'
        assert product_color == see_product_color, \
            'Product color on the Favorites and on the See My Favorites page is different'
        assert product_price == see_product_price, \
            'Product price on the Favorites and on the See My Favorites page is different'

    @allure.description('Test if favorite product link in the Favorites leads to relevant PDP')
    def test_favourite_product_link(self, driver, add_to_favorites):
        page = AccountPage(driver, driver.current_url)

        page.click_favourite_product_name()

        assert page.get_current_url() == URL.PRODUCT_PAGE, \
            'Favorite product link does not lead to relevant PDP'
