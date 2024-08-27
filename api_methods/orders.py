import allure
from api_methods.base import Base
from data import EndPoints

class Orders(Base):

    @allure.step('Отменяем ранее созданный заказ')
    def cancel_order(self, track):
        body_parametrs = {
            "track": track,
        }
        response = self.put_method("api/v1/orders/cancel", body_parametrs)
        return response

    @allure.step('Получаем список заказов')
    def get_list_orders(self, courierId=None, nearestStation=None, limit=None, page=None):
        param = ""
        if courierId != None:
            param += f"&courierId={courierId}"
        if nearestStation != None:
            param += f"&nearestStation={nearestStation}"
        if limit != None:
            param += f"&limit={limit}"
        if page != None:
            param += f"&page={page}"
        if param != "":
            param = "?" + param[1:]

        response = self.get_mehtod(EndPoints.ORDER + param)
        return response

    @allure.step('Создаем новый заказ')
    def create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color=None):
        body_parametrs = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment
        }
        if color != None:
            body_parametrs["color"] = color
        response = self.post_method(EndPoints.ORDER, body_parametrs)
        return response

