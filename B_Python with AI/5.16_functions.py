# Functions in Python   
# Functions are reusable blocks of code that perform a specific task.
# They help in organizing code, improving readability, and reducing redundancy.
# Functions can take inputs (parameters) and can return outputs (return values).
# Functions are defined using the def keyword followed by the function name and parentheses (). 
# The function body is indented below the function definition.
# Functions can be called by using their name followed by parentheses ().

# Examples of Functions in Python:  

# Function without parameters and return value
def greet():
    print("Hello, World!")                     # Output: Hello, World!          
greet()                                        # Calling the function           

# Function with parameters
def add(a, b):  
    return a + b                               # Returns the sum of a and b
result = add(5, 3)
print("Sum:", result)                          # Output: Sum: 8          

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent                     # Returns base raised to the power of exponent      
print("Power:", power(4))                      # Output: Power: 16 (4^2)                    
print("Power:", power(2, 3))                   # Output: Power: 8 (2^3)          

# Function with variable number of arguments    
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print("Multiply:", multiply(2, 3, 4))          # Output: Multiply: 24 (2*3*4)          

# Function with keyword arguments
def introduce(name, age):           
    print(f"My name is {name} and I am {age} years old.")                       
introduce(age=30, name="Alice")                # Output: My name is Alice and I am 30 years old.          

# Lambda Function (Anonymous Function)          
square = lambda x: x ** 2
print("Square:", square(5))                     # Output: Square: 25        

# Function Documentation (Docstring)
def subtract(a, b):     
    """Returns the difference of a and b."""     
    return a - b
print("Subtract:", subtract(10, 4))             # Output: Subtract: 6
print("Docstring:", subtract.__doc__)           # Output: Docstring: Returns the difference of a and b.          

# End of Functions in Python        

# Function Types Reference:
# 1. Built-in Functions - Functions that are pre-defined in Python, such as print(), len(), type(), etc.
# 2. User-defined Functions - Functions that are defined by the user using the def keyword.
# 3. Recursive Functions - Functions that call themselves to solve a problem.
# 4. Higher-order Functions - Functions that take other functions as arguments or return functions as results.
# 5. Anonymous Functions (Lambda Functions) - Small, unnamed functions defined  using the lambda keyword.

# Function Types Examples:

# 1. Built-in Function Example                  
print("Length of 'Hello':", len("Hello"))      # Output: Length of 'Hello': 5          

# 2. User-defined Function Example      
def greet_example():
    print("Hello, World!")
greet_example()  # Output: Hello, World!        

# 3. Recursive Function Example
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))          # Output: Factorial of 5: 120          

# 4. Higher-order Function Example
def apply_function(func, value):
    return func(value)  
def square(x):
    return x ** 2           
print("Apply Function (Square of 4):", apply_function(square, 4)) # Output: Apply Function (Square of 4): 16          

# 5. Anonymous Function (Lambda Function) Example
add = lambda a, b: a + b
print("Lambda Function (Add 3 and 5):", add(3, 5)) # Output: Lambda Function (Add 3 and 5): 8

# End of Function Types Examples        
#   Function Methods Reference:
#   __doc__ - Returns the docstring of the function
#   __name__ - Returns the name of the function
#   __code__ - Returns the code object of the function
#   __defaults__ - Returns a tuple containing default parameter values      
#   __closure__ - Returns a tuple containing cells that contain bindings for the function’s free variables  

# Function Methods Examples:
def example_function(param1, param2=10):
    """This is an example function."""
    return param1 + param2
print("Function Name:", example_function.__name__)         # Output: Function Name: example_function
print("Function Docstring:", example_function.__doc__)     # Output: Function Docstring: This is an example function.          
print("Function Code Object:", example_function.__code__)  ## Output: Function Code Object: <code object example_function at 0x... , file "...", line ...>          
print("Function Default Values:", example_function.__defaults__) # Output: Function Default Values: (10,)          
print("Function Closure:", example_function.__closure__)   # Output: Function Closure: None         
# End of Function Methods Examples                  

# End of Functions in Python    

#What happens if a function is called with fewer arguments than defined?
# If a function is called with fewer arguments than defined, and if the missing arguments have default values, those default values will be used. If there are no default values, a TypeError will be raised.

# What happens if a function is called with fewer arguments than defined?
#Select the correct answer
#A. It executes with None for missing values.
#B. It raises a TypeError.
#C. It executes with default values.
#D. It ignores the missing arguments.
# Answer: B. It raises a TypeError.

#What does a function return if there is no return statement?
# If a function does not have a return statement, it returns None by default.

#What is the key difference between return and yield in functions?
# The key difference between return and yield is that return exits the function and sends a value back to the caller, while yield produces a value and pauses the function, allowing it to be resumed later, making it suitable for creating generators.