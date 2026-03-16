from urls import Urls
import requests
import allure

class UserMethods:

    @staticmethod
    @allure.step('Создаем пользователя')
    def create_user(user_data):
        return requests.post(Urls.CREATE_USER_API, json=user_data)
    
    @staticmethod
    @allure.step('Логин пользователя')
    def auth_user(user_data):
        return requests.post(Urls.AUTH_USER_API, json=user_data)
    
    @staticmethod
    @allure.step('Удаляем пользователя')
    def delete_user(auth_data):
        return requests.delete(Urls.DELETE_USER_API, headers=auth_data)
    
