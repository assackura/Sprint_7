import requests
import allure
from data import Urls

class Base:

    @allure.step('Отправляем POST запрос')
    def post_method(self, api, body):
        url = Urls.MAIN_URL + api
        response = requests.post(url, data=body)
        return response

    @allure.step('Отправляем DELETE запрос')
    def delete_method(self, api, body):
        url = Urls.MAIN_URL + api
        response = requests.delete(url, data=body)
        return response

    @allure.step('Отправляем GET запрос')
    def get_mehtod(self, api):
        url = Urls.MAIN_URL + api
        response = requests.get(url)
        return response

    @allure.step('Отправляем PUT запрос')
    def put_method(self, api, body):
        url = Urls.MAIN_URL + api
        response = requests.post(url, data=body)
        return response