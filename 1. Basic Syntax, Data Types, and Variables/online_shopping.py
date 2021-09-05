# Welcome user
print("Welcome to Python Furniture Shop!")

# Get user input
name = input("Please enter your name: ")
item = input("Please enter what you want to buy: ")
color = input("Color: ")
price = float(input("Price: $"))
quantity = int(input("Quantity: "))

# Process data
total_price = price * quantity

# Output data
print("=" * 30)
print("=" * 30)
print("Your receipt:\n")
print("  Name: " + name.title())
print("  Purchased item: " + color.capitalize() + " " + item.lower())
print("  Price: $" + str(price))
print("  Quantity: " + str(quantity))
print("  Total price: $" + str(total_price))
print("=" * 30)
print("=" * 30)
