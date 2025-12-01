from abc import ABC,abstractclassmethod
class Appliance(ABC):
    def __init__(self,power_rating,brand):
        self.power_rating=power_rating
        self.brand=brand
        
    @abstractclassmethod
    def turn_on(self):
        pass
       
class WashingMachine(Appliance):
    def turn_on(self):
        print(f"brand: {self.brand} ,power_rating: {self.power_rating}")


class Oven(Appliance):
    def turn_on(self):
        print(f"brand: {self.brand} ,power_rating: {self.power_rating}")

wash = WashingMachine(1200,"LG")
oven = Oven(2000,"Samsung")
wash.turn_on()
oven.turn_on()