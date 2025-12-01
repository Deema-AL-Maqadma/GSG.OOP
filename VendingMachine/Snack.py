from Product import Product
# Sub class (Child)

class Snack(Product):
    # constructor
    def __init__(self, name, price,calories):
        super().__init__(name, price) # call Product(Super) constructor
        self.calories=calories

    # Override display_info() 
    def display_info(self):
        return f"{super().display_info()}\nCalories: {self.calories}"