# Scope of Variables in Python
# Scope refers to the visibility and lifetime of variables in different parts of a program.
# There are four types of variable scopes in Python:
# 1. Local Scope - Variables defined within a function are local to that function and cannot be accessed outside of it.
# 2. Enclosing Scope - Variables in the local scope of enclosing functions (nested functions) can be accessed by inner functions.
# 3. Global Scope - Variables defined at the top level of a script or module are global and can be accessed from anywhere in that module.
# 4. Built-in Scope - Python has a set of built-in functions and variables that are always available.

# Examples of Variable Scopes:

# 1. Local Scope
def local_scope_example():
    local_var = "I am local"
    print(local_var)  # Output: I am local      
local_scope_example()
# Uncommenting the next line will raise a NameError because local_var is not accessible outside the function
# print(local_var)  # NameError: name 'local_var' is not defined    

# 2. Enclosing Scope
def outer_function():
    outer_var = "I am in the outer function"
    def inner_function():
        print(outer_var)  # Accessing variable from enclosing scope
    inner_function()
outer_function()  # Output: I am in the outer function

# 3. Global Scope
global_var = "I am global"
def global_scope_example():
    print(global_var)  # Accessing global variable
global_scope_example()  # Output: I am global
print(global_var)      # Output: I am global

# 4. Built-in Scope
def builtin_scope_example():
    print(len("Hello"))  # Using built-in len() function
builtin_scope_example()  # Output: 5
# Scope Reference:
# 1. Local Scope - Variables defined within a function, accessible only inside that function.
# 2. Enclosing Scope - Variables in the local scope of enclosing functions, accessible by inner functions.
# 3. Global Scope - Variables defined at the top level of a script or module, accessible from anywhere in that module.
# 4. Built-in Scope - Pre-defined functions and variables in Python, always accessible.
# Scope Examples:
# 1. Local Scope Example
def example_local():    
    x = 10
    print("Local x:", x)                        # Output: Local x: 10
example_local()
# 2. Enclosing Scope Example
def outer():
    y = 20
    def inner():
        print("Enclosing y:", y)                # Output: Enclosing y: 20
    inner()
outer()
# 3. Global Scope Example
z = 30
def example_global():    
    print("Global z:", z)                        # Output: Global z: 30
example_global()
# 4. Built-in Scope Example
def example_builtin():    
    print("Built-in max:", max(5, 10, 3))       # Output: Built-in max: 10
example_builtin()
# End of Scope in Python        

# Scope Types Reference:
# 1. Local Scope - Variables defined within a function, accessible only inside that function.
# 2. Enclosing Scope - Variables in the local scope of enclosing functions, accessible by inner functions.
# 3. Global Scope - Variables defined at the top level of a script or module, accessible from anywhere in that module.
# 4. Built-in Scope - Pre-defined functions and variables in Python, always accessible.             
# Scope Types Examples:
# 1. Local Scope Example
def func_local():    
    a = 5
    print("Local a:", a)                        # Output: Local a: 5
func_local()
# 2. Enclosing Scope Example
def outer_func():
    b = 15
    def inner_func():
        print("Enclosing b:", b)                # Output: Enclosing b: 15
    inner_func()        
outer_func()
# 3. Global Scope Example
c = 25
def func_global():    
    print("Global c:", c)                        # Output: Global c: 25
func_global()
# 4. Built-in Scope Example
def func_builtin():    
    print("Built-in min:", min(8, 3, 6))        # Output: Built-in min: 3       
func_builtin()
# End of Scope Types Examples        
#   Scope Methods Reference:
#   globals() - Returns a dictionary representing the current global symbol table.
#   locals() - Returns a dictionary representing the current local symbol table.            
#   nonlocal - Used to refer to variables in the nearest enclosing scope that is not global.
#   del - Used to delete variables from a specific scope.
# Example of nonlocal and del
def outer_nonlocal():
    msg = "Hello"
    def inner_nonlocal():
        nonlocal msg
        msg = "Hi"
        print("Inner message:", msg)  # Output: Inner message: Hi
    inner_nonlocal()
    print("Outer message:", msg)      # Output: Outer message: Hi
outer_nonlocal()        
def delete_variable():
    x = 50
    print("Before deletion, x:", x)  # Output: Before deletion, x: 50
    del x
    # Uncommenting the next line will raise a NameError because x has been deleted
    # print("After deletion, x:", x)  # NameError: name 'x' is not defined
delete_variable()   
# End of Scope Methods Examples 
# Scope Methods Examples:
# 1. globals() Example
def globals_example():    
    global_vars = globals()
    print("Global Variables:", global_vars)      # Output: Dictionary of global variables
globals_example()
# 2. locals() Example
def locals_example():    
    local_var = 100
    local_vars = locals()
    print("Local Variables:", local_vars)        # Output: Dictionary of local variables
locals_example()
# End of Scope Methods Examples 
# 3. nonlocal Example
def nonlocal_example():    
    outer_var = "Outer"
    def inner_func():
        nonlocal outer_var
        outer_var = "Modified Outer"
        print("Inner Function:", outer_var)      # Output: Inner Function: Modified Outer
    inner_func()
    print("Outer Function:", outer_var)          # Output: Outer Function: Modified Outer
nonlocal_example()
# 4. del Example
def del_example():  
    temp_var = "Temporary"
    print("Before deletion:", temp_var)          # Output: Before deletion: Temporary
    del temp_var
    # Uncommenting the next line will raise a NameError because temp_var has been deleted
    # print("After deletion:", temp_var)          # NameError: name 'temp_var' is not defined
del_example()   
# End of Scope Methods Examples 
# End of Scope in Python



