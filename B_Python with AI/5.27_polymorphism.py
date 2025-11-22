# Polymorphism in Python    
# Polymorphism is a programming concept that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism is often achieved through method overriding and operator overloading.
# Polymorphism allows for flexibility and the ability to extend code without modifying existing functionality. It promotes code reusability and simplifies code maintenance.
# There are two main types of polymorphism in Python:
# 1. Compile-time Polymorphism (Static Polymorphism) - Achieved through method overloading and operator overloading.
# 2. Run-time Polymorphism (Dynamic Polymorphism) - Achieved through method overriding in inheritance.  

# Examples of Polymorphism in Python:

# Compile-time Polymorphism (Operator Overloading)
class Adder:
    def add(self, a, b):
        return a + b    

# Creating an instance of the Adder class
adder = Adder()

# Using the add method
print(adder.add(5, 3))  # Output: 8
print(adder.add("Hello, ", "world!"))  # Output: Hello, world!  

# Run-time Polymorphism (Method Overriding)
class Animal:
    def speak(self):
        return "Animal speaks"  
class Dog(Animal):
    def speak(self):
        return "Woof!"  
class Cat(Animal):
    def speak(self):
        return "Meow!"  

# Creating instances of Dog and Cat classes
dog = Dog()
cat = Cat()

# Calling the speak method on Dog and Cat instances
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow! 

# Polymorphism Reference:
# 1. Polymorphism allows methods to do different things based on the object it is acting upon.
# 2. It promotes code reusability and flexibility by allowing the same interface to be used for different data types.
# 3. In Python, polymorphism is often achieved through method overriding and operator overloading.

# Polymorphism Examples:
class Shape:
    def area(self):
        pass  
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height  
    
    def area(self):
        return self.width * self.height  
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
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area()) 

# Polymorphism Types Reference:
# 1. Compile-time Polymorphism - Achieved through method overloading and operator overloading.
# 2. Run-time Polymorphism - Achieved through method overriding in inheritance.  

# Polymorphism Types Examples:
class Printer:
    def print(self, data):
        print(data)  

# Creating an instance of the Printer class
printer = Printer() 

# Using the print method with different data types
printer.print("Hello, World!")  # Output: Hello, World!
printer.print(12345)             # Output: 12345
printer.print([1, 2, 3, 4, 5])   # Output: [1, 2, 3, 4, 5]  
# End of Polymorphism in Python 