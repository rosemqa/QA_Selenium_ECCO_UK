from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.CSS_SELECTOR, 'a.logo')
    ACCEPT_ALL_COOKIES_BTN = (By.CSS_SELECTOR, 'button.coi-banner__accept')
    PROFILE_ICON = (By.CSS_SELECTOR, 'a.commerce-links__profile-icon')
    STORE_FINDER_ICON = (By.CSS_SELECTOR, 'a.commerce-links__storefinder')
    FAVORITES_ICON = (By.CSS_SELECTOR, '.favourites__icon')
    FAVOURITES_ICON_COUNT = (By.CSS_SELECTOR, '#favouritesCount')
    BASKET_ICON = (By.CSS_SELECTOR, '#basket_icon')
    BASKET_ICON_COUNT = (By.CSS_SELECTOR, 'span.basket__items-count')
    SEARCH_ICON = (By.CSS_SELECTOR, '.search-icon')


class RegistrationPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
    GENDER_FEMALE = (By.CSS_SELECTOR, '[for="GenderFemale"]')
    GENDER_MALE = (By.CSS_SELECTOR, '[for="GenderMale"]')
    ACCEPT_TERMS = (By.CSS_SELECTOR, '[for="AcceptConsent"]')
    ACCEPT_TERMS_LINK = (By.CSS_SELECTOR, '[for="AcceptConsent"] a')
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '.ecco_button__center')
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, '#FirstName-error')
    LAST_NAME_ERROR = (By.CSS_SELECTOR, '#LastName-error')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#Email-error')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '#Password-error')
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, '#ConfirmPassword-error')
    ACCEPT_TERMS_ERROR = (By.CSS_SELECTOR, '#AcceptConsent-error')
    TERMS_WINDOW_ELEMENT = (By.CSS_SELECTOR, '.signup-consent-dialog')


class AccountPageLocators:
    GREETING_TITLE = (By.CSS_SELECTOR, '.myecco-overview-greeting>.heading')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.product_info__buttons-primary')
    CLICK_AND_COLLECT_BTN = (By.CSS_SELECTOR, '.product_info__buttons-secondary')
    ADD_TO_FAVORITES_BTN = (By.CSS_SELECTOR, '.product_info__add-to-wishlist')
    ADD_TO_FAVORITES_TOOLTIP = (By.CSS_SELECTOR, '.tooltip__content')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_info__intro-title')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_info__price')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '.product_info__color--selected')
    COLOR_SELECTOR_ITEM = (By.CSS_SELECTOR, '.product_info__color-item')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.product_details__media-item-img img')
    AVAILABLE_SIZE = (By.CSS_SELECTOR, '.size-picker__item[title=""]')
    SIZE_GUIDE_BTN = (By.CSS_SELECTOR, 'button.size-guide-button')
    SIZE_GUIDE_MODAL = (By.CSS_SELECTOR, '.modal__inner-wrapper--size-guide')
    SIZE_GUIDE_ADD_SIZE_BTN = (By.CSS_SELECTOR, '.size-guide__calculator .shown')
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


class PLPLocators:
    FILTERS_ITEMS_COUNT = (By.CSS_SELECTOR, '.count-indicator')
    FILTERS_COLOR = (By.CSS_SELECTOR, '#dominantcolor')
    FILTERS_COLOR_NAME = (By.CSS_SELECTOR, '#dominantcolor .custom_selectbox__list-item-checkbox')
    FILTERS_COLOR_AMOUNT = (By.CSS_SELECTOR, '#dominantcolor .amount')
    FILTERS_PRICE = (By.CSS_SELECTOR, '.filter-btn #adjustedprice')
    SELECTED_FILTER = (By.CSS_SELECTOR, '.selected-filter')
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, '.filters-sorting__container')
    SORT_BY_PRICE_ASC = (By.XPATH, '//*[.="Lowest price"]/..')
    SORT_BY_PRICE_DESC = (By.XPATH, '//*[.="Highest price"]/..')
    PRICE_SLIDER_MIN = (By.CSS_SELECTOR, '.handle-left')
    PRICE_SLIDER_MAX = (By.CSS_SELECTOR, '.handle-right')
    PRICE_RANGE_MIN = (By.CSS_SELECTOR, '.rangeslider__value--min')
    PRICE_RANGE_MAX = (By.CSS_SELECTOR, '.rangeslider__value--max')
    CLEAR_ALL_BTN = (By.CSS_SELECTOR, '.selected-filter.clear-filters-btn')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.meta__price')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.meta__title')
    ADD_TO_FAVORITE_ICON = (By.CSS_SELECTOR, '#favorite-fill')
    BACK_TO_TOP_BTN = (By.CSS_SELECTOR, '.scroll-to-top')
