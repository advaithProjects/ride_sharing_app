from abc import ABC

# Encapsulation
# Inheritance


class User(ABC):
    def __init__(self, user_id, name, phone):
        self._user_id = user_id
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name


class Rider(User):
    def request_ride(self, ride_service, distance):
        return ride_service.create_ride(self, distance)


class Driver(User):
    def __init__(self, user_id, name, phone):
        super().__init__(user_id, name, phone)
        self.available = True
