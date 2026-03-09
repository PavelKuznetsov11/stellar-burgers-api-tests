from urls import Urls
import requests
import allure

class OrderMethods:

    @staticmethod
    @allure.step('Создаем заказ с ингредиентами без авторизации пользователя')
    def create_order_without_user(order_data):
        return requests.post(Urls.CREATE_ORDERS_API, json=order_data)
    
    @staticmethod
    @allure.step('Создаем заказ с ингредиентами и авторизации пользователем')
    def create_order_with_user(auth, order_data):
        return requests.post(Urls.CREATE_ORDERS_API, headers=auth, json=order_data)
    
    @staticmethod
    @allure.step('Создаем заказ без авторизации пользователя и ингредиентов')
    def create_order_without_user_and_ingredients():
        return requests.post(Urls.CREATE_ORDERS_API)
    
