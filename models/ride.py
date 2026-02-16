class Ride:
    def __init__(self, ride_id, rider, driver, distance, fare):
        self.ride_id = ride_id
        self.rider = rider
        self.driver = driver
        self.distance = distance
        self.fare = fare
        self.status = "ONGOING"

    def complete_ride(self):
        self.status = "COMPLETED"
        self.driver.available = True
