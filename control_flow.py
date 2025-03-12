# Writing a program to classify positive/negtive numbers, sum based on classifications, and return a classified dictionary

def get_int_input(prompt):
  while True:
    try:
      return(input(prompt))
    except ValueError:
      print("Unexpected input. Please input a whole number and try again.")

# Defining a blank array
numbers = []

count = get_int_input("How many numbers would you like to enter?")

for _ in range(count):
  value = get_int_input("What number would you like to analyze?")
  number.append({
    "value": value,
  })

print(numbers)
  
