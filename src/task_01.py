from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def __repr__(self):
        return f"{self.make} {self.model} {self.spec}"

    @abstractmethod
    def start_engine(self):
        raise NotImplementedError


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Car Engine is running")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Motorcycle Engine is running")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model, spec) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model, spec) -> Motorcycle:
        pass


class USVehicleFatory(VehicleFactory):
    def create_car(self, make, model, spec="(US Spec)") -> Car:
        return Car(make, model, spec)

    def create_motorcycle(self, make, model, spec="(US Spec)") -> Motorcycle:
        return Motorcycle(make, model, spec)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model, spec="(EU Spec)") -> Car:
        return Car(make, model, spec)

    def create_motorcycle(self, make, model, spec="(EU Spec)") -> Motorcycle:
        return Motorcycle(make, model, spec)


# Використання
us_facrtory = USVehicleFatory()
vehicle_us = us_facrtory.create_car("Ford", "Mustang")
vehicle_us.start_engine()
print("Launch US Vehicle: ", vehicle_us)

us_facrtory = EUVehicleFactory()
vehicle_eu = us_facrtory.create_motorcycle("Audi", "R8")
vehicle_eu.start_engine()
print("Launch EU Vehicle: ", vehicle_eu)
