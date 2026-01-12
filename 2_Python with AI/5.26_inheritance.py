# Inheritance in Python
# Inheritance is a fundamental concept in object-oriented programming that allows a class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.
# In Python, inheritance is implemented by defining a new class that specifies the parent class in parentheses.
# There are different types of inheritance in Python:
# 1. Single Inheritance - A subclass inherits from a single parent class.
# 2. Multiple Inheritance - A subclass inherits from multiple parent classes.
# 3. Multilevel Inheritance - A subclass inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance - Multiple subclasses inherit from a single parent class.
# 5. Hybrid Inheritance - A combination of two or more types of inheritance.    

# Examples of Inheritance in Python:

# Single Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"  
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog()

# Accessing inherited method from Animal class
print(my_dog.speak())  # Output: Animal speaks

# Accessing method from Dog class
print(my_dog.bark())   # Output: Woof!  

# Multiple Inheritance
class Canine:
    def howl(self):
        return "Awooo!"  
class Wolf(Animal, Canine):
    def growl(self):
        return "Grrrr!"

# Creating an instance of the Wolf class
my_wolf = Wolf()

# Accessing inherited methods from Animal and Canine classes
print(my_wolf.speak())  # Output: Animal speaks
print(my_wolf.howl())   # Output: Awooo!

# Accessing method from Wolf class
print(my_wolf.growl())  # Output: Grrrr!

# Multilevel Inheritance
class Puppy(Dog):
    def weep(self):
        return "Whimper!"

# Creating an instance of the Puppy class
my_puppy = Puppy()

# Accessing inherited methods from Dog and Animal classes
print(my_puppy.speak())  # Output: Animal speaks
print(my_puppy.bark())   # Output: Woof!

# Accessing method from Puppy class
print(my_puppy.weep())   # Output: Whimper!

# Inheritance Reference:
# 1. Inheritance allows a class to inherit attributes and methods from another class, promoting code reusability.
# 2. The subclass can override methods from the parent class to provide specific implementations.
# 3. The super() function can be used to call methods from the parent class.

# Inheritance Examples:
class Vehicle:
    def start(self):
        return "Vehicle started"  
class Car(Vehicle):
    def drive(self):
        return "Car is driving"  

# Creating an instance of the Car class
my_car = Car()

# Accessing inherited method from Vehicle class
print(my_car.start())  # Output: Vehicle started

# Accessing method from Car class
print(my_car.drive())  # Output: Car is driving  

# End of Inheritance in Python  
# Inheritance Types Reference:
# 1. Single Inheritance - A subclass inherits from a single parent class.
# 2. Multiple Inheritance - A subclass inherits from multiple parent classes.
# 3. Multilevel Inheritance - A subclass inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance - Multiple subclasses inherit from a single parent class.
# 5. Hybrid Inheritance - A combination of two or more types of inheritance.  

# Inheritance Examples:
class Bird:
    def fly(self):
        return "Bird is flying"  
class Sparrow(Bird):
    def chirp(self):
        return "Chirp chirp!"  
class Eagle(Bird):
    def soar(self):
        return "Eagle is soaring!"  

# Creating instances of Sparrow and Eagle classes
my_sparrow = Sparrow()
my_eagle = Eagle()

# Accessing inherited method from Bird class
print(my_sparrow.fly())  # Output: Bird is flying
print(my_eagle.fly())    # Output: Bird is flying

# Accessing methods from Sparrow and Eagle classes
print(my_sparrow.chirp())  # Output: Chirp chirp!
print(my_eagle.soar())     # Output: Eagle is soaring!  

# End of Inheritance Examples

# End of Inheritance in Python


