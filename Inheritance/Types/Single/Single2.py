class Vehicle:
  def start_engine(self):
      print("Starting the engine...")
class Car(Vehicle):
   def start_engine(self):
      print("Car engine starts with a key.")
# Usage
v = Vehicle()
v.start_engine() # Output: Starting the engine...
c = Car()
c.start_engine() # Output: Car engine starts with a key.
