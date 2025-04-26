# Mutable vs Immutable Data Types

# Mutable Data Types (can be changed)
# - list
# - dictionary
# - set

# Immutable Data Types (cannot be changed)
# - string
# - integer
# - boolean
# - tuple
# - float
# - None

# Example of mutable list
dishes = ["samose", "pakore", "fruit chat"]
dishes.append("ice cream")
print(dishes)  # Output: ['samose', 'pakore', 'fruit chat', 'ice cream']

# Example of immutable string
name: str = "Aneeq Khatri"
number: int = 20
print(name)  # Output: Aneeq Khatri

# == vs is operator
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(list1 == list2)  # True (values are equal)
print(list1 is list2)  # False (different objects in memory)

list2 = list1
print(list1 == list2)  # True
print(list1 is list2)  # True (same object)

# String interning example
name1 = "Aneeq how are you? i am fine"
name2 = "Aneeq how are you? i am fine"
print(name1 is name2)  # Depends on Python implementation (may be True or False)

# Reference example
list1 = [1, 2, 3, 4, 5]
list2 = list1  # list2 references the same object as list1
list1.append(6)
print("list2>>>", list2)  # Output: [1, 2, 3, 4, 5, 6]

# List comprehension examples
# Square numbers
def get_sqr_list(n: int):
    sqr_list = [num * num for num in range(n)]
    print("sqr_list>>>", sqr_list)

get_sqr_list(5)  # Output: [0, 1, 4, 9, 16]

# Even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4