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
        create_user[Data.TOKEN] = response_json[Data.ACCESSTOKEN]
        assert response_create_user.status_code == Data.STATUS_CODE['200']
        assert response_json[Data.SUCCESS] == True

    @allure.title('Ошибка 403 при создание пользователя с уже занятым email')
    def test_create_already_exists_user(self, create_already_exists_user):
        response_create_user = UserMethods.create_user(create_already_exists_user)
        response_json = response_create_user.json()
        assert response_create_user.status_code == Data.STATUS_CODE['403']
        assert response_json[Data.MESSAGE] == Data.USER_ALREADY_EXISTS

    @pytest.mark.parametrize('data', 
                            (Data.CREATE_USER_DATA_WITHOUT_EMAIL, 
                             Data.CREATE_USER_DATA_WITHOUT_NAME, 
                             Data.CREATE_USER_DATA_WITHOUT_PASSWORD))
    @allure.title('Ошибка 403 при создании пользователя без email, имени или пароля')
    def test_create_user_without_field(self, data):
        response_create_user = UserMethods.create_user(data)
        response_json = response_create_user.json()
        assert response_create_user.status_code == Data.STATUS_CODE['403']
        assert response_json[Data.MESSAGE] == Data.REQUIRED_FIELD_ERROR



