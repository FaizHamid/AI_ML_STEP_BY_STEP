# Return Statement in Python    
# The return statement is used in functions to send a value back to the caller.
# When a function is called, it can perform some operations and then use the return statement to
# return a result. The returned value can then be used or stored in a variable.
# If a function does not have a return statement, it returns None by default.   

# Examples of Return Statement in Python:       

# Function that returns the sum of two numbers
def add(a, b):
    return a + b                               # Returns the sum of a and b
result = add(10, 5)
print("Sum:", result)                          # Output: Sum: 15        

# Function that returns the maximum of two numbers
def maximum(x, y):
    if x > y:
        return x                               # Returns x if x is greater than y
    else:
        return y                               # Returns y if y is greater than or equal to x
max_value = maximum(8, 12)
print("Maximum:", max_value)                   # Output: Maximum: 12        

# Function that returns multiple values
def calculate(a, b):
    sum_value = a + b
    product_value = a * b
    return sum_value, product_value             # Returns both sum and product as a tuple
sum_result, product_result = calculate(4, 6)
print("Sum:", sum_result)                       # Output: Sum: 10
print("Product:", product_result)               # Output: Product: 24        

# Function without a return statement
def greet(name):
    print(f"Hello, {name}!")                    # Prints a greeting message
greet("Alice")                                 # Output: Hello, Alice!        


# Return Statement Reference:
# 1. The return statement is used to exit a function and return a value to the caller.
# 2. A function can have multiple return statements, but only one will be executed based on the flow of the function.
# 3. If no return statement is present, the function returns None by default.
# 4. Functions can return multiple values as a tuple, which can be unpacked into separate variables.
# 5. The return statement can be used to terminate a function early based on certain conditions.        

# Return Statement Examples:       
# 1. Simple Return Example
def square(num):
    return num ** 2                            # Returns the square of num          
print("Square:", square(7))                    # Output: Square: 49        
# 2. Early Return Example
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"                          # Returns "Even" if num is even
    return "Odd"                               # Returns "Odd" if num is odd
print("Check:", check_even_odd(10))            # Output: Check: Even
print("Check:", check_even_odd(7))             # Output: Check: Odd        
# 3. Multiple Return Values Example
def stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return total, count, average               # Returns total, count, and average
numbers_list = [10, 20, 30, 40, 50]
total_value, count_value, average_value = stats(numbers_list)
print("Total:", total_value)                    # Output: Total: 150
print("Count:", count_value)                    # Output: Count: 5
print("Average:", average_value)                # Output: Average: 30.0         
# 4. Return None Example
def do_nothing():
    pass                                      # Function does nothing and returns None
result = do_nothing()
print("Result:", result)                        # Output: Result: None        


# Return Statement Types Reference:
# 1. Simple Return - Returns a single value from the function.
# 2. Early Return - Exits the function early based on a condition.
# 3. Multiple Return - Returns multiple values as a tuple.
# 4. Implicit Return - Functions without a return statement return None by default.

# Return Statement Types Examples:       
# 1. Simple Return Example
def increment(num):
    return num + 1                            # Returns num incremented by 1          
print("Increment:", increment(9))              # Output: Increment: 10        
# 2. Early Return Example
def is_positive(num):
    if num > 0:
        return True                           # Returns True if num is positive
    return False                              # Returns False otherwise
print("Is Positive:", is_positive(5))          # Output: Is Positive: True
print("Is Positive:", is_positive(-3))         # Output: Is Positive: False        
# 3. Multiple Return Example
def min_max(numbers):
    return min(numbers), max(numbers)         # Returns minimum and maximum values
min_value, max_value = min_max([3, 1, 4, 15, 9])
print("Min:", min_value)                       # Output: Min: 1
print("Max:", max_value)                       # Output: Max: 15        
# 4. Implicit Return Example
def print_message(message):
    print(message)                            # Prints the message
result = print_message("Hello, Python!")       # Output: Hello, Python!
print("Result:", result)                        # Output: Result: None        

# End of Return Statement Types Examples    
# Note: The above examples demonstrate various uses of the return statement in Python functions.    
