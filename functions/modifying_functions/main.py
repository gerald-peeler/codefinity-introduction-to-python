                                # Define a function that applies discounted price after applying the discount
def apply_discount(price, discount=0.05):
                                # Returns the price after applying the discount
    return price * (1 - discount)
    
def apply_tax(price, tax = 0.07):
                                # Returns the price after adding the tax
   return price * (1 + tax)

def calculate_total(price, discount = 0.05, tax = 0.07):
                                # Uses apply_discount() and apply_tax() to return total price
    discounted_price = apply_discount(price, discount = discount)
    total_price = apply_tax(discounted_price, tax = tax)
    return total_price
                                # Calculate - using defaout values
default_total_price = calculate_total(120)
                                # Calculate custom values passed via keyword arguments
custom_total_price = calculate_total(100, discount = 0.10, tax = 0.08)
                                # Output =
print(f"Total cost with default discount and tax: ${default_total_price:.2f}")
print(f"Total cost with custom discount and tax: ${custom_total_price:.2f}")
   