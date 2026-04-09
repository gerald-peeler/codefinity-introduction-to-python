# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

print("Processing Started...")
min_stock = 30
max_stock = 100

for item in inventory:
    print("Processing", item)
    inventory_item = current_stock, regular_price, discounted_price = inventory[item]   
    print(inventory[item][0])
    if inventory[item][0] <= min_stock:
            print("The current minimum stock level is ", min_stock)
    if inventory[item][0] >= max_stock:
            print("The current minimum stock level is greater than ", min_stock, item, "discount")


  #  print("Current stock of", item, "is", inventory_item[0])
    
    # if inventory[item][0] <= min_stock:
    #     print("Current Stock for", (item), "is", inventory_item[0],               
    #           "and meets or exceeds the minimum stock level. No action required at this time.")  
   



# elseif
    # inventory_item[1] >= min_stock
    # print("Current stock level exceeds minimun stock.")
            
        
        
    
    #if item[0] < min_stock:
     #   print("Current Stock for ", inventory_item) 

    
  #  print(inventory_item)
   # while currrent_stock <= 30:
      #  print("Current Stock is", current_stock[item[0])
        #if currrent_stock > 100:
         #   print("")

    