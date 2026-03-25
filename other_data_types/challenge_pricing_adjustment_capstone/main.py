# Task 1 - Create Dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8), 
    "Eggs": ("Dairy", 5.50, 30), 
    "Bread": ("Bakery", 2.99, 15), 
    "Apples": ("Produce", 1.50, 50)
    }

# Task 2 - Check & Update Egg Price
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")    
    grocery_inventory.update({"Eggs": ("Dairy", 5.5 - 1, 30)}) 
else:
    print("The price of eggs is reasonable")

# Task 3 Add a New Item = Tomatoes
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", (grocery_inventory))

# Task 4 - Manage Stock - Check and restock Milk
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")          
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 8 + 20)})        
else:
    print("Milk has sufficient stock")

# Task 5 - Remove Item Based on Price
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price")

# Task 6 Final Inventory Printout
print("Updated Inventory: ", (grocery_inventory))
