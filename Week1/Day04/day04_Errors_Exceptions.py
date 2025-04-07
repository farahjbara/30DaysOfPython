#Day 04 – Errors & Exceptions 
#Today, you'll dive into errors and exception handling in Python. This is a vital skill for creating robust and user-friendly applications.


# 🛠️ Demonstrating Error and Exception Handling in Python

def divide_numbers():
    try:
        # Asking user for two numbers
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # Performing division
        result = numerator / denominator
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter valid integers.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Execution of the program is complete.")

# Calling the function
divide_numbers()

#📚 Explanation
#try block:

#Contains the code that might raise an exception.

#except block(s):

#Handles specific or general exceptions.

#finally block:

#Executes code that runs regardless of whether an exception occurred or not.

#Key Exceptions Demonstrated:

#ZeroDivisionError: When dividing by zero.

#ValueError: When input isn't a valid integer.

#Generic Exception: Catches unexpected errors.