"""
Python Decorators Challenge

This script demonstrates Python decorators with practical examples:
- Basic permission checking decorator
- Performance measurement decorator
- Decorators with parameters
- Real-world use cases

"""

from time import time

# =============================================
# Example 1: Basic Permission Decorator
# =============================================
def permission_example():
    """Demonstrates a basic permission checking decorator"""
    print("\n=== Permission Decorator Example ===\n")
    
    # User data
    user = {
        'id': 1,
        'name': 'Farah',
        'role': 'admin'  # Try changing to 'user' to see different behavior
    }

    def check_permission(func):
        """Decorator to check user permissions before executing function"""
        def wrapper():
            if user['role'] == 'admin':
                return func()
            else:
                print(f"Access denied. {user['name']} is not an administrator.")
        return wrapper

    @check_permission
    def delete_database():
        """Dangerous operation requiring admin privileges"""
        print('Database deleted!')

    # Test the decorated function
    delete_database()

# =============================================
# Example 2: Performance Measurement Decorator
# =============================================
def performance_example():
    """Demonstrates a performance timing decorator"""
    print("\n=== Performance Decorator Example ===\n")

    def performance(fn):
        """Decorator to measure function execution time"""
        def wrapper(*args, **kwargs):
            t1 = time()
            result = fn(*args, **kwargs)
            t2 = time()
            print(f"Execution took {t2 - t1:.4f} seconds")
            return result
        return wrapper

    @performance
    def long_operation():
        """A time-consuming operation"""
        for i in range(1_000_000):
            i * 5

    # Test the decorated function
    print("Running long operation...")
    long_operation()

# =============================================
# Example 3: Decorator with Parameters
# =============================================
def parametrized_decorator_example():
    """Demonstrates a decorator that accepts parameters"""
    print("\n=== Parametrized Decorator Example ===\n")

    def repeat(num_times):
        """Decorator factory that accepts parameters"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(num_times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

    @repeat(num_times=3)
    def greet(name):
        print(f"Hello, {name}!")

    # Test the decorated function
    greet("Alice")

# =============================================
# Why Use Decorators?
# =============================================
"""
Decorators are powerful because they:
1. Allow adding functionality to existing code without modification
2. Help separate concerns and keep code DRY (Don't Repeat Yourself)
3. Enable clean, readable syntax for cross-cutting concerns like:
   - Logging
   - Authentication
   - Performance measurement
   - Caching
   - Input validation
"""

# =============================================
# Main Execution
# =============================================
if __name__ == "__main__":
    permission_example()
    performance_example()
    parametrized_decorator_example()