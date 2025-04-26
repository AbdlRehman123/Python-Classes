print("Hi")
# condition Truse/Flase
if True:
# if False:
  print("condition is true")
else:
  print("condition is False")

#comparison operators True/Flase
num:int=10

print(num< 10)

num:int=100

print(num> 0 and num< 100)

name:str="Sir Sohaib"

if name=="Sir Sohaib":
    print("Welcome Sir Sohaib")
else:
    print("App Kon")

time_of_day: str="Morning"
if time_of_day=="Morning":
  print("Good Afternoon")
elif time_of_day=="morning":
  print("Good Morning")
else:
  print("Good Night")

sector:str="Government"
if sector=="Government":
  print("NGOs")
elif sector=="Government":
  print("Government")
else:
  print("Private")

name="Sir Ali"
numbers:list[int]=[0,1,2]
# index 0 1 2 3,
namesA=["Sir Aneeq", "Sir Sohaib","Sir Sami"]
print(namesA[1])
print(namesA)

name="Sir Ali"
numbers:list[int]=[0,1,2,3,4,5,6,7,8,9,10]
# index 0 1 2 3,4,5,6,7,8,9,10
names=["Sir Aneeq", "Sir Sohaib","Sir Sami","Rabeel","Paras"]
print(names[0])
print(names[1],names[1])
print(names)
print(numbers[10],numbers[7])
print(numbers)

#print (range(0,5)
range(0,5)
#stratin point
# condtion
# increment
numbers:list[int]=[1,2,3,4,5]
#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])
#print (range(0,5)
range(0,5)
#stratin point
# condtion
# increment
numbers:list[int]=[1,2,3,4,5]
names=["grapes","orange"]
#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])
#for variable in iterable:
for num in numbers:
  print("num is", num)
  print("names are",names)

rollNo=int(input("Enter Roll No"))
name=input("Enter Name:")
gender=input("Enter Gender")
age=int(input("Enter Age"))
standard=int(input("Enter Class"))
english=int(input("Enter English70 Marks"))
maths=int(input("Enter Maths Marks"))
science=int(input("Enter Science Marks"))
urdu=int(input("Enter Urdu Marks"))
islamiat=int(input("Enter Islamiat Marks"))
obtained_marks=english+maths+science+urdu+islamiat
percentage=obtained_marks/500*100

print("--------------STUDENT'S MARKSHEET---------------")

print("Your Roll Number is:",rollNo)
print("Your Name is:",name )
print("Your Gender is:",gender)
print("Your Age is:",age)
print("Your Class is:",standard)
print("Total Marks are:, 500")
print("Obtained Marks are:,obtained")
print("Percentage is:",percentage)

english=int(input("Enter English Marks"))
maths=int(input("Enter Maths Marks"))
science=int(input("Enter Science Marks"))
urdu=int(input("Enter Urdu Marks"))
islamiat=int(input("Enter Islamiat Marks"))
total=english+maths+science+urdu+islamiat
print("Total Marks of 5 subject is", total)
percentage=total/500*100
print("Percentage is:",percentage)
if english>=33 and maths>=33 and science>=33 and urdu>=33 and islamiat>=33:
  print("You are pass")
else:
  print("You are fail")

english=int(input("Enter English Marks"))
maths=int(input("Enter Maths Marks"))
science=int(input("Enter Science Marks"))
urdu=int(input("Enter Urdu Marks"))
islamiat=int(input("Enter Islamiat Marks"))
total=english+maths+science+urdu+islamiat
print("Total Marks of 5 subject is", total)
percentage=total/500*100
print("Percentage is:",percentage)
if english<=33 and maths<=33 and science<=33 and urdu<=33 and islamiat<=33:
  print("You are fail")
else:
  print("You are pass")

#Q. Write a programme to calculate the grade of a student.

marks=int(input("Enter your Marks(0 to 100)\n"))
if marks>=90:
  grade="Excelent"
elif marks>=80:
  grade="A++"
elif marks>=70:
  grade="A"
elif marks>=60:
  grade="B"
elif marks>=50:
  grade="C"
elif marks>=40:
  grade="D"
else:
  grade="Fail"
print("Your Grade is:",grade)

#Q. Write 3 table
for i in range(1,11):
  print("3 x",i,"=",3*i)

# Q. Write 9 table
for i in range(0, 11):
    print("9 x", i, "=", 9 * i)

print("\n")  # Add a line break for better readability

# Full multiplication table from 1 to 10 (fixed the formatting error)
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
    print()  # Adds a line break between tables

# 2 Table
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

print("\n")  # Separate output

from plistlib import Image

try:
    img = Image.open('C:/Users/You/Desktop/Laptop.jpg')  # Replace with your actual image path
    img.show()
except FileNotFoundError:
    print("Image file 'Laptop.jpg' not found.")

# Colored Text Output
print("\033[1;37;48m Python \n")
print("\033[1;36;48m Python \n")
print("\033[1;35;48m Python \n")
print("\033[1;34;48m Python \n")
print("\033[1;33;48m Python \n")
print("\033[1;32;48m Python \n")
print("\033[1;31;48m Python \n")

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE + "My name is Rimsha Parveen" + Fore.YELLOW + " I am your AI Student")