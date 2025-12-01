# استدعاء لكلاس الاوردر لعمل اوبجكت منه للاستفادة منه داخل الميثود
from Order import Order
my_order=Order() # اوبجكت 
class Restoaurant:
     
     # constructor 
    def __init__(self):
        self.menu = []
        self.orders = []

     # method to add order to list
    def addToOrder(self,item_indices): 
         for index in item_indices:
            if 1<= index <=  len(self.menu):
               my_order.addItem(self.menu[index-1])
         self.orders.append(my_order)
         return my_order

    # method to record or placed orders
    def listOrder(self):
        print("---> The current orders : ")
        for order in self.orders:
            i = 0
            for item in self.menu:
               i += 1
               print(f"Order {i}: {item.getName()} (${item.getPrice()}) [{item.getCategory()}]")
            print("The Total : ",my_order.total())


     # method to add item to menu
    def addToMenu(self,item):
        self.menu.append(item)

     # method to record or placed menu
    def listMenu(self):
        print("---> The current menu : ")
        for item in self.menu:
            print(f"{item.getName()} (${item.getPrice()}) [{item.getCategory()}]")

