grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8), 
    "Eggs": ("Dairy", 5.50, 30), 
    "Bread": ("Bakery", 2.99, 15), 
    "Apples": ("Produce", 150, 50)
    }
  
   
                 
#price_of_eggs = grocery_inventory["Eggs"][1] 
#print(price_of_eggs)
#grocery_inventory.update({"Eggs": ("Dairy", 4.5, 30)})
#print(grocery_inventory)

if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", 4.5, 30)}) 
    print("The updated prince of eggs is: ", grocery_inventory["Eggs"][1])
else:
    print("The price of eggs is reasonable")

