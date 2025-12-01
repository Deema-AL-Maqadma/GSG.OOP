from Product import Product
# Sub class (Child)

class Candy(Product):
    # constructor
    def __init__(self, name, price,flavor):
        super().__init__(name, price) # call Product(Super) constructor
        self.flavor=flavor

    # Override display_info() 
    def display_info(self):
        return f"{super().display_info()}\nFlavor: {self.flavor}"