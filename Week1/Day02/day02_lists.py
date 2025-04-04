# Day 02 - Working with Lists
#Lists are ordered, mutable collections in Python used to store multiple items in a single variable. You can modify them, add or remove elements, and perform many useful operations.

# 1️⃣ Creating Lists
fruits = ["apple","Orange", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 42, 3.14, True]

print(fruits)
print(numbers)
print(mixed)

# 2️⃣ Accessing List Items
print(fruits[0])    # apple
print(fruits[-1])   # cherry -> last item in the list
print(numbers[1:4]) # [20, 30, 40] -> sequence start by index 1 but not include index 4
print(numbers[-4:-1]) # the same previous result 
print(mixed[:1]) # Go up to (but not include) index 1
print(mixed[:-1]) # Go up to (but not include) the last element (-1 refers to the last index)

# 3️⃣ Modifying List Items
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

fruits[1:3] = ["blackcurrant", "watermelon"] # Start at index 1 Up to but not including index 3
print(fruits)

# 4️⃣ Adding Items
fruits.append("orange")         # Adds to end
fruits.insert(1, "kiwi")        # Insert a list item at a specified index
print(fruits)
# -----------------------------------------------------------------------------------------------------------------
tropical = ["mango", "pineapple", "papaya"] # To append elements from another list to the current list
fruits.extend(tropical)
print(fruits)

# 5️⃣ Removing Items
fruits.remove("apple")          # Removes specific item
popped = fruits.pop()           # Removes last item
print("Popped:", popped)
del fruits[0]                   # Deletes item at index 0
#del fruits #The del keyword can also delete the list completely.
print(fruits)

fruits.clear() 
print(fruits)

# 6️⃣ List Methods
print(len(numbers))             # 5
print(min(numbers))             # 10
print(max(numbers))             # 50
numbers.reverse()               # Reverse list in place
print(numbers)

# 7️⃣ Sorting
numbers.sort()                  # Ascending sort
print(numbers)
numbers.sort(reverse=True)      # Descending sort
print(numbers)

# 8️⃣ List Comprehension
squares = [x**2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]
# -----------------------------------------------------------------------------------------------------------------
# 9️⃣ Loop Lists
#Print all items in the list, one by one:
fruits = ['apple', 'banana', 'cherry', 'date', 'Blackberry']
for x in fruits: 
    print(x)

print("--------------------------------------------")
#Print all items by referring to their index number:
for i in range(len(fruits)):
       print(fruits[i])   
 
# Using a for loop with index (enumerate)to get index & value:
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")   
    
# 🔟 List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

newlist = [ x for x in fruits]
print(newlist)
#We can  condition like a filter that only accepts the items that evaluate to True.
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
