# Methods in Python 
# Methods are functions that are associated with objects and can be called on those objects. In Python, methods are defined within classes and can operate on the data contained in the object (instance) of that class.
# There are two main types of methods in Python:
# 1. Instance Methods - These methods operate on an instance of a class and can access and modify the instance's attributes.
# 2. Class Methods - These methods operate on the class itself rather than on instances of the class. They are defined using the @classmethod decorator and take the class as the first parameter (usually named cls).
# 3. Static Methods - These methods do not operate on an instance or class. They are defined using the @staticmethod decorator and do not take any special first parameter.     

# Examples of Methods in Python:
class Dog:
    # Instance Method
    def bark(self):
        return "Woof!"
    
    # Class Method
    @classmethod
    def species(cls):
        return "Canis familiaris"
    
    # Static Method
    @staticmethod
    def info():
        return "Dogs are domesticated mammals." 

# Creating an instance of the Dog class
my_dog = Dog()

# Calling instance method
print(my_dog.bark())  # Output: Woof!

# Calling class method
print(Dog.species())  # Output: Canis familiaris

# Calling static method
print(Dog.info())     # Output: Dogs are domesticated mammals.
# Method Reference:
# 1. Instance Methods - Defined within a class and operate on instances of that class. They take self as the first parameter.
# 2. Class Methods - Defined with the @classmethod decorator and operate on the class itself. They take cls as the first parameter.
# 3. Static Methods - Defined with the @staticmethod decorator and do not operate on an instance or class. They do not take any special first parameter.    
# Method Examples:
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # Instance Method
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
    # Class Method
    @classmethod
    def unit_circle(cls):
        return cls(1)
    
    # Static Method
    @staticmethod
    def pi_value():
        return 3.14159

# Creating an instance of the Circle class
my_circle = Circle(5)

# Calling instance method
print(my_circle.area())  # Output: Area of the circle with radius 5

# Calling class method
unit_circle = Circle.unit_circle()
print(unit_circle.radius)  # Output: 1

# Calling static method
print(Circle.pi_value())   # Output: 3.14159    

#   Method Types Reference:
# 1. Instance Methods - Operate on instances of a class and can access and modify instance attributes.
# 2. Class Methods - Operate on the class itself and can access class attributes.
# 3. Static Methods - Do not operate on an instance or class and do not take any special first parameter.        
# Method Types Examples:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Instance Method
    def area(self):
        return self.width * self.height
    
    # Class Method
    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)
    
    # Static Method
    @staticmethod
    def description():
        return "A rectangle is a quadrilateral with four right angles."
# Creating an instance of the Rectangle class
my_rectangle = Rectangle(4, 5)

# Calling instance method
print(my_rectangle.area())  # Output: Area of the rectangle with width 4 and height 5

# Calling class method
square = Rectangle.square(4)
print(square.width, square.height)  # Output: 4 4

# Calling static method
print(Rectangle.description())  # Output: A rectangle is a quadrilateral with four right angles.    
# End of Method Types Examples        
#   Method Examples Reference:
# 1. Instance Method Example - A method that operates on an instance of a class.
# 2. Class Method Example - A method that operates on the class itself.
# 3. Static Method Example - A method that does not operate on an instance or class.        
# Method Examples:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance Method
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
    # Class Method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)
    
    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18
# Creating an instance of the Person class
person1 = Person("Alice", 30)   
print(person1.introduce())  # Output: My name is Alice and I am 30 years old.   
person2 = Person.from_birth_year("Bob", 1995)
print(person2.introduce())  # Output: My name is Bob and I am (current_year - 1995) years old.   
print(Person.is_adult(20))  # Output: True    
# End of Method Examples in Python  


# Which method is used to combine two lists without modifying them?
# The method used to combine two lists without modifying them is the `+` operator or the `extend()` method on a new list.   



