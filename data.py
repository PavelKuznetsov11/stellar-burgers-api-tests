

class Data:

    CREATE_USER_DATA = {
        'email': 'qa2fj5@gmail.com',
        'password': 'test_!)f#_85[',
        'name': 'Username110'
    }

    CREATE_USER_DATA_WITHOUT_NAME = {
        'email': 'qa2fj5@gmail.com',
        'password': 'test_!)f#_85['
    }

    CREATE_USER_DATA_WITHOUT_PASSWORD = {
        'email': 'qa2fj5@gmail.com',
        'name': 'Username110'
    }

    CREATE_USER_DATA_WITHOUT_EMAIL = {
        'password': 'test_!)f#_85[',
        'name': 'Username110'
    }

    SUCCESS = 'success'

    ORDER = 'order'

    OWNER = 'owner'

    MESSAGE = 'message'

    MESSAGE_ERROR_INGREDIENT = 'Ingredient ids must be provided'

    SERVER_ERROR = "Internal Server Error"

    TOKEN = 'token'

    ACCESSTOKEN = 'accessToken'

    USER_ALREADY_EXISTS = 'User already exists'

    REQUIRED_FIELD_ERROR = "Email, password and name are required fields"

    EMAIL_PASSWORD_INCORRECT_ERROR = 'email or password are incorrect'

    INCORRECT_PASSWORD = 'qwerty=_14<fg?'

    INCORRECT_EMAIL = 'qa2fj5kqwgdksahiu321342@gmail.com'

    EMAIL = 'email'
    PASSWORD = 'password'

    INGREDIENTS = {
        "ingredients" : ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    INCORRECT_HASH_INGREDIENTS = {
        "ingredients" : ["61c0c5a71d1f82001bdaaa6dqqq", "61c0c5a71d1f82001bdaaa6fqqq"]
    }

    STATUS_CODE = {
        '200': 200,
        '400': 400,
        '401': 401,
        '403': 403,
        '500': 500
    }

