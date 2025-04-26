info = {"name": "Aryan", "CGPA": 3.5, "studying": "BS Maths"}
info["name"] = "hayan"
print(info)
print(type(info))

drama1 = "kurulus Usman"
drama2 = "ertugrul ghazi"
print("my favourate dream serail is", drama1)
print(drama2, "is my favourite drama serial after the ", drama1)

list = ["suleman shah", "Etyuguri ghazi", "usman", "Orhan", "naden"]
list.append("Sultan abdul Hameed")
print(list[0], "the dreamer")
print(list[1], "the dreamer")
print(list[2], "the dreamer")
print(list[3], "the dreamer")
print("the tea was fantastic said by", list[3])

# Ternary Operators
num: int = 9
if num > 10:
    print("number is greater than 10")
    num = num + 10
    print("num>>>,num")
else:
    print("number is less than 10")

num = 9
print("number is greater than 10") if num > 10 else print("number is less than 10")

num = 5
num2 = 20 if num < 10 else 5
print("num2>>>", num2)

# Enumerated Function
names = ["Ali", "Abullah", "Aamir"]
print(names[1])
for name in names:
    if name == "Abullah":
        print("Assalamulakum Abullah found")
        print(name)
        break
else:
    print("Abullah not found")

names = ["Ali", "Abullah", "Aamir"]
print(names[1])
index = 0
for name in names:
    print("index", index)
    index += 1
    print(f"name{index}:{name}")

names = ["Ali", "Abullah", "Aamir"]
for index, name in enumerate(names):
    if name == "Abullah":
        print("Assalamulaikum Abdullah")
        print(f"name{index}:{name}")

# Map, Filter, Reduce functions
numbers = [1, 2, 3, 4, 5]

def square(num: int):
    return num * num

new_list = []
for num in numbers:
    print(f"num>>>{num}")
    print("Calling square function")
    num_sqr = square(num)
    print(f"square value{num_sqr}")
    new_list.append(square(num))
    print(new_list)

# Using map
numbers = [1, 2, 3, 4, 5]

def square(num: int):
    return num * num

new_list = list(map(square, numbers))
print("numbers>>>", numbers)
print("new_list>>>", new_list)

# Filter
numbers = [1, 2, 3, 4, 5]

def filter_function(num: int):
    return num > 3

filtered_list = list(filter(filter_function, numbers))
print("numbers>>>", numbers)
print("filtered_list>>>", filtered_list)

# Map example with grades
marks = [77, 97, 64, 85, 55]

def grades(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    elif 50 <= marks < 60:
        return 'E'
    else:
        return 'F'

grade_list = list(map(grades, marks))
print("Exam Score:", marks)
print("grades:", grade_list)

# Reduce
from functools import reduce

def multi(a, r):
    return a * r

numbers = [1, 2, 3, 4, 5]
new_list = reduce(multi, numbers)
print(new_list)

# Map vs Filter demonstration
numbers = [1, 2, 3, 4, 5]

def map_function(num: int):
    return num > 3

map_list = list(map(map_function, numbers))
print("map_list>>>", map_list)  # This will return [False, False, False, True, True]

filter_list = list(filter(map_function, numbers))
print("filter_list>>>", filter_list)  # This will return [4, 5]