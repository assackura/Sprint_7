import pytest
import allure

from api_methods.courier import Courier
from data import ResponseMessages


class TestLoginCourier:

    @allure.title('Тест авторизации курьера')
    @allure.description('Тест проверяет, курьер успешно авторизуется с корректными данными и API возвращает ID курьера')
    def test_login_courier_successfully(self, create_delete_login, courier):
        response_login = courier.login_courier_in_system(create_delete_login["login"], create_delete_login["password"])

        assert response_login.status_code == 200 and response_login.json()['id'] != None

    @allure.title('Тест ошибки при авторизации без одного из полей')
    @allure.description('Тест проверяет, что API вернет ошибку при отсутствии одно или более полей в теле запроса')
    def test_login_courier_without_password_return_error(self, create_delete_login, courier):
        response_login = courier.login_courier_in_system(create_delete_login["login"])

        assert response_login.status_code == 400 and response_login.json()['message'] == ResponseMessages.INSUFFICIENT_DATA_LOGIN

    @allure.title('Тест ошибки авторизации при отсутствующем логине')
    @allure.description('Тест проверяет, что API вернет ошибку при указании несуществующих пары логин/пароль')
    def test_login_not_exists_account(self, courier):
        response_login = courier.login_courier_in_system("no_exists_account", "rekgmdflbdoivmsd")

        assert response_login.status_code == 404 and response_login.json()['message'] == ResponseMessages.LOGIN_IS_NOT_FOUND