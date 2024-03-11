class URL:
    BASE_URL = 'https://gb.ecco.com/en-GB'
    REGISTER_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO/Register'
    PRODUCT_PAGE = 'https://gb.ecco.com/en-GB/product/5643365205/ECCO-METROPOLE-LONDON'
    PLP = 'https://gb.ecco.com/en-GB/Men/Shoes'
    ACCOUNT_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO'
    LOGIN_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO/Login'
    EDIT_USER_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO/My-Personal-Details/Edit'
    MY_FAVOURITES_PAGE = 'https://gb.ecco.com/en-GB/My-ECCO/My-Favourites'


class AuthData:
    LOGIN_EMAIL = 'fayabob242@fkcod.com'
    LOGIN_PASSWORD = '123qwe!'


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


class LoginAlerts:
    EMPTY_EMAIL_ALERT = 'Email required'
    EMPTY_PASSWORD_ALERT = 'Password required'
    INCORRECT_EMAIL_FORMAT_ALERT = 'Email invalid'
    LOGIN_FAILED = 'Invalid login'


class AccountAlerts:
    EDIT_EMPTY_FIRSTNAME_ALERT = 'First Name Required'
    EDIT_EMPTY_LASTNAME_ALERT = 'Last Name Required'
    EDIT_EMPTY_EMAIL_ALERT = 'Email required'
    EDIT_INCORRECT_EMAIL_FORMAT_ALERT = 'Email invalid'
    EDIT_EMPTY_PHONE_NUMBER_ALERT = 'Phone is a required field'
    EDIT_INCORRECT_PHONE_NUMBER_FORMAT_ALERT = 'Phone must be number'
    EDIT_INCORRECT_PHONE_NUMBER_LENGTH_ALERT = 'The phone must contain a minimum of 7 and a maximum of 11 digits'
    ADDRESS_EMPTY_FIRSTNAME_ALERT = 'First name is a required field'
    ADDRESS_EMPTY_LASTNAME_ALERT = 'Last name is a required field'
    ADDRESS_EMPTY_STREET_ALERT = 'Street is a required field'
    ADDRESS_EMPTY_NUMBER_ALERT = 'Number is a required field'
    ADDRESS_EMPTY_CODE_ALERT = 'Zip code is a required field'
    ADDRESS_EMPTY_CITY_ALERT = 'City is a required field'
    UPDATED_INFO_TEXT = 'Your information have now been updated, thank you!'
    EMPTY_FAVORITES_MESSAGE = 'You have not selected any favourites yet'
    MY_FAVOURITES_TITLE_TEXT = 'My Favourites'
    GUEST_FAVOURITES_TITLE_TEXT = 'Guest Favourites'
