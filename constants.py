class URL:
    BASE_URL = 'https://gb.ecco.com/en-GB'
    REGISTER_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO/Register'
    PRODUCT_PAGE = 'https://gb.ecco.com/en-GB/product/5643365205/ECCO-METROPOLE-LONDON'
    PLP = 'https://gb.ecco.com/en-GB/Men/Shoes'
    ACCOUNT_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO'


class RegistrationAlerts:
    EMPTY_FIRSTNAME_ALERT = 'First name required'
    EMPTY_LASTNAME_ALERT = 'Last name required'
    EMPTY_EMAIL_ALERT = 'Email required'
    INCORRECT_EMAIL_FORMAT_ALERT = 'Email invalid'
    EMPTY_PASSWORD_ALERT = 'Password required'
    INCORRECT_PASSWORD_FORMAT_ALERT = \
        'Passwords must contain at least 1 letter and 1 number, and be at least 6 characters long.'
    SHORT_PASSWORT_ALERT = 'Passwords must be at least 6 characters long.'
    CONFIRM_PASSWORD_ALERT = 'The passwords must be the same'
    ACCEPT_TERMS_ALERT = 'Accept terms is required'
