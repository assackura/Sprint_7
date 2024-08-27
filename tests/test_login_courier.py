import pytest
import allure

from api_methods.courier import Courier


class TestLoginCourier:

    @allure.title('Тест авторизации курьера')
    @allure.description('Тест проверяет, курьер успешно авторизуется с корректными данными и API возвращает ID курьера')
    def test_login_courier_successfully(self, new_user_data, courier):
        courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])

        response_login = courier.login_courier_in_system(new_user_data["login"], new_user_data["password"])

        courier.delete_courier(response_login.json()['id'])

        assert response_login.status_code == 200 and response_login.json()['id'] != None

    @allure.title('Тест ошибки при авторизации без одного из полей')
    @allure.description('Тест проверяет, что API вернет ошибку при отсутствии одно или более полей в теле запроса')
    def test_login_courier_without_password_return_error(self, new_user_data, courier):
        courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])

        response_login = courier.login_courier_in_system(new_user_data["login"])

        get_id_courier = courier.login_courier_in_system(new_user_data["login"], new_user_data["password"])
        courier.delete_courier(get_id_courier.json()['id'])

        assert response_login.status_code == 400 and response_login.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Тест ошибки авторизации при отсутствующем логине')
    @allure.description('Тест проверяет, что API вернет ошибку при указании несуществующих пары логин/пароль')
    def test_login_not_exists_account(self, courier):
        response_login = courier.login_courier_in_system("no_exists_account", "rekgmdflbdoivmsd")

        assert response_login.status_code == 404 and response_login.json()['message'] == 'Учетная запись не найдена'