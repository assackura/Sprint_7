import allure

class TestGetListOrder:

    @allure.title('Тест запроса списка заказов')
    @allure.description('Тест проверяет, что API возвращает нсписок заказов')
    def test_get_list_order(self, order):
        response = order.get_list_orders()

        assert response.status_code == 200