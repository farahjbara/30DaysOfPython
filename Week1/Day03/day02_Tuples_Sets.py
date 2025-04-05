# Day 03 – Tuples & Sets
#✅ Concepts Covered:
#Tuples: creation, indexing, immutability

#Sets: creation, uniqueness, operations (union, intersection, difference)

#Use cases and best practices
#🧪 Tuples – Immutable Lists
#Tuple unpacking
# Creating a tuple
colors = ("red", "green", "blue")
print(colors)
print(type(colors))

# Accessing elements
print(colors[0])     # red
print(colors[-1])    # blue

# Tuple is immutable
# colors[1] = "yellow"  ❌ This will raise an error

# Tuple with one item (comma is required!)
single = ("only_one",)
print(type(single))  # tuple

# Tuple unpacking
a, b, c = colors
print(a)  # red
print(b)  # green
print(c)  # blue

# Nested tuples
nested = ("apple", (1, 2, 3))
print(nested[1][2])  # 3

#🧪 Sets – Unordered, Unique Elements
# Creating a set
fruits = {"apple", "banana", "orange", "apple"}
print(fruits)  # {'banana', 'orange', 'apple'} – duplicates removed!

# Add an item
fruits.add("kiwi")
print(fruits)

# Remove an item
fruits.remove("banana")
print(fruits)

# Check if item exists
print("apple" in fruits)  # True

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)        # {1, 2, 3, 4, 5, 6}
print("Intersection:", set1 & set2) # {3, 4}
print("Difference:", set1 - set2)   # {1, 2}

# Convert list to set to remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # [1, 2, 3, 4, 5]
#--------------------------------------------------------------
#🎯 Example 1: Tuple with Mixed Data Types
info = ("Farah", 25, True)
print(info)
print(f"Name: {info[0]}, Age: {info[1]}, Active: {info[2]}")


#🎯 Example 2: Tuple inside a List
people = [("Alice", 30), ("Bob", 28), ("Farah", 25)]
for name, age in people:
    print(f"{name} is {age} years old")
