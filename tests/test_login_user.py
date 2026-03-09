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
        assert response_login_user.status_code == 200
        assert response_json['success'] == True

    @allure.title('Ошибка 401 при создании пользователя с некорректным паролем')
    def test_login_user_incorrect_password(self, login_user_incorrect_password):
        response_login_user = UserMethods.auth_user(login_user_incorrect_password)
        response_json = response_login_user.json()
        assert response_login_user.status_code == 401
        assert response_json['message'] == 'email or password are incorrect'

