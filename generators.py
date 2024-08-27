import datetime
import random
import string


class UserGenerator:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

class PhoneGenerator:

    def generate_random_phone(self):
        phone = "+7"
        for i in range(10):
            phone += str(random.randint(0, 9))
        return phone

class DateGenerator:

    def generate_random_date(self):
        return f"{datetime.date.today().year}-0{random.randint(1, 12)}-{random.randint(10, 28)}"

