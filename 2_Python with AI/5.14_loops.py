# Loops in Python  
# Loops are used to execute a block of code repeatedly as long as a specified condition is true.
# The main types of loops in Python are:
# 1. for loop - Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# 2. while loop - Used to execute a block of code as long as a specified condition is true.
# 3. Nested loops - Loops inside other loops to perform more complex iterations.
# 4. Loop control statements - Used to modify the behavior of loops (break, continue, pass).    

# Examples of Loops in Python:

# 1. for loop
print("For Loop Example:")
fruits = ["apple", "banana", "cherry"]              
for fruit in fruits:
    print(fruit)                                    # Output: apple banana cherry                                           

# 2. while loop
print("\nWhile Loop Example:")                  
count = 1
while count <= 5:       
    print("Count:", count)                          # Output: Count: 1 Count: 2 Count: 3 Count: 4 Count: 5
    count += 1

# 3. Nested loops
print("\nNested Loop Example:")
for i in range(1, 4):               # Outer loop
    for j in range(1, 4):           # Inner loop
        print(f"i: {i}, j: {j}")    # Output: i: 1, j: 1 ... i: 3, j: 3

# 4. Loop control statements
print("\nLoop Control Statements Example:")

# break statement
print("Break Statement Example:")
for num in range(1, 10):
    if num == 5:
        break                                   # Exit the loop when num is 5
    print(num)                                  # Output: 1 2 3 4

# continue statement
print("\nContinue Statement Example:")
for num in range(1, 10):
    if num % 2 == 0:
        continue                                # Skip even numbers
    print(num)                                  # Output: 1 3 5 7 9

# pass statement
print("\nPass Statement Example:")
for num in range(1, 6):
    if num == 3:
        pass                                    # Do nothing when num is 3
    print(num)                                  # Output: 1 2 3 4 5                     
# End of Loops in Python

# Which loop is best when the number of iterations is known?
# The for loop is best when the number of iterations is known.

#What happens when break is encountered in a loop?
# When break is encountered in a loop, it immediately terminates the loop and exits to the next statement following the loop.

#Which loop control statement skips the current iteration?
# The continue statement skips the current iteration and moves to the next iteration of the loop.


                    