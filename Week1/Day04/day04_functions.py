# Day 04 – Python Functions
#✅ What is a Function?
#A function is a reusable block of code that performs a specific task. Instead of writing the same code over and over, we wrap it in a function and call it whenever we need it.
# 1️⃣ Defining a Function
def greet():
    print("Hello, world")
    
greet()
# 2️⃣ Function with Parameters
name = input("Enter your name:")
def say_hello(name):
    print(f"Hello, {name}!")
    
say_hello(name)
#------------------------------------------
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest
greet("Farah")  # Hello, Farah


# 3️⃣ Function with Return Value
def Multiplication(a,b):
    return (a * b)
print(Multiplication(5, 5))
    

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
# 4️⃣ def total_sum(*args):
def total_sum(*nb):
    return sum(nb)

print(total_sum(1, 2, 3, 4))  # 10


# 6️⃣