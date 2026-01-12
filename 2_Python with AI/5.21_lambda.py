# Lambda Functions in Python
# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have a single expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.     

# Examples of Lambda Functions in Python:

# 1. Basic Lambda Function
add = lambda x, y: x + y
print("Add:", add(3, 5))                         # Output: Add: 8       

# 2. Lambda Function with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)                       # Output: Squared: [1, 4, 9, 16, 25]        

# 3. Lambda Function with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))      
print("Even Numbers:", even_numbers)             # Output: Even Numbers: [2, 4]        

# 4. Lambda Function with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)                       # Output: Product: 120             

# 5. Lambda Function as a key in sorting
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
points_sorted = sorted(points, key=lambda point: point[1])
print("Points Sorted by Y-coordinate:", points_sorted) # Output: Points Sorted by Y-coordinate: [(3, 1), (1, 2), (2, 3), (5, 4)]                

# Lambda Function Reference:
# 1. Lambda functions are defined using the lambda keyword followed by parameters, a colon, and an expression.
# 2. They can take any number of arguments but can only have a single expression.
# 3. The expression is evaluated and returned when the lambda function is called.
# 4. Lambda functions are often used in higher-order functions like map(), filter(), and reduce().
# 5. They are useful for short, throwaway functions that are not reused elsewhere.        

# Lambda Function Examples:
# 1. Simple Lambda Function Example             
multiply = lambda a, b: a * b
print("Multiply:", multiply(4, 6))               # Output: Multiply: 24                 
# 2. Lambda with map() Example  
numbers = [10, 20, 30, 40]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)                       # Output: Doubled: [20, 40, 60, 80]        
# 3. Lambda with filter() Example
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd Numbers:", odd_numbers)               # Output: Odd Numbers: []        
# 4. Lambda with reduce() Example
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", sum_of_numbers)         # Output: Sum of Numbers: 100        
# 5. Lambda as key in sorting Example
words = ["banana", "apple", "cherry", "date"]
words_sorted = sorted(words, key=lambda word: len(word))
print("Words Sorted by Length:", words_sorted)   # Output: Words Sorted by Length: ['date', 'apple', 'banana', 'cherry']        

# End of Lambda Functions in Python     
# Lambda Function Types Reference:
# 1. Basic Lambda Function - A simple lambda function that performs a single operation.
# 2. Lambda with map() - A lambda function used to transform items in an iterable.
# 3. Lambda with filter() - A lambda function used to filter items in an iterable.
# 4. Lambda with reduce() - A lambda function used to cumulatively apply an operation to items in an iterable.
# 5. Lambda as key in sorting - A lambda function used to specify the sorting criteria.        

# Lambda Function Types Examples:

# 1. Basic Lambda Function Example
subtract = lambda a, b: a - b
print("Subtract:", subtract(10, 4))               # Output: Subtract: 6                 
# 2. Lambda with map() Example
original_list = [2, 4, 6, 8]
halved = list(map(lambda x: x / 2, original_list))
print("Halved:", halved)                         # Output: Halved: [1.0, 2.0, 3.0, 4.0]        
# 3 Lambda with filter() Example
greater_than_five = list(filter(lambda x: x > 5, original_list))
print("Greater than Five:", greater_than_five)   # Output: Greater than Five: [6, 8]        
# 4. Lambda with reduce() Example       
sum_of_original = reduce(lambda x, y: x + y, original_list)
print("Sum of Original List:", sum_of_original)   # Output: Sum of Original List: 20        
# 5. Lambda as key in sorting Example
tuples_list = [(1, 'one'), (3, 'three'), (2, 'two')]
tuples_sorted = sorted(tuples_list, key=lambda item: item[0])
print("Tuples Sorted by First Element:", tuples_sorted) # Output: Tuples Sorted by First Element: [(1, 'one'), (2, 'two'), (3, 'three)]        
# End of Lambda Function Examples in Python 

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

# End of Lambda Functions in Python 


# What is a lambda function in Python?
# Select the correct answer
# A. A built-in module
# B. A function defined without a name
# C. A function that only accepts one argument
# D. A loop function
# Answer: B. A function defined without a name