class Order:
      # constructor
    def __init__(self):
        self.items =[]

       # method to add item to list
    def addItem(self,item):
        self.items.append(item)

       # method to calculate the total
    def total(self):
        total = 0
        for item in self.items:
            total+= item.getPrice()
        return total
    