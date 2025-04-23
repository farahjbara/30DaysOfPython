"""
Python Functional programming

This script demonstrates various Python functions and concepts:
- filter()
- zip()
- reduce()
- Lambda expressions
- List comprehensions
- Dictionary comprehensions
"""
from functools import reduce 

# =============================================
# filter() Examples
# =============================================
def filter_examples():
    """Demonstrates the filter() function"""
    print("\n=== filter() Examples ===\n")
    
    # Example 1: Filter odd numbers
    numbers = [1, 2, 3, 4]
    
    def only_odd(item):
        return item % 2 != 0
    
    print("Odd numbers:", list(filter(only_odd, numbers)))
    print("Original list remains unchanged:", numbers)
    
    # Example 2: Filter adults
    ages = [5, 12, 17, 18, 24, 32]
    
    def is_adult(age):
        return age >= 18
    
    adults = filter(is_adult, ages)
    print("Adults:", list(adults))
    
    # Note: Once consumed, filter objects are empty
    print("Filter object is now empty:", list(adults))

# =============================================
# zip() Examples
# =============================================
def zip_examples():
    """Demonstrates the zip() function"""
    print("\n=== zip() Examples ===\n")
    
    names = ['Farah', 'Emilie', 'Bob', 'Lulu']
    scores = [100, 75, 55, 20]
    
    result = zip(names, scores)
    print("Zipped results:", list(result))
    
    # Note: Once consumed, zip objects are empty
    print("Zip object is now empty:", list(result))

# =============================================
# reduce() Examples
# =============================================
def reduce_examples():
    """Demonstrates the reduce() function"""
    print("\n=== reduce() Examples ===\n")
    
    numbers = [1, 2, 3, 4, 5]
    
    def accumulator(num1, num2):
        return num1 + num2
    
    print("Sum of numbers:", reduce(accumulator, numbers))

# =============================================
# Lambda Expressions
# =============================================
def lambda_examples():
    """Demonstrates lambda expressions"""
    print("\n=== Lambda Examples ===\n")
    
    # Example 1: Simple lambda
    short_list = [5, 4, 3]
    my_func = lambda x: sorted(x)
    print("Sorted list:", my_func(short_list))
    print("Original list remains unchanged:", short_list)
    
    # Example 2: Sorting with lambda
    pairs = [(0, 2), (4, 3), (10, -1), (9, 9)]
    pairs.sort(key=lambda x: x[1])
    print("Sorted by second element:", pairs)

# =============================================
# List Comprehensions
# =============================================
def comprehension_examples():
    """Demonstrates list and dictionary comprehensions"""
    print("\n=== Comprehension Examples ===\n")
    
    # List comprehensions
    chars = [x for x in "hello"]
    squares = [x**2 for x in range(5)]
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    
    print("Characters from 'hello':", chars)
    print("Squares of 0-4:", squares)
    print("Squares of even numbers 0-9:", even_squares)
    
    # Dictionary comprehension
    num_dict = {num: num*2 for num in [1, 2, 3]}
    print("Number dictionary:", num_dict)
    
    # Find duplicates with comprehension
    items = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
   
