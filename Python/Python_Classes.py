"""
OOP stands for --> Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
"""

# A simple example

class MyClass: # MyClass is the name of our class
    x = 5 # x is value
    
person1 = MyClass() # p1 is an object
print(person1.x) # print x's value from object p1

# A class is almost useless without its objects.



"""Delete Object"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greeting(self):
        print(f"Hello. My name is {self.name}")

person1 = Person("Milad", 22)

del person1

print(person1)



"""Multiple Objects"""
class MyClass:
    x = 3

object1 = MyClass()
object2 = MyClass()
object3 = MyClass()

print(object1.x)
print(object2.x)
print(object3.x)

"""Note: Each object is independent and has its own copy of the class properties."""




"""The __init__ Method"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person1 = Person("Milad", 22)

print(person1.name)
print(person1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.


# You can also set default values for parameters in the __init__() method:
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
        
person1 = Person("Faraz") # output: Faraz 18
person2 = Person("Milad", 22) # output: Milad 22

print(person1.name, person1.age)
print(person2.name, person2.age)

#### The __init__ method can have as many parameters as you need ###



"""
The self parameter is used to access properties and methods that belong to the class.
"""

### Note: The self parameter must be the first parameter of any method in the class. ###

### Without /self/, python would not know which object's properties you want to access ###


"""
self Does Not Have to Be Named "self"

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.
"""

### You can also call other methods within the class using /self/. ###
class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f"Hello {self.name}."
    
    def welcome(self):
        message = self.greet()
        print(f"{message}! Welcome to our website.")
        
person1 = Person("Milad")
person1.welcome()




"""Class Properties"""
"""
Properties are variables that belong to a class.
"""

### You can modify the value of properties on objects: ###
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person1 = Person("Milad", 22)
print(person1.age)

person1.age = 23
print(person1.age)


### You can add new properties to existing objects: ###
class Person:
    def __init__(self, name):
        self.name = name
        
person1 = Person("Milad")

person1.age = 22
person1.country = "Iran"

print(person1.name)
print(person1.age)
print(person1.city)
# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.

"""
Class Methods

Methods are functions that belong to a class.
"""
### Note: All methods must have self as the first parameter. ###



"""Python Inheritance"""
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""


"""
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
"""
class Student(Person):
    pass
# Now the Student class has the same properties and methods as the Person class.
# A simple Example:
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def print_name(self):
        print(self.first_name, self.last_name)
     
        
class Student(Person):
    pass

x = Student("Milad", "Salimi")
x.print_name


# When you add the /__init__()/ function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's /__init__()/ function, add a call to the parent's /__init__()/ function:
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_name(self):
        print(self.first_name, self.last_name)
        
        
class Student(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        

x = Student("Milad", "Salimi")
x.print_name


# Python also has a /super()/ function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Milad", "Salimi")
x.printname()

# By using the /super()/ function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.



# Add Properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduation_year = 2026

x = Student("Milad", "Salimi")
print(x.graduation_year)

# In another way (better way):
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduation_year = year

x = Student("Milad", "Salimi", 2026)
print(x.graduation_year)


# Add Methods
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def print_name(self):
        print(self.first_name, self.last_name)
        

class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year
        
    def welcome(self):
        print(f"Welcome {self.first_name} {self.last_name} to the class of {self.graduation_year}.")

x = Student("Milad", "Salimi", 2026)
x.welcome()

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent 
# method will be overridden (will be canceled).


"""Python Polymorphism"""
"""
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
"""

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

"""
Inheritance Class Polymorphism
"""
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()



"""Python Encapsulation"""
"""
Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works.
"""

# In Python, you can make properties private by using a double underscore __ prefix:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

person1 = Person("Milad", 22)
print(person1.name)
print(person1.__age) # This will cause (raise) an error

# Note: Private properties cannot be accessed directly from outside the class.


# To access a private property, you can create a getter method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

person1 = Person("Milad", 22)
print(person1.get_age())


### Set Private Property Value ###
# To modify a private property, you can create a setter method.
# The setter method can also validate the value before setting it:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

person1 = Person("Milad", 22)
print(person1.get_age())

person1.set_age(19)
print(person1.get_age())


# A complete example of Encapsulation:
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Milad")
student.set_grade(90)
print(student.get_grade())
print(student.get_status())


# Python also has a convention for protected properties using a single underscore _ prefix:
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary  # Protected property

person1 = Person("Milad", 50000)
print(person1.name)
print(person1._salary)  # Can access, but shouldn't

### Note: A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction. ###


# Private Methods #
# You can also make methods private using the double underscore prefix.
# Note: Just like private properties with double underscores, private methods cannot be called directly from outside the class. The __validate method can only be used by other methods inside the class.


# Name Mangling #
"""
Name mangling is how Python implements private properties and methods.

When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

For example, __age becomes _Person__age.
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age)  # Not recommended!

# Note: While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.



"""Python Inner Classes"""
"""
An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
"""
# Create an inner class
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)


# To access the inner class, create an object of the outer class, and then create an object of the inner class:
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()


# Accessing Outer Class from Inner Class #
"""
Inner classes in Python do not automatically have access to the outer class instance.

If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:
"""
class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

# Inner classes are useful for creating helper classes that are only used within the context of the outer class.
# Practical Example:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()


# A class can have multiple inner classes:
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()