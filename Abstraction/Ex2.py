from abc import ABC,abstractclassmethod
class Vehicle(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    @abstractclassmethod
    def start_engine(self):
        pass
    @abstractclassmethod
    def stop_engine(self):
        pass
       
class Car(Vehicle):
    def start_engine(self):
        print(f"Start/ make: {self.make} ,model: {self.model},year: {self.year}")

    def stop_engine(self):
        print(f"Stop/ make: {self.make} ,model: {self.model},year: {self.year}")



class Bike(Vehicle):
    def start_engine(self):
        print(f"Start/ make: {self.make} ,model: {self.model},year: {self.year}")

    def stop_engine(self):
        print(f"Stop/ make: {self.make} ,model: {self.model},year: {self.year}")

car = Car("Toyota","Camry",2022)
bike = Bike("Harly_Davidson","sporter",2021)
car.start_engine()
car.stop_engine()
bike.start_engine()
bike.stop_engine()