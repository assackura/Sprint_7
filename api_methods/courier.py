import allure
from api_methods.base import Base
from data import EndPoints

class Courier(Base):

    @allure.step('Авторизуемся в системе')
    def login_courier_in_system(self, login=None, password=None):
        body_parametrs = {}
        if login != None:
            body_parametrs["login"] = login
        if password != None:
            body_parametrs["password"] = password
        response = self.post_method(EndPoints.LOGIN_COURIER, body_parametrs)
        return response

    @allure.step('Создаем курьера')
    def create_courier(self, login, password, firstName):
        body_parametrs = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = self.post_method(EndPoints.CREATE_DELETE_COURIER, body_parametrs)
        return response

    @allure.step('Удаляем курьера по его идентификатору')
    def delete_courier(self, courier_id=None):
        body_parametrs ={
            "id": courier_id
        }
        response = self.post_method(f"{EndPoints.CREATE_DELETE_COURIER}/{courier_id}", body_parametrs)
        return response

    @allure.step('Удаляем курьера по логину и паролю')
    def delete_courier_by_login_password(self, login, password):
        login_response = self.login_courier_in_system(login, password)
        courier_id = login_response.json()["id"]
        response = self.delete_courier(courier_id)
        return response.status_code
