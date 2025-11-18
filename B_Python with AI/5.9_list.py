# List
# Lists are ordered, mutable collections of items in Python. They are defined using square brackets [] and can contain items of different data types.   
# Lists support various operations such as indexing, slicing, appending, removing, and iterating over elements.
# Lists are commonly used to store and manage collections of data.

# Examples of List operations:

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)               # Output: Original List: [1, 2, 3, 4, 5]

# List Indexing - Accessing individual elements in a list using their position (index)
example_list = ['a', 'b', 'c', 'd', 'e']
first_element = my_list[0]    # 'a'
last_element = my_list[-1]    # 'e'
# Accessing elements by index
print("First Element:", my_list[0])            # Output: First Element: 1
print("Last Element:", my_list[-1])            # Output: Last Element: 5

# List Slicing - Accessing a subset of elements in a list using a range of indices
sub_list = my_list[1:4]       # [2, 3, 4]    
print("Sliced List (2nd to 4th):", my_list[1:4]) # Output: Sliced List (2nd to 4th): [2, 3, 4]

# Appending an element to the list
my_list.append(6)
print("List after append:", my_list)           # Output: List after append: [1, 2, 3, 4, 5, 6]

# Removing an element from the list
my_list.remove(3)
print("List after remove:", my_list)           # Output: List after remove: [1, 2, 4, 5, 6]

# Iterating over the list
print("Iterating over the list:")
for item in my_list:
    print(item)

# Output:
# Iterating over the list:
# 1 
# 2
# 4
# 5
# 6             
# List Comprehension - Creating a new list by applying an expression to each item in an existing list
squared_list = [x**2 for x in my_list]
print("Squared List:", squared_list)           # Output: Squared List: [1, 4, 16, 25, 36]
  
# List metnhods reference:
# append() - Adds an element to the end of the list
# extend() - Extends the list by appending elements from another iterable
# insert() - Inserts an element at a specified position
# remove() - Removes the first occurrence of a specified element
# pop() - Removes and returns an element at a specified position (default is the last element)
# clear() - Removes all elements from the list
# index() - Returns the index of the first occurrence of a specified element
# count() - Returns the number of occurrences of a specified element
# sort() - Sorts the elements of the list in ascending order
# reverse() - Reverses the order of the elements in the list

# List methods examples:
my_list = [5, 2, 9, 1, 5, 6]
my_list.append(3)
print("After append(3):", my_list)             # Output: After append(3): [5, 2, 9, 1, 5, 6,    3]      
my_list.sort()
print("After sort():", my_list)                 # Output: After sort(): [1, 2, 3, 5, 5, 6, 9]
my_list.reverse()
print("After reverse():", my_list)             # Output: After reverse(): [9, 6, 5, 5, 3, 2, 1]
my_list.remove(5)
print("After remove(5):", my_list)             # Output: After remove(5): [9, 6, 5, 3, 2, 1]
popped_element = my_list.pop()
print("After pop():", my_list, "Popped Element:", popped_element) # Output: After pop(): [9, 6, 5, 3, 2] Popped Element: 1    

# End of List in Python
# # The list method used to add an element at the end of the list is `append()`.  
#What will be the output of lst = [1, 2, 3]; lst.pop()?
# Output: 3

# Which list comprehension creates a list of squares of even numbers from 1 to 10?
# The list comprehension is: [x**2 for x in range(1, 11) if x % 2 == 0]