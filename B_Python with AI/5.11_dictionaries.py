# Dictionaries in Python
# A dictionary is an unordered collection of key-value pairs. Dictionaries are defined using curly braces {}, with key-value pairs separated by commas and a colon separating keys and  values.
# Dictionaries are mutable, meaning their contents can be changed after creation. They support various operations such as adding, removing, and accessing elements using keys.
# Dictionaries are commonly used to store and manage 
                               
# Examples of Dictionary operations:        

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)          # Output: Original Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values using keys
print("Name:", my_dict["name"])                 # Output: Name: Alice
print("Age:", my_dict["age"])                   # Output: Age: 25

# Adding a new key-value pair
my_dict["country"] = "USA"
print("Dictionary after adding country:", my_dict) # Output: Dictionary after adding country: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Updating an existing value
my_dict["age"] = 26
print("Dictionary after updating age:", my_dict) # Output: Dictionary after updating age: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair  

# Using del statement
del my_dict["city"]
print("Dictionary after deleting city:", my_dict) # Output: Dictionary after deleting city: {'name': 'Alice', 'age': 26, 'country': 'USA'}                          

# Using pop() method
country = my_dict.pop("country")
print("Popped Country:", country)                # Output: Popped Country: USA
print("Dictionary after popping country:", my_dict) # Output: Dictionary after popping country: {'name': 'Alice', 'age': 26}    

# Iterating over the dictionary
print("Iterating over the dictionary:")
for key, value in my_dict.items():
    print(key + ":", value)                                 

# Output:
# Iterating over the dictionary:
# name: Alice
# age: 26                                   
# Dictionary Methods Reference:
# keys() - Returns a view object containing the keys of the dictionary
# values() - Returns a view object containing the values of the dictionary
# items() - Returns a view object containing the key-value pairs of the dictionary
# get() - Returns the value for a specified key, or a default value if the key is not found
# update() - Updates the dictionary with key-value pairs from another dictionary or iterable
# clear() - Removes all key-value pairs from the dictionary             

# Dictionary methods examples:
my_dict = {"a": 1, "b": 2, "c": 3}
print("Keys:", my_dict.keys())                   # Output: Keys: dict_keys(['a', 'b', 'c'])
print("Values:", my_dict.values())               # Output: Values: dict_values([1, 2, 3])
print("Items:", my_dict.items())                 # Output: Items: dict_items([('a', 1), ('b', 2), ('c', 3)])
print("Get value for key 'b':", my_dict.get("b")) # Output: Get value for key 'b': 2
my_dict.update({"d": 4, "e": 5})
print("Dictionary after update:", my_dict)       # Output: Dictionary after update: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_dict.clear()
print("Dictionary after clear:", my_dict)        # Output: Dictionary after clear: {}
# End of Dictionary operations  



# Which data structure uses key-value pairs?
# Dictionaries use key-value pairs.

# What will dict1.get('key', 'default') return if 'key' does not exist?
# It will return 'default'.

# Which method is used to get all dictionary keys?
# The method used to get all dictionary keys is `keys()`.

# What syntax defines a dictionary comprehension, for example, to create a dictionary of numbers and their squares from 1 to 3?
# The syntax is `{key: value for key, value in iterable}`. For example, `{x: x**2 for x in range(1, 4)}` creates a dictionary of numbers and their squares from 1 to 3.


#What will dict1 = {}; dict1['a'] = 10 result in?
# It will create a dictionary with one key-value pair: {'a': 10}.

# What does items() return in a dictionary?
# The items() method returns a view object containing the key-value pairs of the dictionary as tuples.
