# Mock build of an inventory system for a store that tracks products and quantities

name = string(input("Product name?"))
price = float(input("Product price?"))
quantity = int(input("Product quantity?"))
valid_tags = ["electronics", "household", "grocery", "clothing"]
tags = string(input("Product type?"))

def check_tag(tags)
  if tags in valid_tags
    print(f"Tag valid, proceeding")
else:
    print(f"Error: {tags} not found! Retry required")


