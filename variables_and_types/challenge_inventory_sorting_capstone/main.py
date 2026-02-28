# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"

# Slicing
candy1 = items[0:9]
candy2 = items[10:20]
dry_goods = items[21:27]

# Assigning Parsed String into Categories
categories = "Candy Aisle, Pasta Aisle"
category1 = categories[0:11]
category2 = categories[13:24]

# Assigning variables
bubblegum_price = "1.50"
choclate_price = "2.00"
pasta_price = "$5.40"

candy_aisle = category1
pasta_aisle = category2

print("We have " + candy1 + " for $" + bubblegum_price + " in the " + category1)
print("We have" + candy2 + " for $" + choclate_price + " in the " + category1)
print("We have" + dry_goods + " for " + pasta_price + " in the " + category2)

#message = category1 + category2
#print(message)