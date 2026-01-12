# Data Types in Python
# Python has several built-in data types that are used to store different kinds of data.
# Common data types include:
# 1. int - Integer type, used to represent whole numbers.
# 2. float - Floating-point type, used to represent decimal numbers.
# 3. str - String type, used to represent text.
# 4. bool - Boolean type, used to represent True or False values.
# 5. list - List type, used to store a collection of items in a specific order.
# 6. tuple - Tuple type, similar to lists but immutable (cannot be changed).
# 7. dict - Dictionary type, used to store key-value pairs.
# 8. set - Set type, used to store unique items in an unordered collection.

# Examples of different data types:

# 1. Scalar Data Types - integer, float, string, boolean, complex
# Integer
age = 25
print("Age:", age, "Type:", type(age))         # Output: Age: 25 Type: <class 'int'>
# Float
height = 5.9
print("Height:", height, "Type:", type(height)) # Output: Height: 5.9 Type: <class 'float'>
# String
name = "Alice"
print("Name:", name, "Type:", type(name))       # Output: Name: Alice Type: <class 'str'>
# Boolean
is_student = True
print("Is Student:", is_student, "Type:", type(is_student)) # Output: Is Student: True Type: <class 'bool'>
# Complex Number
compilex_number = 3 + 4j
real_part = compilex_number.real
imaginary_part = compilex_number.imag
print("Real Part:", real_part)                   # Output: Real Part: 3.0
print("Imaginary Part:", imaginary_part)         # Output: Imaginary Part: 4.0              
print("Complex Number:", compilex_number, "Type:", type(compilex_number)) # Output: Complex Number: (3+4j) Type: <class 'complex'>

# 2. Composite or Aggregate Data Types - list, tuple, dictionary, set
# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "Type:", type(fruits)) # Output: Fruits: ['apple', 'banana', 'cherry'] Type: <class 'list'>
# Tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates, "Type:", type(coordinates)) # Output: Coordinates: (10.0, 20.0) Type: <class 'tuple'>
# Dictionary
person = {"name": "Bob", "age": 30}                    
print("Person:", person, "Type:", type(person)) # Output: Person: {'name': 'Bob', 'age': 30} Type: <class 'dict'>

# Data Assignment and Type Checking
x = 42
y = x                     # Assigning the value of x to y       

print("x:", x, "id of x:", id(x), "Typez:", type(x)) # Output: x: 42 Type: <class 'int'>
print("y:", y, "id of y:", id(y), "Typez:", type(y)) # Output: y: 42 Type: <class 'int'>

y = 78
print("After changing y:")
print("x:", x, "id of x:", id(x), "Typez:", type(x)) # Output: x: 42 Type: <class 'int'>
print("y:", y, "id of y:", id(y), "Typez:", type(y)) # Output: y: 78 Type: <class 'int'>
    