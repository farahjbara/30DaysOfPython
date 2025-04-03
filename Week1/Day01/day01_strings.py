# Day 01 - Working with Strings

# 1️⃣ Declaring Strings
name = "Farah"
greeting = 'Hello, World!'
multiline = """This is 
a multiline 
string."""

print(name)       # Output: Farah
print(greeting)   # Output: Hello, World!
print(multiline)

# 2️⃣ String Concatenation
first_name = "Farah"
last_name = "Jbara"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# 3️⃣ String Formatting
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# 4️⃣  User input
x = input('Enter your name:')
print('Hello, ' + x)

# 5️⃣ String Methods
sentence = "  Python is fun!  "
print(sentence.upper())   # Convert to uppercase
print(sentence.lower())   # Convert to lowercase
print(sentence.swapcase())  # pYTHON IS fUN!  -> Swaps uppercase to lowercase and vice versa
print(sentence.capitalize())  # Python is fun!  -> Capitalizes first letter of sentence
print(sentence.title())   # Python Is Fun!  -> Capitalizes first letter of each word
print(sentence.strip())   # Remove spaces at the beginning and end
print(sentence.lstrip())  # "Hello   " -> Removes spaces from the left
print(sentence.rstrip())  # "   Hello" -> Removes spaces from the right
print(sentence.replace("Python", "Coding"))  # Replace substring
print(sentence.split())   # Split words into a list
print("-".join(sentence)) # Join all items and using a '-' character as separator

text = "Hello, welcome to Python!"

print(text.startswith("Hello"))  # True -> Checks if string starts with "Hello"
print(text.endswith("Python!"))  # True -> Checks if string ends with "Python!"
print(text.find("Python"))  # 18 -> Finds first occurrence index of "Python"
print(text.index("welcome"))  # 7 -> Returns index of substring, raises error if not found
print(text.count("o"))  # 3 -> Counts occurrences of 'o' in the string

word = "python123"

print(word.isalpha())  # False -> Checks if all characters are letters (A-Z, a-z)
print(word.isdigit())  # False -> Checks if all characters are digits (0-9)
print("12345".isdigit())  # True
print(word.isalnum())  # True -> Checks if all characters are letters or digits
print("hello".islower())  # True -> Checks if all letters are lowercase
print("HELLO".isupper())  # True -> Checks if all letters are uppercase
print("   ".isspace())  # True -> Checks if string contains only spaces