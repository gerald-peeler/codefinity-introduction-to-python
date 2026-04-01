prices = [29.99, 45.50, 12.75, 38.20]

# Discount factor (10% off each item)
discount_factor = [0.10, 0.20, 0.15, 0.05]

# Iterate over the list of prices using range(len())
for cost in range(len(prices)):
    prices[cost] = prices[cost] - (prices[cost] * discount_factor[cost])
    print(f"Updated price for item {cost +1}: ${prices[cost]:.2f}") 


    
