from Shape import Shape

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return f"The Area = {3.14*(self.radius**2)}"