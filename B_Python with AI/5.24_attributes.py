# Attributes in Python
# Attributes are properties or characteristics associated with objects in Python. They can store data or provide functionality related to the object.
# Attributes are defined within classes and can be accessed using the dot notation (object.attribute).
# There are two main types of attributes in Python:
# 1. Instance Attributes - These attributes are specific to an instance of a class and are defined within the __init__ method.
# 2. Class Attributes - These attributes are shared among all instances of a class and are defined directly within the class body.  

# Examples of Attributes in Python:
class Car:
    # Class Attribute
    wheels = 4
    
    def __init__(self, make, model):
        # Instance Attributes
        self.make = make
        self.model = model  

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing instance attributes
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Camry

# Accessing class attribute
print(my_car.wheels)  # Output: 4   

# Accessing class attribute using class name
print(Car.wheels)     # Output: 4

# Attribute Reference:
# 1. Instance Attributes - Defined within the __init__ method and specific to each instance of a class.
# 2. Class Attributes - Defined directly within the class body and shared among all instances of the class.

# Attribute Examples:
class Person:
    # Class Attribute
    species = "Homo sapiens"    

    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age 













