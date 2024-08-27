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
