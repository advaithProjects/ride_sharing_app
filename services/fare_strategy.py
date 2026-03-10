from abc import ABC, abstractmethod

# Polymorphism
# Strategy Pattern


class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class NormalFare(FareStrategy):
    def calculate_fare(self, distance):
        return distance * 10


class SurgeFare(FareStrategy):
    def calculate_fare(self, distance):
        return distance * 20
