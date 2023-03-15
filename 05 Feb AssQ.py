#!/usr/bin/env python
# coding: utf-8

# Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# 
# In object-oriented programming (OOP), a class is a blueprint or template for creating objects, 
# which define the properties and behaviors of those objects. An object, on the other hand, is 
# an instance of a class that has its own unique set of values for the properties defined by the class.

# In[18]:


class Car:
    def __init__(self, make, model, year, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def start(self):
        # implementation of the start method
        pass

    def stop(self):
        # implementation of the stop method
        pass

    def accelerate(self):
        # implementation of the accelerate method
        pass

    def brake(self):
        # implementation of the brake method
        pass


my_car = Car("Toyota", "Camry", 2022, "blue", 25000)

print(my_car.make)    
print(my_car.price)   
my_car.start()     


# Name the four pillars of OOPs.
# 
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# Explain why the __init__() function is used. Give a suitable example.
# 
# In object-oriented programming (OOP), the __init__() function is a special method that is 
# called when an object is created from a class. It is used to initialize the properties or 
# attributes of the object to their initial values. The __init__() function is sometimes referred to 
# as a constructor because it constructs or creates an object.
# 
# The __init__() function takes at least one argument, which is typically named self, to refer to 
# the object being created. It can also take additional arguments to initialize the properties of 
# the object.

# In[19]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.describe()  
person2.describe()


# Why self is used in OOPs?
# 
# In object-oriented programming (OOP), self is a special keyword that refers to the instance of a 
# class that is being worked with. It is used as the first parameter to instance methods and is 
# typically named self (although it can be named anything in Python).
# 
# self is used in OOP for two main reasons:
# 
# To refer to the properties and methods of the current instance: When an instance method is called, 
#     the self parameter is used to refer to the current instance of the class, and its properties 
#     and methods can be accessed using the self keyword
#     
# To differentiate between instance and class variables: In Python, class variables are shared by 
#     all instances of a class, whereas instance variables are unique to each instance. When defining 
#     instance methods, the self parameter is used to refer to instance variables, 
#     while class variables are referred to directly by their name

# What is inheritance? Give an example for each type of inheritance.
# 
# In object-oriented programming (OOP), inheritance is a mechanism that allows a new class, 
# called a subclass or derived class, to be based on an existing class, called a superclass or 
# base class. The subclass inherits properties and behaviors from the superclass, and can add or 
# modify them as needed.
# 
# There are four types of inheritance:
# 
# 1- Single inheritance: In single inheritance, a subclass inherits properties and methods from a 
# single superclass.

# In[20]:


class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

dog = Dog()
dog.eat()  
dog.bark()


# In[23]:


##2.Multiple inheritance: In multiple inheritance, a subclass inherits properties and methods from multiple superclasses.

class A:
    def methodA(self):
        print("Method A")

class B:
    def methodB(self):
        print("Method B")

class C(A, B):
    def methodC(self):
        print("Method C")

c = C()
c.methodA()  
c.methodB()   
c.methodC() 


# In[24]:


## 3 Multilevel inheritance: In multilevel inheritance, a subclass inherits properties and 
##methods from a superclass, which in turn inherits properties and methods from its own superclass.

class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

class Labrador(Dog):
    def run(self):
        print("Labrador is running.")

lab = Labrador()
lab.eat()   
lab.bark()  
lab.run()  


# In[26]:


## 4. Hierarchical inheritance: In hierarchical inheritance, multiple subclasses inherit properties 
##and methods from a single superclass.

class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing.")

dog = Dog()
dog.eat()   
dog.bark() 

cat = Cat()
cat.eat()   
cat.meow() 


# In[ ]:




