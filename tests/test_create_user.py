import allure
import pytest
from api_methods.user_methods import UserMethods
import requests
from urls import Urls
from data import Data

class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя')
    def test_create_unique_user(self, create_user):
        response_create_user = UserMethods.create_user(create_user)
        response_json = response_create_user.json()
        create_user['token'] = response_json['accessToken']
        assert response_create_user.status_code == 200
        assert response_json['success'] == True

    @allure.title('Ошибка 403 при создание пользователя с уже занятым email')
    def test_create_already_exists_user(self, create_already_exists_user):
        response_create_user = UserMethods.create_user(create_already_exists_user)
        response_json = response_create_user.json()
        assert response_create_user.status_code == 403
        assert response_json['message'] == 'User already exists'

    @allure.title('Ошибка 403 при создании пользователя без имени')
    def test_create_user_without_name(self):
        user_data = Data.CREATE_USER_DATA_WITHOUT_NAME
        response_create_user = UserMethods.create_user(user_data)
        response_json = response_create_user.json()
        assert response_create_user.status_code == 403
        assert response_json['message'] == "Email, password and name are required fields"

