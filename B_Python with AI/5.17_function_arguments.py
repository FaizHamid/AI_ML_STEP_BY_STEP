# Function Arguments in Python
# Function arguments are the values that are passed to a function when it is called.
# Python supports several types of function arguments:
# 1. Positional Arguments - Arguments that are passed to a function in the correct positional order.
# 2. Keyword Arguments - Arguments that are passed to a function by explicitly specifying the   parameter name.
# 3. Default Arguments - Arguments that assume a default value if no value is provided during the function call.
# 4. Variable-length Arguments - Allows a function to accept an arbitrary number of arguments. This can be done using *args for non-keyword arguments and **kwargs for keyword arguments.   

# Examples of Function Arguments in Python: 

# 1. Positional Arguments
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")
greet("Alice", 30)                             # Output: Hello, my name is Alice and I am 30 years old.

# 2. Keyword Arguments
greet(age=25, name="Bob")                      # Output: Hello, my name is Bob and I am 25 years old.

# 3. Default Arguments
def introduce(name, country="USA"):
    print(f"My name is {name} and I am from {country}.")
introduce("Charlie")                           # Output: My name is Charlie and I am from USA.
introduce("David", "Canada")                   # Output: My name is David and I am from Canada.

# 4. Variable-length Arguments
def summarize(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
summarize(1, 2, 3, name="Eve", age=28)

# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Eve', 'age': 28}
# End of Function Arguments in Python               
# Function Arguments Types Reference:
# 1. Positional Arguments - Must be passed in the correct order.
# 2. Keyword Arguments - Can be passed in any order by specifying the parameter name.
# 3. Default Arguments - Have default values that are used if no value is provided.
# 4. Variable-length Arguments - Allow functions to accept an arbitrary number of arguments using *args and **kwargs.

# Examples of Function Arguments Types:

# 1. Positional Argument Example
def multiply(a, b):
    return a * b
print("Multiply:", multiply(4, 5))              # Output: Multiply: 20

# 2. Keyword Argument Example
print("Multiply:", multiply(b=6, a=7))          # Output: Multiply: 42

# 3. Default Argument Example
def power(base, exponent=2):
    return base ** exponent
print("Power:", power(3))                        # Output: Power: 9 (3^2)
print("Power:", power(2, 4))                     # Output: Power: 16 (2^4)

# 4. Variable-length Argument Example
def concatenate(*args, **kwargs):            
    result = " ".join(args)
    for key, value in kwargs.items():
        result += f" {key}:{value}"
    return result
print("Concatenate:", concatenate("Hello", "World", lang="English", punctuation="!")) 
# Output: Concatenate: Hello World lang:English punctuation:!
# End of Function Arguments Types Examples      

#What type of argument allows specifying a default value?
# The type of argument that allows specifying a default value is a "Default Argument".  
#What happens if a function is called with fewer arguments than defined?
# If a function is called with fewer arguments than defined, and if the missing arguments have default values, those default values will be used. If there are no default values, a TypeError will be raised.
# What happens if a function is called with fewer arguments than defined?
#Select the correct answer
#A. It executes with None for missing values.    
#B. It raises a TypeError.
#C. It ignores the missing arguments.
# Answer: B. It raises a TypeError.
#C. It executes with default values.


#What syntax allows you to pass multiple arguments in a function?
# The syntax that allows you to pass multiple arguments in a function is using *args for non-keyword arguments and **kwargs for keyword arguments.


