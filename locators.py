from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.CSS_SELECTOR, 'a.logo')
    ACCEPT_NECESSARY_COOKIES_BTN = (By.CSS_SELECTOR, '#coiOverlay #declineButton')
    PROFILE_ICON = (By.CSS_SELECTOR, 'a.commerce-links__profile-icon')
    STORE_FINDER_ICON = (By.CSS_SELECTOR, 'a.commerce-links__storefinder')
    FAVORITES_ICON = (By.CSS_SELECTOR, '.favourites__icon')
    BASKET_ICON = (By.CSS_SELECTOR, '#basket_icon')
    SEARCH_ICON = (By.CSS_SELECTOR, '.search-icon')
    BACK_TO_TOP_BTN = (By.CSS_SELECTOR, '.scroll-to-top')

