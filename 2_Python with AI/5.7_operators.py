# Operators in Python 
# Operators are special symbols or keywords that perform operations on one or more operands (values or variables).
# Python supports various types of operators, including:
# 1. Arithmetic Operators: +, -, *, /, %, //, **
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
# 5. Bitwise Operators: &, |, ^, ~, <<, >>
# 6. Membership Operators: in, not in
# 7. Identity Operators: is, is not 

# Examples of different operators:  
# 1. Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # Output: Addition: 13
print("Subtraction:", a - b)       # Output: Subtraction: 7
print("Multiplication:", a * b)    # Output: Multiplication: 30
print("Division:", a / b)          # Output: Division: 3.3333333333333335
print("Modulus:", a % b)           # Output: Modulus: 1
print("Floor Division:", a // b)   # Output: Floor Division: 3
print("Exponentiation:", a ** b)   # Output: Exponentiation: 1000
# 2. Comparison Operators  
# Equal to
print("Equal to:", a == b)         # Output: Equal to: False
# Not equal to
print("Not equal to:", a != b)     # Output: Not equal to: True
# Greater than
print("Greater than:", a > b)      # Output: Greater than: True
# Less than
print("Less than:", a < b)         # Output: Less than: False
# Greater than or equal to
print("Greater than or equal to:", a >= b) # Output: Greater than or equal to: True
# Less than or equal to
print("Less than or equal to:", a <= b)    # Output: Less than or equal to: False
# 3. Logical Operators
x = True
y = False
print("Logical AND:", x and y)     # Output: Logical AND: False
print("Logical OR:", x or y)       # Output: Logical OR: True
print("Logical NOT:", not x)       # Output: Logical NOT: False
# 4. Assignment Operators
c = 5
c += 2
print("c after += 2:", c)          # Output: c after += 2: 7
c *= 3
print("c after *= 3:", c)          # Output: c after *= 3: 21
# 5. Bitwise Operators
p = 5      # Binary: 0101
q = 3      # Binary: 0011
print("Bitwise AND:", p & q)       # Output: Bitwise AND: 1
print("Bitwise OR:", p | q)        # Output: Bitwise OR: 7
print("Bitwise XOR:", p ^ q)       # Output: Bitwise XOR: 6
print("Bitwise NOT:", ~p)          # Output: Bitwise NOT: -6
print("Left Shift p by 1:", p << 1) # Output: Left Shift p by 1: 10
print("Right Shift p by 1:", p >> 1) # Output: Right Shift p by 1: 2
# 6. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?:", 3 in my_list)   # Output: Is 3 in my_list?: True
print("Is 6 not in my_list?:", 6 not in my_list) # Output: Is 6 not in my_list?: True
# 7. Identity Operators
m = [1, 2, 3]
n = m   
print("m is n?:", m is n)           # Output: m is n?: True
o = [1, 2, 3]
print("m is o?:", m is o)           # Output: m is o?: False
print("m is not o?:", m is not o)   # Output: m is not o?: True         
# End of Operators in Python    


# Which operation finds common elements between two sets?
# The operation that finds common elements between two sets is called "Set Intersection".
# What is the result of 7 // 3 in Python?
