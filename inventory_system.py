# Mock build of an inventory system for a store that tracks products and quantities

# define error handling

def get_input(prompt):
  while True:
    try:
      return (input(prompt))
    except ValueError:
      print("Unexpected value. Please input a non-numeric value and try again.")

def get_int_input(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Unexpected value. Please input a whole number and try again.")

def get_float_input(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Unexpected value. Please input a numeric value and try again.")


# Define blank array to store data types in
inventory = []

num_item = get_int_input("Input the number of unique items: ")

# For loop for # of num_items input
for _ in range(num_item):
  name = get_input("Product name? ")
  price =get_float_input("Product price? ")
  quantity = get_int_input("Product quantity? ")
  tags =get_input("Product type? ").split(",")

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

  for num_item in inventory:
    discounted_price = num_item["price"]*(1 - (discount/100))
    total_value += discounted_price*num_item["quantity"]

  return total_value

# Final function calculation
final_inventory_value = calculate_inventory_value(inventory, discount)

print(f"The final inventory value after discounts is {final_inventory_value:.2f}")
