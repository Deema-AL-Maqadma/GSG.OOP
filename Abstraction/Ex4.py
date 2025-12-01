from abc import ABC, abstractmethod
class Animal(ABC):
   @abstractmethod
   def make_sound(self):
     pass
   @abstractmethod
   def move(self):
     pass
   def describe(self):
     return "Animals are living organisms that move and make sounds."
   
#-----------------------------------------------------------------

class Dog(Animal):
   def make_sound(self):
     return "Bark"
   def move(self):
     return "Runs on four legs"
   
#-----------------------------------------------------------------

class Cat(Animal):
   def make_sound(self):
     return "Meow"
   def move(self):
     return "Jumps gracefully"

#-----------------------------------------------------------------

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    print(f"{animal.__class__.__name__} says {animal.make_sound()} and {animal.move()}")
print(animal.describe())
