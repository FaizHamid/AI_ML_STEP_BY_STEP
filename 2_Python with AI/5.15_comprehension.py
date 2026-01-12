# Comprehensions in Python
# Comprehensions provide a concise way to create lists, sets, or dictionaries by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items using a condition.
# The main types of comprehensions in Python are:
# 1. List Comprehension - Used to create a new list by applying an expression to each item in an existing list or iterable.
# 2. Set Comprehension - Similar to list comprehension but creates a set, which stores unique items.
# 3. Dictionary Comprehension - Used to create a new dictionary by applying an expression to each item in an existing iterable, typically generating key-value pairs.       

# Examples of Comprehensions in Python: 

# 1. List Comprehension
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]  # Squares each element
print("Original List:", original_list)         # Output: Original List: [1, 2, 3, 4, 5]
print("Squared List:", squared_list)         # Output: Squared List: [1, 4, 9, 16, 25]      

# 2. Set Comprehension
original_list = [1, 2, 2, 3, 4, 4, 5]
squared_set = {x**2 for x in original_list}  # Squares each element and stores in a set (unique values)
print("Original List with Duplicates:", original_list) # Output: Original List with Duplicates: [1, 2, 2, 3, 4, 4, 5]
print("Squared Set:", squared_set)         # Output: Squared Set: {1, 4, 9, 16, 25}      

# 3. Dictionary Comprehension
original_list = ['a', 'b', 'c']         
ascii_dict = {char: ord(char) for char in original_list}  # Creates a dictionary with characters as keys and their ASCII values as values
print("Original List:", original_list)         # Output: Original List: ['a', 'b', 'c']
print("ASCII Dictionary:", ascii_dict)       # Output: ASCII Dictionary:        {'a': 97, 'b': 98, 'c': 99}      

# Comprehensions with Conditions

# List Comprehension with Condition
original_list = [1, 2, 3, 4, 5, 6]
even_squared_list = [x**2 for x in original_list if x % 2 == 0]  # Squares only even numbers
print("Original List:", original_list)         # Output: Original List: [1, 2, 3, 4, 5, 6]
print("Even Squared List:", even_squared_list)   # Output: Even Squared List: [4, 16, 36]      

# Set Comprehension with Condition
original_list = [1, 2, 2, 3, 4, 4, 5, 6]
even_squared_set = {x**2 for x in original_list if x % 2 == 0}  # Squares only even numbers and stores in a set
print("Original List with Duplicates:", original_list) # Output: Original List with Duplicates: [1, 2, 2, 3, 4, 4, 5, 6]
print("Even Squared Set:", even_squared_set)     # Output: Even Squared Set: {4, 16, 36}      

# Dictionary Comprehension with Condition
original_list = ['apple', 'banana', 'cherry', 'date']
length_dict = {fruit: len(fruit) for fruit in original_list if len(fruit) > 5}  # Creates a dictionary for fruits with names longer than 5 characters
print("Original List:", original_list)         # Output: Original List: ['apple', 'banana', 'cherry', 'date']
print("Length Dictionary (names longer than 5 chars):", length_dict) # Output: Length Dictionary (names longer than 5 chars): {'banana': 6, 'cherry': 6}      

# End of Comprehensions in Python   