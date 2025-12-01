from Product import Product
# Sub class (Child)

class Drink(Product):
    # constructor
    def __init__(self, name, price,volume):
        super().__init__(name, price) # call Product(Super) constructor
        self.volume=volume

    # Override display_info() 
    def display_info(self):
        return f"{super().display_info()}\nVolume: {self.volume}ml"