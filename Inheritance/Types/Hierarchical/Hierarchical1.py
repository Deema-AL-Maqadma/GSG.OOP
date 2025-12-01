class Animal:
  def sound(self):
     print("Some generic animal sound")
class Dog(Animal):
  def sound(self):
     print("Bark")
class Cat(Animal):
  def sound(self):
     print("Meow")
# Usage
animals = [Dog(), Cat()] # array of objects
for animal in animals:
 animal.sound()