# 
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def interduce(self):
        print(f"->Name: {self.name}, Age: {self.age}")

class Staff:
    def __init__(self,department,salary):
        self.department=department
        self.salary=salary

    def display_staff(self):
        print(f"->Department: {self.name}, Salary: {self.age}")

class Student(Person):
    def __init__(self, name, age,st_id,major):
        super().__init__(name,age)
        self.st_id=st_id
        self.major=major
    
    def study(self):
        super().interduce()
        print(f"-> Major: {self.major}, Id:{self.st_id}")

    def interduce(self):# override
        print(f"->Major: {self.major}, Id:{self.st_id}")

class Teachre(Person,Staff):
    def __init__(self, name, age,department,salary,em_id,subject):
        super().__init__(name,age)
        super().__init__(department,salary)
        self.em_id=em_id
        self.subject=subject
    
    def teach(self):
        super().interduce()
        print(f"-> ID: {self.em_id}, Subject: {self.subject}")
    def interduce(self):# override
        super().interduce()
        print(f"->ID: {self.em_id}, Subject: {self.subject}")
    

st= Student("Deema",19,"2023","Computer saience")
st.study()
print("#"*50)
st.interduce() # sub
print("#"*50)
teacher=Teachre("Ahmad",20,"IT",2500,"2025","Syber Security")
teacher.interduce() # super
print("#"*50)
teacher.teach()
print("#"*50)
teacher.interduce()