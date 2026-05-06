# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
                                    # Create a copy so the original list stays untouched
    prices_copy = prices.copy()

                                    # Apply 10% discount to prices over $2.00
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90  # store the discounted price

    return prices_copy

                                    # Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

                                    # Print each updated price
for index in range(len(updated_prices)):
    print(f"Updated product prices: product {index + 1}: ${updated_prices[index]:.2f}")