from abc import ABC, abstractmethod

# Polymorphism
# Strategy Pattern


class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, diatance):
        pass


class NormalFare(FareStrategy):
    def calculate_fare(self, diatance):
        return diatance * 10


class SurgeFare(FareStrategy):
    def calculate_fare(self, diatance):
        return diatance * 20
