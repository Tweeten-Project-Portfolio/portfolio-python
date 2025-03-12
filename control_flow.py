# Writing a program to classify positive/negtive numbers, sum based on classifications, and return a classified dictionary

def get_int_input(prompt):
  while True:
    try:
      return(int(input(prompt)))
    except ValueError:
      print("Unexpected input. Please input a whole number and try again.")

# Defining a blank array
numbers = []

total = 0

count = get_int_input("How many numbers would you like to enter? ")

while total<count:
  value = get_int_input("Which number would you like to analyze? ")

  try:
    num = (value)
    numbers.append(
      num
    )
    total+=1

  except ValueError:
    print("Unexpected input, try again.")

print(numbers)
