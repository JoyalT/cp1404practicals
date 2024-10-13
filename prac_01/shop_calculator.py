# Get the input for the number of products
item_count = int(input("Enter number of products: "))
total_cost = 0

# Check if the item count is valid
while item_count < 0:
    print("Error: Invalid number of products!")
    item_count = int(input("Enter number of products: "))

# Calculate the total cost of the items
for index in range(item_count):
    product_price = float(input("Enter price of product: "))
    total_cost += product_price

# Apply discount if the total exceeds $100
if total_cost > 100:
    discounted_total = total_cost * 0.9  # 10% discount applied
    print(f"Total cost for {item_count} products is ${discounted_total:.2f}")
else:
    print(f"Total cost for {item_count} products is ${total_cost:.2f}")


