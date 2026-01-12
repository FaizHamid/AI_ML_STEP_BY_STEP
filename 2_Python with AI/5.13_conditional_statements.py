# Conditional Statements in Python  
# Conditional statements are used to perform different actions based on certain conditions.
# The main conditional statements in Python are:
# 1. if statement - Used to execute a block of code if a specified condition is true.
# 2. elif statement - Short for "else if", used to check multiple conditions.
# 3. else statement - Used to execute a block of code if none of the previous conditions are true. 
# 4. Nested if statements - if statements inside other if statements to check multiple levels of conditions.
# 5. Conditional Expressions (Ternary Operator) - A shorthand way of writing an if-else statement in a single line. 

# Examples of Conditional Statements:   

# if statement
age = 18
if age >= 18:
    print("You are an adult.")               # Output: You are an adult.            

inp = input("Nationality ? ")
if inp == "French":
    print("Bonjour!")                         # Output: Bonjour! (if input is French)
elif inp == "Spanish":
    print("Hola!")                            # Output: Hola! (if input is Spanish)
else:
    print("Hello!")                           # Output: Hello! (for any other input)

# if-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")                # Output: You are a minor.

# if-elif-else statement
score = 85          
if score >= 90:
    print("Grade: A")
elif score >= 80:               
    print("Grade: B")                      # Output: Grade: B
elif score >= 70:             
    print("Grade: C")                      # Output: Grade: C                   
else:
    print("Grade: F")                      # Output: Grade: F                   

# Nested if statement                           
num = 10
if num > 0:             
    if num % 2 == 0:
        print("The number is positive and even.")  # Output: The number is positive and even.              
    else:
        print("The number is positive and odd.")                
else:             
    print("The number is non-positive.")                    

# Conditional Expressions (Ternary Operator)        
is_even = "Even" if num % 2 == 0 else "Odd"             
print("The number is", is_even)               # Output: The number is Even          

# End of Conditional Statements in Python   

# Which statement executes when all if and elif conditions fail?`
# The else statement executes when all if and elif conditions fail.

# What will if not 0: evaluate to?`
# The expression `if not 0:` evaluates to True because 0 is considered falsy in Python, and the `not` operator negates it to True.

#Which of the following is not a valid condition?
# A. if x == 5:
# B. if (x > y) and (y < z):
# C. if x = 10:
# D. if not x:
# Answer: C. if x = 10:  (This is an assignment, not a comparison. The correct syntax for comparison is `if x == 10:`)

#What is the output of if "": print("Empty") else: print("Not Empty")?
# The output will be "Not Empty" because an empty string is considered falsy in Python.


#What is the result of for i in range(0, 5, 2): print(i)?
# The output will be:
# 0
# 2
# 4
# This is because the range(0, 5, 2) generates numbers starting from 0 up to (but not including) 5, with a step of 2.