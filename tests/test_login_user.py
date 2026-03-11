import allure
import pytest
from api_methods.user_methods import UserMethods
import requests
from urls import Urls
from data import Data

class TestLoginUser:

    @allure.title('Успешная авторизация пользователя')
    def test_login_user(self, login_user):
        response_login_user = UserMethods.auth_user(login_user)
        response_json = response_login_user.json()
        assert response_login_user.status_code == Data.STATUS_CODE['200']
        assert response_json[Data.SUCCESS] == True

    @allure.title('Ошибка 401 при создании пользователя с некорректным email или паролем')
    def test_login_user_incorrect_field(self, login_user_incorrect_field):
        response_login_user = UserMethods.auth_user(login_user_incorrect_field)
        response_json = response_login_user.json()
        assert response_login_user.status_code == Data.STATUS_CODE['401']
        assert response_json[Data.MESSAGE] == Data.EMAIL_PASSWORD_INCORRECT_ERROR

