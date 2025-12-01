from abc import ABC,abstractclassmethod
class Employee(ABC):
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
        
    @abstractclassmethod
    def calculate_salary(self):
        pass
    @abstractclassmethod
    def get_benefits(self):
        pass
       
class FullTimeEmployee(Employee):
    def __init__(self,name, id, salary,bunas):
        super().__init__(name, id, salary)
        self.bunas=bunas

    def calculate_salary(self):
        print(f"Salary = {self.salary+self.bunas}")

    def get_benefits(self):
        print(f"Very Good")



class PartTimeEmployee(Employee):
        def __init__(self,name, id, salary,hours,price):
          super().__init__(name, id, salary)
          self.hours=hours
          self.price=price

        def calculate_salary(self):
             print(f"Salary = {self.hours*self.price}")

        def get_benefits(self):
             print(f"Good")

full = FullTimeEmployee("Ali",100,200,500)
part = PartTimeEmployee("Deema",100,200,15,500)
full.calculate_salary()
full.get_benefits()
print("*"*50)
part.calculate_salary()
part.get_benefits()