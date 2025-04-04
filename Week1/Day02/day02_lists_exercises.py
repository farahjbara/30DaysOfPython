#🧪 Day 02 – Evaluation Exercises
# 🚀 Exercise 1
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# 1. Print the first 3 colors
print(colors[0:3])  # ['red', 'green', 'blue']
for x in range(3):
    print(colors[x])  # prints each color individually

# 2. Print the last color
print(colors[-1])  # orange

# 3. Replace "yellow" with "black"
for i in range(len(colors)):
    if colors[i] == "yellow":
        colors[i] = "black"
        break
print(colors)

# 4. Print the list in reverse order
print(colors[::-1])  # new reversed list
# OR (in-place reverse):
colors.reverse()
print(colors)

#------------------------------------------------------------------------------------------------------------------
# 🚀 Exercise 2
numbers = [3, 7, 2, 8, 5, 10, 4, 6]

# 1. Loop through the list and print only even numbers
for x in numbers:
    if x % 2 == 0:
        print(x)

# 2. Calculate and print the sum of all numbers
total = 0
for x in numbers:
    total += x
print("Sum:", total)

# 3. Find the maximum and minimum number
Max = Min = numbers[0]
for x in numbers:
    if x > Max:
        Max = x
    elif x < Min:
        Min = x
print("Max:", Max)
print("Min:", Min)

# 4. Create a new list of all numbers > 5 using a for loop
new_numbers = [x for x in numbers if x > 5]
print("Numbers > 5:", new_numbers)

#------------------------------------------------------------------------------------------------------------------
# 🚀 Exercise 3

# 1. Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# 2. Create another list with only even squares
even_squares = [x for x in squares if x % 2 == 0]
print("Even Squares:", even_squares)

# 3. Create a new list of words with more than 4 letters
words = ["hello", "python", "code", "loop", "devops"]
long_words = [word for word in words if len(word) > 4]
print("Words > 4 letters:", long_words)
#------------------------------------------------------------------------------------------------------------------
# 🚀 Exercise 4

# 1. Ask the user to enter 5 names and store them in a list
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("Names list:", names)

# 2. Sort the list alphabetically
names.sort()
print("Sorted list:", names)

# 3. Remove the last entered name
names.pop()
print("List after removal:", names)

# 4. Print how many names are left
print("Names remaining:", len(names))

# 5. Check if "Farah" is in the list
if "Farah" in names:
    print("Farah is here! 🎉")
else:
    print("Farah is not in the list.")