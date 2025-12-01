class Father:
  def skills(self):
     print("Gardening, Programming")
class Mother:
  def skills(self):
     print("Cooking, Art")
class Child(Father, Mother):
  def skills(self):
     print("Child's own skills:")
     super().skills() # This will follow MRO (Method Resolution Order)
     print("Sports")
# Usage
c = Child()
c.skills()
#  Python uses the Method Resolution Order (MRO) to decide whichskills() method to call first when super().skills() is used. Since Father appears before Mother in theinheritance list of Child, Father.skills() is called.
print(Child.__mro__)
# Output: (<class '__main__.Child'>, <class '__main__.Father'>, <class'__main__.Mother'>, <class 'object'>)
