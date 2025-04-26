# range function/method
# 1. strarting point
# 2. condition
# 3. Increament

x=range(1,20,2) # 1,2,3,4,5
print(*x)

# range function/method
# 1. strarting point
# 2. condition
# 3. Increament

x=range(1,20,3) # 1,2,3,4,5
print(*x)

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(list(x))

# am zangi
num:int=2
print("2*1=",num*1)
print("2*2=",num*2)

for num in range(1,11):
    print("num is ",num) # indentation

# Mino Zangi
for num in range(1,11): #1,2,3,4,5
  print("2 x",num,2*num)

for num in range(1,11):
  print(f"2 x {num} ={2*num}") # Fstring

# loops
#1. For loop specific range
#2. While loop if condition true
num=1
while num<10:
  print(num)
  num=num+1

num=1
while num<=10:
  print(num)
  num=num+1

num=1 # H.w
while num<5:
  print(num)
  num=num+1

num=1 # H.w
while num<=5:
  print(num)
  num=num+1

num=1 # H.w
while num<=5:
  print(num)
  num=num+1

start=1
while start<=10:
  print(f"count{start}")
  start=start+1

start=10 # H.W
while start<=20:
  print(f"count{start}")
  start=start+1

num=1
  # while condition infinite
while num<10:
    print(num)

num=1
while num<10: # while loop truse condtion
    print(num)
    num=num+1

user_input=input("Type yor answer please")
print("user_input is ",user_input)

pasword:str="python123"
print("password==python123")

while user_input !=pasword:
  print("type again")

# print("user_input !=password is",user_input !=password)
password="python123"
user_input=""
while user_input != password:
  user_input=input("Type your answer please")
  print("incorrect pasword")

# String
# interger
# boolean
# list
# tupple
numbers=[1,2,3,4,5]
# 0,1,2,3
names1=["ali","bilal","hamza","Oskasha"] # list mutable
names2=("ali","bilal","hamza","Oskasha","Raja") # tuple immutable
name:str="Ali"
name="Bilal"

print(numbers[0])
print([names1])
print("names1 before over write",names1)
print("list first name is",names1[0])
print("tuple first name is", names2[0])
print("tuple first name is", names2[1])

# String
# interger
# boolean
# list
# tupple
numbers=[1,2,3,4,5,6,7,8,9,10,11]
# 0,1,2,3
names1=["ali","bilal","hamza","Oskasha","Raja","Devadas"] # list mutable
names2=("ali","bilal","hamza","Oskasha","Raja") # tuple immutable
name:str="Ali"
name="Bilal"

print(numbers[0]),print(numbers[4]),print(numbers[5])
print([names1])
print("names1 before over write",names1)
print("list fourth  name is",names1[3])
print("tuple fifth name is", names1[4])
print("tuple third name is", names2[2])
print(numbers[10])