########### Exercises ###########
'''
Exercise 1 : Timing Decorator
Write a decorator @timing that measures and prints the time taken by a function to execute.
'''
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the decorated function
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to run.")
        return result  # Return the original function's result
    return wrapper


@timing
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
example_function(1_000_000)
'''
Exercises 2: Debugging Decorator
Write @debug to log function calls, arguments, and return values.
'''
def debug(func):
    """A simple decorator to print function calls and arguments"""
    def wrapper(*args, **kwargs):
        # Print function name and arguments
        print(f"Calling {func.__name__} with:")
        print(f"  - Positional arguments: {args}")
        print(f"  - Keyword arguments: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Print the return value
        print(f"{func.__name__} returned: {result}")
        print("-" * 40)  # Visual separator
        
        return result
    return wrapper


@debug
def greet(name, greeting="Hello"):
    """A simple greeting function"""
    return f"{greeting}, {name}!"

@debug
def add_numbers(a, b):
    """Adds two numbers"""
    return a + b

# Test the decorated functions
greet("Alice", greeting="Hi")
add_numbers(3, 5)
'''
Exercise 3: Repeat Call Decorator
Create @repeat(n) that runs the function n times.
'''
def repeat(n):
    """Decorator that repeats a function call n times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi!")
say_hi()
