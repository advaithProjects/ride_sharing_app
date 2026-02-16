from models.ride import Ride
import uuid


class RideService:
    def __init__(self, fare_strategy):
        self.fare_strategy = fare_strategy
        self.drivers = []
        self.rides = []

    def register_driver(self, driver):
        self.drivers.append(driver)

    def find_available_driver(self):
        for driver in self.drivers:
            if driver.available:
                driver.available = False
                return driver
        return None

    def create_ride(self, rider, distance):
        driver = self.find_available_driver()
        if not driver:
            raise Exception("No drivers available")
        fare = self.fare_strategy.calculate_fare(distance)
        ride = Ride(
            ride_id=str(uuid.uuid4()),
            rider=rider,
            driver=driver,
            distance=distance,
            fare=fare,
        )
        self.rides.append(ride)
        return ride

    # modify
    def get_ride(self, ride_id):
        for ride in self.rides:
            if ride.ride_id == ride_id:
                return ride
        return None
