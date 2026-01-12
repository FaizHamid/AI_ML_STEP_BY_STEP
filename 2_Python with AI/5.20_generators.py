# Generators in Python
# Generators are a special type of iterable in Python that allow you to iterate over a sequence of values without storing them all in memory at once.
# They are defined using functions and the yield keyword.
# When a generator function is called, it returns a generator object without executing the function body.
# The function body is executed only when the next() function is called on the generator object, which runs the function until it hits a yield statement.
# Each time yield is encountered, the function's state is saved, and the yielded value is returned to the caller.
# Generators are memory-efficient and are useful for working with large datasets or infinite sequences.     

# Examples of Generators in Python:

# 1. Simple Generator Function
def simple_generator():
    yield 1
    yield 2
    yield 3     
gen = simple_generator()
print("Simple Generator:")
print(next(gen))                                # Output: 1
print(next(gen))                                # Output: 2
print(next(gen))                                # Output: 3 

# 2. Generator for Fibonacci Sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print("\nFibonacci Generator:")
for num in fibonacci_generator(5):
    print(num)                                  # Output: 0 1 1 2 3

# 3. Generator Expression
squares = (x ** 2 for x in range(5))
print("\nGenerator Expression for Squares:")
for square in squares:
    print(square)                               # Output: 0 1 4 9 16

# 4. Infinite Generator
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1
print("\nInfinite Counter Generator (first 5 values):")
counter = infinite_counter()
for _ in range(5):
    print(next(counter))                        # Output: 0 1 2 3 4

# Generator Reference:
# 1. Generators are defined using functions and the yield keyword.
# 2. Generators return a generator object when called, without executing the function body.
# 3. The function body is executed when next() is called on the generator object.
# 4. Each yield statement produces a value and saves the function's state for the next call.
# 5. Generators are memory-efficient and suitable for large datasets or infinite sequences.

# Generator Examples:
# 1. Simple Generator Example
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
print("\nCount Up To Generator:")
for number in count_up_to(3):
    print(number)                               # Output: 1 2 3
# 2. Generator Expression Example
evens = (x for x in range(10) if x % 2 == 0)
print("\nEven Numbers Generator Expression:")
for even in evens:
    print(even)                                # Output: 0 2 4 6 8
# 3. Generator for Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_generator(n):
    num = 2
    count = 0
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1
print("\nPrime Numbers Generator:")
for prime in prime_generator(5):
    print(prime)                                # Output: 2 3 5 7 11        
# 4. Generator for Reading Large Files
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
# Note: The above function is a placeholder and requires a valid file path to work.
# End of Generator Examples 

# Note: The above examples demonstrate various uses of generators in Python, showcasing their memory efficiency and ability to handle large or infinite data sequences. 
# Generators are a powerful feature in Python that can help optimize performance and resource usage in many scenarios.  
# Generator Types Reference:
# 1. Simple Generators - Basic generator functions that yield a sequence of values.
# 2. Generator Expressions - Compact generator syntax similar to list comprehensions but using parentheses ().
# 3. Infinite Generators - Generators that can produce an infinite sequence of values.
# 4. Coroutine Generators - Generators that can consume values sent to them using the send() method.
# Generator Types Examples:
# 1. Simple Generator Example
def simple_gen():
    for i in range(4):
        yield i
print("\nSimple Generator Type Example:")
for value in simple_gen():
    print(value)                                # Output: 0 1 2 3
# 2. Generator Expression Example
cubes = (x ** 3 for x in range(4))
print("\nGenerator Expression Type Example:")
for cube in cubes:
    print(cube)                                 # Output: 0 1 8 27
# 3. Infinite Generator Example
def infinite_ones():
    while True:
        yield 1
print("\nInfinite Generator Type Example (first 3 values):")
ones_gen = infinite_ones()
for _ in range(3):
    print(next(ones_gen))                       # Output: 1 1 1
# 4. Coroutine Generator Example
def coroutine_gen():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value
print("\nCoroutine Generator Type Example:")
co_gen = coroutine_gen()
next(co_gen)                                   # Prime the generator
print(co_gen.send(5))                          # Output: 5
print(co_gen.send(10))                         # Output: 15
print(co_gen.send(3))                          # Output: 18
# End of Generator Types Examples        
# Note: The above examples demonstrate different types of generators in Python, showcasing their versatility and various use cases. Generators can be simple or complex, and they can be used for a wide range
# of applications, from simple iteration to advanced coroutine patterns.    
# Generators are a powerful feature in Python that can help optimize performance and resource usage in many scenarios.  
# End of Generators in Python



# What do generators return in Python?
# Generators return a generator object in Python.





