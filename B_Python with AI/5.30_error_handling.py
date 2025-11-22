# Error Handling in Python
# The main error handling techniques in Python are:
# 1. try-except block - Used to catch and handle exceptions that may occur during the execution of a program.
# 2. finally block - Used to execute code that should run regardless of whether an exception occurred or not.
# 3. raise statement - Used to manually raise exceptions in a program.  

# Examples of Error Handling in Python:

# 1. try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  # Output: Error: Division by zero is not allowed. 

# 2. try-except-finally block
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")  # Output: Error: File not found.
finally:
    print("Execution completed.")    # Output: Execution completed.

# 3. raise statement
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")  # Raises ValueError if age is negative
    else:
        print("Valid age:", age)    
try:
    check_age(-5)
except ValueError as ve:
    print("Error:", ve)  # Output: Error: Age cannot be negative.


# End of Error Handling in Python

# Error Handling Reference:
# 1. Exceptions - Events that occur during the execution of a program that disrupt the normal flow of instructions.
# 2. try block - A block of code that is tested for exceptions.
# 3. except block - A block of code that is executed if an exception occurs in the try block.
# 4. finally block - A block of code that is always executed after the try and except blocks, regardless of whether an exception occurred or not.
# 5. raise statement - A statement used to raise exceptions manually in a program.

# Error Handling Examples:
# Example of handling multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Example of using else block with try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)  # Output: Result: <calculated_value> if no exception occurs
# Example of custom exception
class NegativeValueError(Exception):
    pass    
def check_positive(value):
    if value < 0:
        raise NegativeValueError("Value cannot be negative.")
    else:
        print("Positive value:", value)
try:
    check_positive(-10)
except NegativeValueError as nve:
    print("Error:", nve)  # Output: Error: Value cannot be negative.
# End of Error Handling Examples in Python  

# Error Handling Types Reference:
# 1. Syntax Errors - Errors in the syntax of the code that prevent it from being executed
# 2. Runtime Errors - Errors that occur during the execution of the program
# 3. Logical Errors - Errors in the logic of the code that lead to incorrect results
# 4. Built-in Exceptions - Predefined exceptions in Python like ValueError, TypeError, IndexError, etc.
# 5. User-defined Exceptions - Custom exceptions defined by the user using the class keyword.

# Error Handling Types Examples:
# Syntax Error Example
# Uncomment the following line to see a syntax error
# print("Hello World"  # Missing closing parenthesis    
# Runtime Error Example
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Error: List index out of range.")  # Output: Error: List index out of range.
# Logical Error Example
def add_numbers(a, b):
    return a - b  # Logical error: should be a + b
result = add_numbers(5, 3)
print("Result of addition (with logical error):", result)  # Output: Result of addition (with logical error): 2
# Built-in Exception Example
try:
    number = int("abc")  # This will raise a ValueError
except ValueError:
    print("Error: Invalid literal for int().")  # Output: Error: Invalid literal for int().
# User-defined Exception Example
class EvenNumberError(Exception):
    pass    
def check_odd(number):
    if number % 2 == 0:
        raise EvenNumberError("Number is even, expected odd.")
    else:
        print("Odd number:", number)
try:
    check_odd(4)
except EvenNumberError as ene:
    print("Error:", ene)  # Output: Error: Number is even, expected odd.
# End of Error Handling Types Examples in Python    
# Error Handling in Python Completed


#Which statement is used in Python to catch and handle exceptions?
# Select the correct answer


# A. catch

# B. try-except

# C. error handling

# D. raise
# Answer: B. try-except

