# Data Structures in Python 
# Python provides several built-in data structures to organize and store data efficiently.
# Common data structures include:
# 1. List - An ordered, mutable collection of items. List is defined using square brackets [], with items separated by commas.      
# 2. Tuple - An ordered, immutable collection of items. Tuple is defined using parentheses (), with items separated by commas.  
# 3. Dictionary - An unordered collection of key-value pairs. Dictionary is defined using curly braces {}, with key-value pairs separated by commas and a colon separating keys and values.
# 4. Set - An unordered collection of unique items.  Set is defined using curly braces {} or the set() function.

# Examples of different data structures:
# 1. List
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)                     # Output: List: [10, 20, 30, 40, 50]
print("First Element:", my_list[0])         # Output: First Element: 10             
my_list.append(60)
print("List after append:", my_list)        # Output: List after append: [10, 20, 30, 40, 50, 60]
my_list.remove(30)
print("List after remove:", my_list)        # Output: List after remove: [10, 20, 40, 50, 60]
# 2. Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)                   # Output: Tuple: (1, 2, 3, 4, 5)
print("Second Element:", my_tuple[1])         # Output: Second Element: 2
# Tuples are immutable, so we cannot add or remove elements
# 3. Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)                # Output: Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Name:", my_dict["name"])            # Output: Name: Alice
my_dict["age"] = 26
print("Dictionary after update:", my_dict)  # Output: Dictionary after update: {'name': 'Alice', 'age': 26, 'city': 'New York'}
my_dict["country"] = "USA"
print("Dictionary after adding country:", my_dict) # Output: Dictionary after adding country: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
# 4. Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)                       # Output: Set: {1, 2, 3, 4, 5}
my_set.add(6)
print("Set after add:", my_set)             # Output: Set after add: {1 , 2, 3, 4, 5, 6}
my_set.remove(3)
print("Set after remove:", my_set)          # Output: Set after remove: {1, 2, 4, 5, 6}
# End of Data Structures in Python  