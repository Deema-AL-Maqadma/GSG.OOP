# Super class (Parent)
class Product:

    def __init__(self, name, price):
        self.name=name
        self.price=price

    def  display_info(self):
        return f"""
-> Product Information :
Product: {self.name}, Price:  ${self.price}"""
    
