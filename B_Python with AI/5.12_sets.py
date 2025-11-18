# Sets in Python                            
# A set is an unordered collection of unique items. Sets are defined using curly braces {} or the set() function.
# Sets are mutable, meaning their contents can be changed after creation. They support various operations such as adding, removing, and checking for membership of elements.
# Sets are commonly used to store unique items and perform mathematical set operations like union, intersection, and difference.            
# Examples of Set operations:
   
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)                   # Output: Original Set: {1, 2, 3, 4, 5}                

# Adding an element to the set
my_set.add(6)               
print("Set after add:", my_set)                  # Output: Set after add: {1, 2, 3, 4, 5, 6}
# Removing an element from the set
my_set.remove(3)
print("Set after remove:", my_set)               # Output: Set after remove: {1, 2, 4, 5, 6}                
# Checking for membership
print("Is 4 in set?", 4 in my_set)               # Output: Is 4 in set? True
print("Is 3 in set?", 3 in my_set)               # Output: Is 3 in set? False                
# Set Union - Combining two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_union = set_a.union(set_b)
print("Set Union:", set_union)                    # Output: Set Union: {1, 2, 3, 4, 5}                
# Set Intersection - Finding common elements
set_intersection = set_a.intersection(set_b)
print("Set Intersection:", set_intersection)      # Output: Set Intersection: {3}                
# Set Difference - Finding elements in set_a not in set_b
set_difference = set_a.difference(set_b)
print("Set Difference (A - B):", set_difference)  # Output: Set Difference (A - B): {1, 2}                
# Iterating over the set
print("Iterating over the set:")
for item in my_set:
    print(item)     
# Output:
# Iterating over the set:
# 1
# 2
# 4             
# 5
# 6
# Set Operations / Methods Reference:
# add() - Adds an element to the set
# remove() - Removes a specified element from the set
# discard() - Removes a specified element from the set if it exists (does not raise an error if the element is not found)
# pop() - Removes and returns an arbitrary element from the set
# clear() - Removes all elements from the set       
# union() - Returns a new set containing all elements from both sets
# intersection() - Returns a new set containing only the elements common to both sets
# difference() - Returns a new set containing elements in the first set but not in the second
# issubset() - Checks if the set is a subset of another set
# issuperset() - Checks if the set is a superset of another set 
# Set methods examples:
set_x = {1, 2, 3}
set_y = {3, 4, 5}               
print("Is set_x a subset of set_y?", set_x.issubset(set_y))   # Output: Is set_x a subset of set_y? False
print("Is set_y a superset of set_x?", set_y.issuperset(set_x)) # Output: Is set_y a superset of set_x? False
# End of Set operations 

# Which of the following is an invalid way to create a set?
# A) my_set = {1, 2, 3}
# B) my_set = set([1, 2, 3])
# C) my_set = {}
# D) my_set = set()
# Answer: C) my_set = {}  (This creates an empty dictionary, not a set)



#Which operation removes all elements from a set?
# The operation that removes all elements from a set is the `clear()` method.

#What is the result of {1, 2, 3} | {3, 4, 5}?
# The result of {1, 2, 3} | {3, 4, 5} is {1, 2, 3, 4, 5}, which is the union of the two sets.

