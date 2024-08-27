import pytest
import allure
from data import UserLoginWithOutParams

class TestCreateCourier:

    @allure.title('Тест создания нового курьера')
    @allure.description('Тест проверяет создание нового курьера с указанием всех необходимы параметров')
    def test_create_courier_return_ok(self, new_user_data, courier):
        response = courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])
        courier.delete_courier_by_login_password(new_user_data["login"], new_user_data["password"])

        assert response.status_code == 201 and response.json()['ok']

    @allure.title('Тест создания дублированного курьера')
    @allure.description('Тест проверяет, что API вернет ошибку, при попытке создать курьера, который уже существует')
    def test_create_two_identical_couriers_return_bad(self, new_user_data, courier):
        response = courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])
        response_double = courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])
        courier.delete_courier_by_login_password(new_user_data["login"], new_user_data["password"])

        assert response_double.status_code == 409 and response_double.json()['message'] == 'Этот логин уже используется'

    @allure.title('Тест создания нового курьера без необходимых данных')
    @allure.description('Тест проверяет, что API вернет ошибку при отсутствии одно или более полей в теле запроса')
    @pytest.mark.parametrize(UserLoginWithOutParams.parametrs, UserLoginWithOutParams.value)
    def test_create_courier_without_params(self, login, password, firstName, courier):
        response = courier.create_courier(login, password, firstName)

        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

