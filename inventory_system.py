# Mock build of an inventory system for a store that tracks products and quantities

# Define blank array to store data types in
inventory = []

item = int(input("Input the number of unique items: "))

# For loop for # of items input
for _ in range(item):
  name = (input("Product name? "))
  price = float(input("Product price? "))
  quantity = int(input("Product quantity? "))
  tags = (input("Product type? "))

  inventory.append({
    "name": name,
    "price": price,
    "quantity": quantity,
    "tags": [tag.strip() for tag in tags]
  })

# Calculate discount percentage
discount = float(input("Enter the discount percentage: "))
discount_percent = discount/100

# Define inventory calculation function
def calculate_inventory_value(inventory,discount):
  total_value = 0

  for item in inventory:
    discounted_price = item["price"]*(1 - (discount/100))
    total_value += discounted_price*item["quantity"]

  return total_value

# Final function calculation
final_inventory_value = calculate_inventory_value(inventory, discount)

print(f"The final inventory value after discounts is {final_inventory_value:.2f}")
