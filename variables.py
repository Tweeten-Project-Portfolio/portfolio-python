# Demonstrating my knowledge of how variables work and basic variable functions

price = float(input("Please type in the price of the item"))
quantity = int(input("Please type in how many items were purchased"))
tax_rate = float(input("Please type in the effective tax rate"))
discount = float(input("Please type in the discount on this item, if applicable"))

total_before_tax = price*quantity
discounted_price = total_before_tax - (total_before_tax*(discount/100))
tax_amount = discounted_price*(tax_rate/100)
final_price = discounted_price+tax_amount

print(f"Your total is {final_price}")
