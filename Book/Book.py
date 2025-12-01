class Book:

    def __init__(self,name,auther):
        self.name=name
        self.auther=auther

    def getInfo(self):
        return f"->Name : {self.name}, ->Auther :{self.auther}"
    
