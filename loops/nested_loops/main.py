produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for n1 in groceries:
        for n2 in n1:
            print("Item name: ", n2)