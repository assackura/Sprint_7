import random

from generators import UserGenerator, PhoneGenerator, DateGenerator


class Urls:

    MAIN_URL = "https://qa-scooter.praktikum-services.ru/"
    
class EndPoints:
    
    LOGIN_COURIER = "api/v1/courier/login"
    CREATE_DELETE_COURIER = "api/v1/courier"
    ORDER = "api/v1/orders"

class ResponseMessages:
    
    LOGIN_ALREADY_EXIST = 'Этот логин уже используется'
    INSUFFICIENT_DATA_CREATE = 'Недостаточно данных для создания учетной записи'
    INSUFFICIENT_DATA_LOGIN = 'Недостаточно данных для входа'
    LOGIN_IS_NOT_FOUND = 'Учетная запись не найдена'


class UserLoginWithOutParams:
    generator = UserGenerator()
    parametrs = 'login, password, firstName'
    value = [
        ["", generator.generate_random_string(10), generator.generate_random_string(10)],
        ["", "", generator.generate_random_string(10)],
        [generator.generate_random_string(10), "", generator.generate_random_string(10)]
    ]

class ColorsParametrOrder:
    generator = UserGenerator()
    phone = PhoneGenerator()
    date = DateGenerator()
    parametrs = "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color"
    value = [
        [generator.generate_random_string(10), generator.generate_random_string(10), generator.generate_random_string(10), 34, phone.generate_random_phone(), random.randint(1,9), date.generate_random_date(), generator.generate_random_string(30), ['BLACK']],
        [generator.generate_random_string(10), generator.generate_random_string(10), generator.generate_random_string(10), 73, phone.generate_random_phone(), random.randint(1,9), date.generate_random_date(), generator.generate_random_string(30), ['GREY']],
        [generator.generate_random_string(10), generator.generate_random_string(10), generator.generate_random_string(10), 76, phone.generate_random_phone(), random.randint(1,9), date.generate_random_date(), generator.generate_random_string(30), ['BLACK', 'GREY']],
        [generator.generate_random_string(10), generator.generate_random_string(10), generator.generate_random_string(10), 144, phone.generate_random_phone(), random.randint(1,9), date.generate_random_date(), generator.generate_random_string(30), None]
    ]