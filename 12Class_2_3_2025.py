# Recursive Function/Recursion
def count_down(num: int)-> int:
  if num ==0:
    print("Count down done")
  else:
    print("num>>>",num) # 10->9
    count_down(num-1) # 9-1 ->8


count_down(10)

# lambda function in python
def add(a:int,b:int):
  return a+b

result=add(5,6)
print(result)
result=add(5,6)
print(result)

def add(a:int,b:int):
  return a+b

result=add(5,6)
print(result)
result=add(5,6)
print(result) # Changed 'revse_result' to 'result'

# def add(a:int,b:int)-int:
#  return a+b

# Lambda function to add two numbers
add = lambda a, b: a + b

result = add(5, 6)
print("result>>>", result)  # Output: result>>> 11

# If you want to calculate n = num*num - 1 using lambda:
num = 5  # First you need to define num
calculate = lambda x: x*x - 1
n = calculate(num)
print("n>>>", n)  # Output: n>>> 24 (when num is 5)

# OS operting System
import os
print("cwd",os.getcwd()) #cwd-> current working directory
print("list dir",os.listdir)

if os.path.exists("text.txt"):
    file = open("text.txt", "r")
    print("files>>>", file)
    print(file.read())
    file.close()
else:
    print("The file 'text.txt' does not exist in the current directory.")

file=open("text2.txt","w")
file.write(" I am fine ")
file.close()

numberGames = {}
numberGames[(1,2,4)]=8
numberGames[(4,2,1)]=10
numberGames[(1,2)]=12
sum=0
for k in numberGames:
  sum += numberGames[k]
print(len(numberGames)+sum)

numberGames = {}
numberGames[(1,2,4)]=101
numberGames[(4,2,1)]=101
numberGames[(1,2)]=101
numberGames[(1,3)]=101
numberGames[(1,3,4)]=101
sum=0
for k in numberGames:
  sum += numberGames[k]
print(len(numberGames)+sum)