# Mock build of an inventory system for a store that tracks products and quantities

# Define blank array to store data types in
inventory = []

item_quantity = int(input("Input the number of unique items: "))

# For loop for # of items input
for _ in range(item_quantity):
  name = string(input("Product name?"))
  price = float(input("Product price?"))
  quantity = int(input("Product quantity?"))
  tags = string(input("Product type?"))

  inventory.append({
    "name": name,
    "price": price,
    "quantity": quantity,
    "tags": [tag.strip() for tag in tags
  })

# Calculate discount percentage
discount = float(input("Enter the discount percentage: "))
discount_percent = discount/100

# Final function calculation
final_inventory_value = calculate_inventory_value(inventory, discount)

print(f"The final inventory value after discounts is {final_inventory_value:.2f}")

# Define a flow control to check for valid tags

def check_tag(tags)
  if tags in valid_tags
    print(f"Tag valid, proceeding")
else:
    print(f"Error: {tags} not found! Retry required")


