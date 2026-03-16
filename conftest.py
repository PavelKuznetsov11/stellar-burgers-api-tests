from api_methods.user_methods import UserMethods
import pytest
from data import Data
from modify_field import ModifyField

@pytest.fixture
def create_user():
    user_data = Data.CREATE_USER_DATA.copy()
    yield user_data
    headers = {
        'Authorization': user_data['token']
    }
    UserMethods.delete_user(headers)

@pytest.fixture
def create_already_exists_user():
    user_data = Data.CREATE_USER_DATA.copy()
    response_create_user = UserMethods.create_user(user_data)
    token = response_create_user.json()['accessToken']
    headers = { "Authorization": token }

    yield user_data

    UserMethods.delete_user(headers)


@pytest.fixture
def login_user():
    user_data = Data.CREATE_USER_DATA.copy()
    response_create_user = UserMethods.create_user(user_data)
    token = response_create_user.json()['accessToken']
    headers = { "Authorization": token }

    yield ModifyField.del_field_name(user_data)

    UserMethods.delete_user(headers)

@pytest.fixture(params=['email', 'password'])
def login_user_incorrect_field(request):
    field = request.param
    user_data = Data.CREATE_USER_DATA.copy()
    response_create_user = UserMethods.create_user(user_data)
    token = response_create_user.json()['accessToken']
    headers = { "Authorization": token }
    if field == Data.EMAIL:
        incorrect_data = ModifyField.incorrect_email_field(user_data)
    else:
        incorrect_data = ModifyField.incorrect_password_field(user_data)

    yield incorrect_data

    UserMethods.delete_user(headers)

@pytest.fixture
def create_order_with_user():
    user_data = Data.CREATE_USER_DATA.copy()
    response_create_user = UserMethods.create_user(user_data)
    token = response_create_user.json()['accessToken']
    headers = { "Authorization": token }
    yield headers

    UserMethods.delete_user(headers)

