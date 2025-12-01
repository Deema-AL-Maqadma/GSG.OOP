class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def getInfo(self):
        return f"->Name = {self.name},->ID = {self.id}"