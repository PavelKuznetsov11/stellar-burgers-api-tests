import allure
import pytest
from api_methods.order_methods import OrderMethods
from data import Data


class TestCreateOrder:

    @allure.title('Успешное создание заказа с ингредиентами ' \
    'и авторизацией пользователя')
    def test_create_order_with_user_success(self, create_order_with_user):
        response_create_order = OrderMethods.create_order_with_user(
            create_order_with_user, Data.INGREDIENTS)
        response_json = response_create_order.json()
        assert response_create_order.status_code == Data.STATUS_CODE['200']
        assert response_json[Data.SUCCESS] == True 
        assert response_json[Data.ORDER][Data.OWNER]

    @allure.title('Успешное создание заказа с ингредиентами ' \
    'и без авторизации пользователя')
    def test_create_order_without_user_success(self):
        response_create_order = OrderMethods.create_order_without_user(
            Data.INGREDIENTS)
        response_json = response_create_order.json()
        assert response_create_order.status_code == Data.STATUS_CODE['200']
        assert response_json[Data.SUCCESS] == True

    @allure.title('Ошибка 400 при создании заказа ' \
    'без ингредиентов и авторизации пользователя')
    def test_create_order_without_ingredients_and_user_failed(self):
        response_create_order = OrderMethods.create_order_without_user_and_ingredients()
        response_json = response_create_order.json()
        assert response_create_order.status_code == Data.STATUS_CODE['400']
        assert response_json[Data.MESSAGE] == Data.MESSAGE_ERROR_INGREDIENT

    @allure.title('Ошибка 500 при создании заказа без авторизации пользователя' \
    'и некорректным хэшем ингредиентов')
    def test_create_order_with_incorrect_hash_ingredient_failed(self):
        response_create_order = OrderMethods.create_order_without_user(
            Data.INCORRECT_HASH_INGREDIENTS)
        assert response_create_order.status_code == Data.STATUS_CODE['500']
        assert Data.SERVER_ERROR in response_create_order.text

