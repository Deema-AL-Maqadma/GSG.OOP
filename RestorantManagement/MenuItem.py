class MenuItem:
     # consructor
    def __init__(self,name,price,category):
        self.__name=name
        self.__price=price
        self.__category=category

      # Setters for privete attributes
    def setName(self,name):
        self.__name=name
    def setPrice(self,price):
        self.__price=price
    def setCategory(self,category):
        self.__category=category

      # Getters
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getCategory(self):
        return self.__category
    
    #method to show the details
    def __str__(self):
        return f"{self.getName()} (${self.getPrice}) [{self.getCategory}]"

    