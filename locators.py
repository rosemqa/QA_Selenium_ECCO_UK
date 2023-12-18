from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.CSS_SELECTOR, 'a.logo')
    ACCEPT_NECESSARY_COOKIES_BTN = (By.CSS_SELECTOR, '#coiOverlay #declineButton')
    PROFILE_ICON = (By.CSS_SELECTOR, 'a.commerce-links__profile-icon')
    STORE_FINDER_ICON = (By.CSS_SELECTOR, 'a.commerce-links__storefinder')
    FAVORITES_ICON = (By.CSS_SELECTOR, '.favourites__icon')
    BASKET_ICON = (By.CSS_SELECTOR, '#basket_icon')
    BASKET_ICON_COUNT = (By.CSS_SELECTOR, 'span.basket__items-count')
    SEARCH_ICON = (By.CSS_SELECTOR, '.search-icon')
    BACK_TO_TOP_BTN = (By.CSS_SELECTOR, '.scroll-to-top')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.product_info__buttons-primary')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_info__intro-title')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_info__price')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '.product_info__color--selected')
    AVAILABLE_SIZE = (By.CSS_SELECTOR, '.size-picker__item[title=""]')
    MINI_BASKET_OVERLAY = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible')
    MINI_BASKET_GO_TO_BASKET_BTN = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible a.ecco_button')
    MINI_BASKET_KEEP_SHOPPING_BTN = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible [aria-label="Keep Shopping"]')
    MINI_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .product_name')
    MINI_BASKET_PRODUCT_COLOR = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .product_color')
    MINI_BASKET_PRODUCT_SIZE = (
        By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .product_size .product_size__variant'
    )
    MINI_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .price')
    MINI_BASKET_TOTAL = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .summary_total .summary_price')
    MINI_BASKET_NUMBER_OF_ITEMS = (By.CSS_SELECTOR, '.basket_overlay__wrapper--visible .summary_num-of-items')



