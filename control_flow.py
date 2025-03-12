# Writing a program to classify positive/negtive numbers, sum based on classifications, and return a classified dictionary

def get_int_input(prompt):
  while True:
    try:
      return(int(input(prompt)))
    except ValueError:
      print("Unexpected input. Please input a whole number and try again.")

# defining variables for later analysis

positive_sum = []
negative_sum = []
zero_sum = []

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

if not numbers:
  print("null")
else:
  index = 0
  while index < len(numbers):
    if(numbers[index]>1):
      positive_sum.append(numbers[index])
    elif:
      negative_sum.append(numbers[index])
    else:
      (numbers[index]=0):
        zero_sum.append(numbers[index])
    index+=1

print(positive_sum)
print(negative_sum)
    
print(numbers)
  
