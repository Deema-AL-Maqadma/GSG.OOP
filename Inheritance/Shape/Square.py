from Shape import Shape

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return f"The Area = {(self.side**2)}"