import allure
from data import Data

class ModifyField:


    @staticmethod
    @allure.step('Удаляем поле Имя')
    def del_field_name(data):
        del data['name']
        return data
    

    @staticmethod
    @allure.step('Удаляем поле имя и меняем пароль на некорректный')
    def incorrect_password_field(data):
        incorrect_data = ModifyField.del_field_name(data)
        incorrect_data['password'] = Data.INCORRECT_PASSWORD
        return incorrect_data
    
    @staticmethod
    @allure.step('Удаляем поле имя и меняем email на некорректный')
    def incorrect_email_field(data):
        incorrect_data = ModifyField.del_field_name(data)
        incorrect_data['email'] = Data.INCORRECT_EMAIL
        return incorrect_data
    
