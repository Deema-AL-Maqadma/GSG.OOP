# The implementation of ( Vending Machine System ) :
from Drink import Drink
from Snack import Snack
from Candy import Candy
#-----------------------------------------------------------------------

# The File of Products
import os
with open ("products.txt","w") as f:
    f.write("Drink,Cola,1.50,500\nSnack,Chips,2.00,250\nCandy,Gummy Bears,1.20,Strawberry\nDrink,Water,1.00,600\nSnack,Cookies,1.75,300")
#-----------------------------------------------------------------------
# To read the information from the file
def load_products(filename):
    products = [] # List Store all objects
    if os.path.exists(filename):
       with open(filename,"r") as f:
            for line in f:
               parts = line.strip().split(',')
               product_type = parts[0]
               name = parts[1]
               price = float(parts[2])
               attribute = parts[3]
            
               if product_type == "Drink":
                  products.append(Drink(name, price, int(attribute)))
               elif product_type == "Snack":
                  products.append(Snack(name, price, int(attribute)))
               elif product_type == "Candy":
                  products.append(Candy(name, price, attribute))
    else:
        print("File Not exits!")

    return products
#-----------------------------------------------------------------------



# Show the menue
def main():
  
  print("--->>> Welcome to the Python Vending Machine!")
  # To display the menue
  products = load_products("products.txt")
  for i, product in enumerate(products, 1):
        print(f"{i}. {product.__class__.__name__} - {product.name}")
    
  
  while True:
        try:
            choice = int(input("\n---> Enter your choice : ")) - 1
            if 0 <= choice < len(products):
                selected = products[choice]
                print(selected.display_info())
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

#-----------------------------------------------------------------------
# Usage
print("*** Deema AL-Maqadma wish you Enjoy ^_^ ***\n")
main()

    