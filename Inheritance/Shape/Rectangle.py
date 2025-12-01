from Shape import Shape
class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return f"The Area = {(self.width*self.width)}"