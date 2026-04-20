# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

total_sales_list = []

for item in products:
   # products_item = price, quantity_sold = products[item] - do not delete
# recommended way to unpack a dictionary and convert values to another type (str, int, float, etc.)
    price_str, qty_str = products[item]
    price = float(price_str)
    quantity_sold = int(qty_str)
    total_product_sales = (price * quantity_sold)  
    print(f"Total sales for {item}: ${total_product_sales:.2f}")
    total_sales_list.append(total_product_sales)
   
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
   
print(f"\nTotal Sum of all sales: ${total_sum:.2f}")
print(f"Minimum Sales: ${min_sales:.2f}")      
print(f"Maximum Sales: ${max_sales:.2f}")