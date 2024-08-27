import pytest

from api_methods.courier import Courier
from api_methods.orders import Orders
from generators import UserGenerator

@pytest.fixture(scope='function')
def new_user_data():
    generator = UserGenerator()
    login_pass = {"login": generator.generate_random_string(10),
                  "password": generator.generate_random_string(10),
                  "firstName": generator.generate_random_string(10)}
    return login_pass

@pytest.fixture(scope='function')
def courier():
    courier = Courier()
    return courier

@pytest.fixture(scope='function')
def order():
    order = Orders()
    return order
    
@pytest.fixture(scope='function')
def create_delete_login(new_user_data, courier):
    courier.create_courier(new_user_data["login"], new_user_data["password"], new_user_data["firstName"])
    yield new_user_data
    
    response_login = courier.login_courier_in_system(new_user_data["login"], new_user_data["password"])
    courier.delete_courier(response_login.json()['id'])
