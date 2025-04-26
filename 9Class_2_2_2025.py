Student=["Raja","Dileep"]
student = {"name":"Raja","age":"22","course":"agentic AI"} # Removed leading spaces from this line
print(student["name"])

student = {"name":"Raja","age":"22","course":"agentic AI"}
for key, value in student.items():
  print(f"key {key} and value {value}")

# error handiling
# Three types
#1 abnormale termination
#2 gress full termission
#3 try except
num:int=100
num2:int=10
#result=num/num2
#print(result)

try:
    result=num/num2
    print(result)
except Exception as e:
   print(e)

# Zero division error
# key error
# intex error
# value error
# try error
# import error

list=["aLI","Parveen","Fatima"]
num:int=55
num2:int=11
try:
    result=num/num2
    print(result)
except Exception as e:
   print(e)
   #
try:
    result=num/num2
    print(result)
except ZeroDivisionError:
   print("this is error with index")
except ZeroDivisionError:
   print("this is error with index")
except ZeroDivisionError:
   print("this is error with index")


   # HOME WORK FOR STUDENTS
   # USER_INPUT=INPUT("ENTER YOUR NUMBER")

num=int(input("enter your value"))
for i in range(1,11):
  print(f"{num}*{i}={num*i}")
  try:
    num=num/i
    print(num)
  except Exception as num:
    print("Enter the valid valu"(num))

# 1
num1=int(input("enter your value"))
num2=int(input("enter your value"))
print(num1+num2)

# 2
print("Enter num 1")
num1=int(input())
print("Enter num 2")
num2=int(input())
print(num1+num2)

# 3
print("Enter num 1")
num1=input()
print("Enter num 2")
num2=input()
try:
  print("The sum of these two numers is",
        int(num1)+int(num2))
except Exception as e:
    print(e)
    print("This is very important")

try:
    num = int(input("Enter a Number: "))
    print(f"You Entered: {num}\n")

    print(f"Multiplication Table of {num}:\n")
    for i in range(1, 21):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Invalid Input! Please Enter a Valid Number.")

try:
    num = int(input("Enter a Number: "))
    print(f"You Entered: {num}\n")

    print(f"Multiplication Table of {num}:\n")
    for i in range(1, 21):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Invalid Input! Please Enter a Valid Number.")

list1=["Ali","Parveen","Fatima"]
list2=["Devdas","Sana","Sooraj","Chandar","Heer"]
x=list1
y=list2
z=list1+list2
print(x,y)
print(" ".join(x)),print(" ".join(y))
print(" ".join(z))

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)

# try: # home works
#     user_inp = int(input("please enter a number :\t"))

#     for i in range(1 , 11):
#         print(f"{user_inp} * {i} = {user_inp *i}")
#     num = i/user_inp
#     print(num)
# except Exception as e:
#     print(f"your input is invalid or {e}\n")

def cal():
    user_input1 = int(input("\nplease  Enter 1st number:\t"))
    user_input2 = int(input("\nplease  Enter 2nd number:\t"))
    user_opr = (input("\nplease  Enter Your operation:\n+ , - , * , / :\t"))
    add = "add"
    sub = "subtraction"
    mult = "multiplication"
    div = "division"

    if(user_opr ==add or user_opr ==  "+" or  user_opr == "add".capitalize() or  user_opr == "add".upper() or  user_opr == "addition".capitalize() or user_opr =="addition".upper() ):
        result == user_input1 + user_input2
        print(f"Your final Result is :{result}")

    elif(user_opr ==sub or user_opr ==  "-" or  user_opr == "sub".capitalize() or user_opr =="subtraction".upper() ):
        result = user_input1 - user_input2
        print(f"Your final Result is :{result}")

    elif(user_opr ==mult or user_opr ==  "*" or  user_opr == "multiplication".capitalize() or  user_opr == "multiply" or  user_opr == "multiply". upper() or  user_opr == "multipli".capitalize() or  user_opr == "multiply".lower() or user_opr =="multiplication".upper() ):
        result = user_input1 * user_input2
        print(f"Your final Result is :{result}")

    elif(user_opr ==div or user_opr ==  "/" or  user_opr == "division".capitalize() or user_opr =="division".upper() or user_opr == "Divide" or user_opr == "Divide".upper()  or user_opr == "Divide".lower() ):
        result = user_input1 / user_input2
        print(f"Your final Result is :{result}")
try:
    cal()

except Exception as e:
    print(f" There is an error such as \t{e} \n")

try:
  k1=(input("Enter a Table:"))
  print(k1)
  for i in range (1,11):
    print(f"11*{i}={11*i}")
except Exception as Valuerror:
  print("Valuerror")

# try: # home work2
#     user_inp = int(input("please enter a number :\t"))

#     for i in range(1 , 11):
#         print(f"{user_inp} * {i} = {user_inp *i}")
#     num = i/user_inp
#     print(num)
# except Exception as e:
#     print(f"your input is invalid or {e}\n")

def cal():
    user_input1 = int(input("\nplease  Enter 1st number:\t"))
    user_input2 = int(input("\nplease  Enter 2nd number:\t"))
    user_opr = (input("\nplease  Enter Your operation:= \n + , - , * , / :\t"))
    add =   "add"
    sub = "subtraction"
    mult = "multiplication"
    div = "division"


    if(user_opr ==sub or user_opr ==  "-" or  user_opr == "sub".capitalize() or user_opr =="subtraction".upper() or  user_opr == "subtraction".capitalize() or user_opr =="subtraction".upper() ):
        result = user_input1 - user_input2
        print(f"Your final Result is :{result}")
    elif(user_opr ==add or user_opr ==  "+" or  user_opr == "add".capitalize() or  user_opr == "add".upper() or  user_opr == "addition".capitalize() or user_opr =="addition".upper() ):
        result == user_input1 + user_input2
        print(f"Your final Result is :{result}")


    elif(user_opr ==mult or user_opr ==  "*" or  user_opr == "multiplication".capitalize() or  user_opr == "multiply" or  user_opr == "multiply". upper() or  user_opr == "multipli".capitalize() or  user_opr == "multiply".lower() or user_opr =="multiplication".upper() ):
        result = user_input1 * user_input2
        print(f"Your final Result is :{result}")

    elif(user_opr ==div or user_opr ==  "/" or  user_opr == "division".capitalize() or user_opr =="division".upper() or user_opr == "Divide" or user_opr == "Divide".upper()  or user_opr == "Divide".lower() ):
        result = user_input1 / user_input2
        print(f"Your final Result is :{result}")
try:
    cal()

except Exception as e:
    print(f" There is an error such as \t{e} \n")

# final
def cal():
    try:
        user_input1 = int(input("\nPlease enter the 1st number:\t"))
        user_input2 = int(input("\nPlease enter the 2nd number:\t"))
        user_opr = input("\nPlease enter your operation (+, -, *, /):\t").strip().lower()

        if user_opr in ["-", "subtraction", "sub"]:
            result = user_input1 - user_input2
            print(f"Your final result is: {result}")
        elif user_opr in ["+", "addition", "add"]:
            result = user_input1 + user_input2
            print(f"Your final result is: {result}")
        elif user_opr in ["*", "multiplication", "multiply"]:
            result = user_input1 * user_input2
            print(f"Your final result is: {result}")
        elif user_opr in ["/", "division", "divide"]:
            if user_input2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = user_input1 / user_input2
                print(f"Your final result is: {result}")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the calculator function
cal()

# filter in python
def is_even(n):
  return n%2 == 0

nums=[1,2,3,4,5,6,7,8,9,10]
even_num= filter(is_even,nums)
print(list(even_num))

# filter in python odd
def is_odd(n):
  return n%2 == 0

nums=[1,2,3,4,5,6,7,8,9,10]
odd_num= filter(is_odd,nums)
print(list(odd_num))

number=int(input("enter a number"))

if number%2 == 0:
    print("even")
else:
    print("odd")

def num(n):
    if n%2 == 0:
        print(n, "is a EVEN number")
    else:
        print(n, "is a ODD number")
num(78)

num1 = int(input("Enter a First number: "))
num2 = int(input("Enter a second number: "))
operation = input("Enter your operaton: \n'addition'\n'subtract'\n'multiply'\n'divide':\n ")

def calculator(num1, num2, opeartion):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "Invalid Operation"
print(calculator(num1, num2, operation))