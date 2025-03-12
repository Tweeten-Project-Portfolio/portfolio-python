# Demonstrating my knowledge of how variables work and basic variable functions

# Defining helper functions to handle unknown input 

def get_float_input(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Unexpected input. Please enter a numeric value.")

def get_int_input(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Unexpected input. Please enter a whole number.")

# Defining calc functions

price = get_float_input("Please type in the price of the item ")
quantity = get_int_input("Please type in how many items were purchased ")
tax_rate = get_float_input("Please type in the effective tax rate ")
discount = get_float_input("Please type in the discount on this item, if applicable ")

total_before_tax = price*quantity
discounted_price = total_before_tax - (total_before_tax*(discount/100))
tax_amount = discounted_price*(tax_rate/100)
final_price = discounted_price+tax_amount

# Printing final calculations w/ .2f for 2 decimal places
print(f"Your total is {final_price:.2f}")
