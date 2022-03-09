def sale_price(original, discount_percentage):
    # Calculate the sale price here.
    return (1 - discount_percentage / 100) * original

# Write the rest of your program here


product_name = input("Product: ")
original_price = float(input("Original price ($): "))
discount = float(input("Discount (%): "))

print(f"{product_name} on sale for ${round(sale_price(original_price, discount), 2)}.")
