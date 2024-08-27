import pytest
import allure

from data import ColorsParametrOrder


class TestCreateOrder:

    @allure.title('Тест создания нового заказа')
    @allure.description('Тест проверяет, что API создает новый заказ и возвращает номер заказа')
    @pytest.mark.parametrize(ColorsParametrOrder.parametrs, ColorsParametrOrder.value)
    def test_create_order_color_return_track(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color, order):
        response_order = order.create_order(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color)
        
        order.cancel_order(response_order.json()['track'])

        assert response_order.status_code == 201 and response_order.json()['track'] != None
