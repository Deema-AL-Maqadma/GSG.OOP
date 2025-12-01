# implementation
from Circle import Circle
from Square import Square
from Rectangle import Rectangle

# print the area shap
def descripe_shape(Shape):
    print(type(Shape).__name__)
    print(Shape.area())

c=Circle(5)
s=Square(4)
r=Rectangle(6,8)
shapes=[c,s,r] # array of objects

for shape in shapes: 
   descripe_shape(shape)
   print("*"*50)

