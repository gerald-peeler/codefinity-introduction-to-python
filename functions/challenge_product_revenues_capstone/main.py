                                                # List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]               # price per item
quantities_sold = [150, 200, 100, 50]           # number of items sold

                                                # Calculate revenue for each product
def calculate_revenue(prices, quantities_sold): # Multiplies price by quantity & return a list of revenues
    revenues= []
    for i in range(len(prices)):
        revenues.append(prices[i] * quantities_sold[i])
    return revenues

def formatted_output(revenue_per_product):
    for product, revenue in revenue_per_product:
        print(f"{product} has total revenue of ${revenue:.2f}")

revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenues))
revenue_per_product.sort(key=lambda x: x[1], reverse=True)
formatted_output(revenue_per_product)