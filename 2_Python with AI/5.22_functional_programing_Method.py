# Functional Programming Methods in Python
# Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.
# Python supports several functional programming methods, including:
# 1. map() - Applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
# 2. filter() - Constructs an iterator from elements of an iterable for which a function returns true.
# 3. reduce() - Applies a rolling computation to sequential pairs of values in an iterable
# 4. zip() - Combines multiple iterables (like lists or tuples) into a single iterable of tuples.
# 5. enumerate() - Adds a counter to an iterable and returns it as an enumerate object.

# Examples of Functional Programming Methods:
from functools import reduce

# 1. map() Example
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers using map():", squared)   # Output: Squared Numbers using map(): [1, 4, 9, 16, 25]

# 2. filter() Example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using filter():", even_numbers) # Output: Even Numbers using filter(): [2, 4]

# 3. reduce() Example
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers using reduce():", product) # Output: Product of Numbers using reduce(): 120

# 4. zip() Example
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = list(zip(list1, list2))
print("Zipped Lists using zip():", zipped)       # Output: Zipped Lists using zip(): [('a', 1), ('b', 2), ('c', 3)] 

# 5. enumerate() Example
fruits = ['apple', 'banana', 'cherry']
enumerated = list(enumerate(fruits))
print("Enumerated Fruits using enumerate():", enumerated) # Output: Enumerated Fruits using enumerate(): [(0, 'apple'), (1, 'banana'), (2, 'cherry)] 

# End of Functional Programming Methods in Python
# Functional Programming Methods Reference:
# 1. map() - Transforms each item in an iterable using a specified function.
# 2. filter() - Filters items in an iterable based on a specified condition.
# 3. reduce() - Reduces an iterable to a single value by applying a binary function cumulatively.
# 4. zip() - Combines multiple iterables into a single iterable of tuples.
# 5. enumerate() - Adds a counter to an iterable and returns it as an enumerate object.
# Functional Programming Methods Examples:
# 1. map() Example
original_list = [10, 20, 30, 40]
doubled = list(map(lambda x: x * 2, original_list))
print("Doubled List using map():", doubled)     # Output: Doubled List using map(): [20, 40, 60, 80]
# 2. filter() Example
greater_than_25 = list(filter(lambda x: x > 25, original_list))
print("Numbers Greater than 25 using filter():", greater_than_25) # Output: Numbers Greater than 25 using filter(): [30, 40]
# 3. reduce() Example
sum_of_list = reduce(lambda x, y: x + y, original_list)
print("Sum of List using reduce():", sum_of_list) # Output: Sum of List using reduce(): 100
# 4. zip() Example
listA = [1, 2, 3]
listB = ['one', 'two', 'three']
zipped_lists = list(zip(listA, listB))
print("Zipped Lists using zip():", zipped_lists) # Output: Zipped Lists using zip(): [(1, 'one'), (2, 'two'), (3, 'three')] 
# 5. enumerate() Example
colors = ['red', 'green', 'blue']
enumerated_colors = list(enumerate(colors, start=1))
print("Enumerated Colors using enumerate():", enumerated_colors) # Output: Enumerated Colors using enumerate(): [(1, 'red'), (2, 'green'), (3, 'blue)] 
# End of Functional Programming Methods Examples in Python
# Functional Programming Methods Types Reference:
# 1. map() - Used for transforming data in an iterable.
# 2. filter() - Used for filtering data in an iterable based on a condition.
# 3. reduce() - Used for aggregating data in an iterable to a single value.
# 4. zip() - Used for combining multiple iterables into one.
# 5. enumerate() - Used for adding a counter to an iterable.
# Functional Programming Methods Types Examples:
# 1. map() Example
names = ['alice', 'bob', 'charlie']
capitalized_names = list(map(lambda name: name.capitalize(), names))
print("Capitalized Names using map():", capitalized_names) # Output: Capitalized Names using map(): ['Alice', 'Bob', 'Charlie']
# 2. filter() Example
long_names = list(filter(lambda name: len(name) > 3, names))
print("Names Longer than 3 Characters using filter():", long_names) # Output: Names Longer than 3 Characters using filter(): ['alice', 'charlie']
# 3. reduce() Example
from functools import reduce
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum Number using reduce():", max_number) # Output: Maximum Number using reduce(): 5
# 4. zip() Example
numbers_list = [1, 2, 3]
letters_list = ['A', 'B', 'C']
zipped_result = list(zip(numbers_list, letters_list))
print("Zipped Result using zip():", zipped_result) # Output: Zipped Result using zip(): [(1, 'A'), (2, 'B'), (3, 'C')]
# 5. enumerate() Example
animals = ['cat', 'dog', 'rabbit']
enumerated_animals = list(enumerate(animals, start=1))
print("Enumerated Animals using enumerate():", enumerated_animals) # Output: Enumerated Animals using enumerate(): [(1, 'cat'), (2, 'dog'), (3, 'rabbit)] 
# End of Functional Programming Methods Types Examples in Python    
# Infinite Generator Example
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1    
print("\nInfinite Counter Generator (first 5 values):")
counter = infinite_counter()
for _ in range(5):
    print(next(counter))                        # Output: 0 1 2 3 4     
# End of Functional Programming Methods in Python


#Which of the following is a key feature of functional programming in Python?
# Select the correct answer


# A. Mutable data structures

# B. Side effects in functions

# C. First-class functions and immutability

# D. Sequential execution only

# Answer: C. First-class functions and immutability



