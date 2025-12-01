# Deema Mohammed AL-Maqadma 
# Introduction to (OOP)
# oop Assignment [ Restoaurant Managment ]
# The Emplementation
from  Restoaurant import Restoaurant 
restoaurant1 = Restoaurant() # Restoaurant object

def add():
  name= input("Enter item name :")
  price= float(input("Enter item price :"))
  category= input("Enter item category :")
  from MenuItem import MenuItem
  manu_item = MenuItem(name,price,category)
  restoaurant1.addToMenu(manu_item)
  print("---> Menu item added successfully !")

def view():
   restoaurant1.listMenu()

def create():
   from Order import Order
   order = Order()
   selection=input("Enter item numbers for the order separated by commas (e.g., 1,2): ").split(",")
   item_indices=[]
   for i in selection:
      if i.strip().isdigit():
         item_indices.append(int(i))
   restoaurant1.addToOrder(item_indices)
   print("-> Order created and added successfully...")

def listOrders():
   restoaurant1.listOrder()

print("\n---> Deema Mohammed AL-Maqadma ... Enjoy ^_^ \n")
exit=False
while exit==False:
  choice=input("""
 *** Welcome to the Restoaurant Management System ! ***
             
 1/ Add menue item
 2/ View menu
 3/ create new order
 4/ list all orders
 5/ Exit
             
 ---> Choose an option :""")

  if choice=="1":
      add()
  elif choice=="2":
      view()
  elif choice=="3":
      create()
  elif choice=="4":
      listOrders()
  elif choice=="5":
      print("\nThank you for using the Restoaurant Management System !\n--->>> Thx ^_^ , see you ...\n")
      exit=True
  else:
    print("InValid choice ! please choose operation from(1-5) ...")
