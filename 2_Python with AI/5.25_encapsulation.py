# Encapsulation in Python
# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. Encapsulation helps to restrict direct access to some of an object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
# In Python, encapsulation is implemented using access specifiers:
# 1. Public Members - Attributes and methods that are accessible from outside the class. They have no special prefix.
# 2. Protected Members - Attributes and methods that are intended to be accessed only within the class and its subclasses. They are prefixed with a single underscore (_).
# 3. Private Members - Attributes and methods that are intended to be accessed only within the class itself. They are prefixed with a double underscore (__).   

# Encapsulation Examples:
class BankAccount:
    def __init__(self, account_number, balance):
        # Public Attribute
        self.account_number = account_number
        # Private Attribute
        self.__balance = balance  

    # Public Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Public Method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Public Method to access private attribute
    def get_balance(self):
        return self.__balance   
# Creating an instance of the BankAccount class
my_account = BankAccount("123456789", 1000)

# Accessing public attribute
print(my_account.account_number)  # Output: 123456789

# Accessing private attribute directly (will raise an AttributeError)
# print(my_account.__balance)  # Uncommenting this line will cause an error

# Accessing private attribute using public method
print(my_account.get_balance())  # Output: 1000

# Using public methods to modify private attribute
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance())  # Output: 1300

# Encapsulation Reference:
# 1. Public Members - Accessible from outside the class without any restrictions.
# 2. Protected Members - Indicated by a single underscore (_) and intended for use within the class and its subclasses.
# 3. Private Members - Indicated by a double underscore (__) and intended for use only within the class itself.
# Encapsulation Examples:
class Person:
    def __init__(self, name, age):
        # Public Attribute
        self.name = name
        # Private Attribute
        self.__age = age  

    # Public Method
    def get_age(self):
        return self.__age

    # Public Method
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("John", 30)
print(person.name)          # Output: John
print(person.get_age())    # Output: 30
person.set_age(35)
print(person.get_age())    # Output: 35
person.set_age(-5)        # Output: Age cannot be negative. 
# End of Encapsulation Examples
# End of Encapsulation in Python
