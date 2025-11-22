# Abstraction in Python
# Abstraction is a fundamental concept in object-oriented programming that focuses on hiding the complex implementation details and exposing only the necessary and relevant parts of an object or system.
# It allows programmers to work at a higher level of understanding by simplifying interactions with complex systems.
# In Python, abstraction is typically achieved through the use of abstract classes and interfaces, which define a blueprint for other classes to follow without providing a complete implementation.
# The abc module in Python provides tools for defining abstract base classes (ABCs) and enforcing that derived classes implement specific methods.
# Abstraction helps in reducing complexity, improving code maintainability, and promoting code reusability.

# Examples of Abstraction in Python:
from abc import ABC, abstractmethod 

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height  
    
    def area(self):
        return self.width * self.height

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  
    
    def area(self):
        import math
        return math.pi * (self.radius ** 2)  

# Creating instances of Rectangle and Circle classes
rectangle = Rectangle(5, 10)
circle = Circle(7)  

# Calculating and printing the area of Rectangle and Circle
print("Area of Rectangle:", rectangle.area())  # Output: Area of Rectangle: 50
print("Area of Circle:", circle.area())        # Output: Area of Circle: 153.93804002589985

# Abstraction Reference:
# 1. Abstraction is the process of simplifying complex systems by hiding unnecessary details and exposing only the relevant parts.
# 2. Abstract classes and interfaces are used to define blueprints for other classes without providing complete implementations.
# 3. The abc module in Python provides tools for creating abstract base classes and enforcing method implementation in derived classes.

# Abstraction Examples:
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass    

# Derived Class - Car
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"  

# Derived Class - Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"  

# Creating instances of Car and Motorcycle classes
my_car = Car()
my_motorcycle = Motorcycle()  

# Starting engines of Car and Motorcycle
print(my_car.start_engine())          # Output: Car engine started
print(my_motorcycle.start_engine())   # Output: Motorcycle engine started  

# End of Abstraction in Python  
# Abstraction Types Reference:
# 1. Data Abstraction - Hiding the internal data representation and exposing only the necessary data through methods.
# 2. Control Abstraction - Hiding the control flow and exposing only the necessary operations through functions or methods.
# 3. Procedural Abstraction - Hiding the implementation details of procedures and exposing only the procedure interface.  

# Abstraction Types Examples:   
from abc import ABC, abstractmethod
# Abstract Base Class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass    
    @abstractmethod
    def turn_off(self):
        pass    

# Derived Class - WashingMachine
class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing machine is now ON"  
    
    def turn_off(self):
        return "Washing machine is now OFF"  

# Derived Class - Refrigerator
class Refrigerator(Appliance):
    def turn_on(self):
        return "Refrigerator is now ON"  
    
    def turn_off(self):
        return "Refrigerator is now OFF"  

# Creating instances of WashingMachine and Refrigerator classes
washing_machine = WashingMachine()
refrigerator = Refrigerator()  

# Turning appliances ON and OFF
print(washing_machine.turn_on())     # Output: Washing machine is now ON
print(washing_machine.turn_off())    # Output: Washing machine is now OFF
print(refrigerator.turn_on())        # Output: Refrigerator is now ON
print(refrigerator.turn_off())       # Output: Refrigerator is now OFF  
# End of Abstraction Examples   
# End of Abstraction in Python


