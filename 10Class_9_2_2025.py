print("Helow world")

print("hi are you")

user_input=int(input("enter your number"))
try:
  for num in range(1,11):
    print(f"{user_input}*{num}={num*user_input}")
except Exception as error:
  print("please enter valid number")

num=[1,2,3,4]
try:
  result=num[4]
except IndexError:
  print("please provide in valid index")

# # local and Global Variables
# Global variable
num_x = 5
print("num_x outside function:", num_x)

def hello():
    print("num_x inside function:", num_x)
    print("hello, how are you?")

hello()

num_x=10
print("num_x ouside function two",num_x)

def addition(num1: int, num2: int):
    """takes twoparamters and return their sum""" # or under same way
    '''takes twoparamters and return their sum'''
    return num1+num2
result= addition(2,2)
print(addition.__doc__)
print(result)

def subtraction(num1: int, num2: int):
    """takes twoparamters and return their subtraction""" # or under same way
    '''takes twoparamters and return their subtraction'''
    return num1-num2
result= subtraction(8,2)
print(subtraction.__doc__)
print(result)

def multply(num1: int, num2: int):
    """takes twoparamters and return their Multply""" # or under same way
    '''takes twoparamters and return their Multply'''
    return num1*num2
result= multply(8,2)
print(multply.__doc__)
print(result)

def division(num1: int, num2: int):
    """takes twoparamters and return their division""" # or under same way
    '''takes twoparamters and return their division'''
    return num1/num2
result= division(8,2)
print(division.__doc__)
print(result)

def addition(num1: int, num2: int):
    """Takes two parameters and returns their sum"""
    return num1 + num2

result = addition(2, 2)

print(addition.__doc__)  # Prints the docstring
print(result)            # Prints the result: 4

def addition(num1: int, num2: int):
    """takes twoparamters and return their sum"""
    return num1+num2

result= addition(2,2)
print(addition.__doc__)
print(result)

result= addition(4,6)
print(addition.__doc__)
print(result)

# string
# number/interger
# boolean
# list
# Tuple
# Dictonary
# set
## add
## Remove
## discard
##
names_list=["Ali","Heer","Aamir","Ali","Abdullah"]
names_set={"Ali","Manoj Kumar","Aamir","Ali","Abdullah"}
print("names list",names_list[1])
print("names set",names_set)
print("updated names",names_set)
names_set.pop()
names_set.add("Rahim")
names_list.remove("Ali")
names_set.discard("Manoj Kumar")
print("updated names",names_set)

#Final
names_list = ["Ali", "Heer", "Aamir", "Ali", "Abdullah"]


names_set = {"Ali", "Manoj Kumar", "Aamir", "Ali", "Abdullah"}


print("Second name in the list:", names_list[1])

print("Original names set:", names_set)


names_set.pop()


names_set.add("Rahim")


if "Ali" in names_list:
    names_list.remove("Ali")

names_set.discard("Manoj Kumar")
print("Updated names set:", names_set)
print("Updated names list:", names_list)

num_set_1={1,2,3}
num_set_2={3,4,5}

result=num_set_1.union(num_set_2)
result=num_set_1.intersection(num_set_2)
result=num_set_1.difference(num_set_2)
result=num_set_1.symmetric_difference(num_set_2)
print(("result>>>",result))
print(num_set_1)
print(num_set_2)
print(result)

# assiginment
## goglw colab read
### github read
####

import calendar
import calendar
import calendar
cal = calendar.month(2025, 1)
print("Here is the calendar:")
print(f"\033[3m\033[34m{cal}")

import calendar

# User input with error handling
try:
    num = int(input("Enter a Number: "))
    print(f"You Entered: {num}\n")
except ValueError:
    print("Invalid Input! Please enter a valid number.")
    num = None

# Calendar Example
try:
    year = int(input("\nEnter a Year to Display the Calendar: "))
    print(calendar.calendar(year))  # Display full year's calendar
except ValueError:
    print("Invalid Year! Please enter a valid number.")

num1 = int(input('Enter A Number:'))

for i in range(1,30):
    print(f'{num1}x{i} ={num1*i}')
    i +=1