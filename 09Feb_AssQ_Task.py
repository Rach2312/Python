#!/usr/bin/env python
# coding: utf-8

# Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.
# 

# In[1]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


# In[2]:


my_car = Vehicle(name_of_vehicle="Toyota", max_speed=120.0, average_of_vehicle=6.5)


# In[3]:


print(my_car.name_of_vehicle)
print(my_car.max_speed) 
print(my_car.average_of_vehicle)


# Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

# In[4]:


class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)
    
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} people."


# In[5]:


my_car = Car(name_of_vehicle="Toyota", max_speed=120.0, average_of_vehicle=6.5)
print(my_car.seating_capacity(5))


# What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# Multiple inheritance is a feature in object-oriented programming where a class can inherit from multiple parent classes. 
# In other words, a subclass can inherit attributes and methods from more than one parent class. 
# This allows for greater code reuse and can help simplify complex class hierarchies.

# In[7]:


class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car(Vehicle, Engine):
    def __init__(self, name, color, model):
        Vehicle.__init__(self, name, color)
        self.model = model

    def get_info(self):
        print(f"{self.name} ({self.model}) in {self.color} color.")

my_car = Car("Toyota", "Blue", "Corolla")
my_car.start()
my_car.get_info()


# What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.

# Getter and setter are methods used to access and modify the value of an object's attributes in object-oriented programming. 
# In Python, we can define getter and setter methods using the @property and @<attribute_name>.setter decorators respectively

# In[8]:


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

person = Person("John")
print(person.name)
person.name = "Mike"
print(person.name)


# What is method overriding in python? Write a python code to demonstrate method overriding.

# Method overriding is a feature in object-oriented programming where a subclass can provide its own implementation of a 
# method that is already defined in its parent class. When the method is called on an instance of the subclass, 
# the subclass's implementation is used instead of the parent class's implementation.

# In[9]:


class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

my_animal = Animal()
my_cat = Cat()
my_dog = Dog()

my_animal.speak()
my_cat.speak() 
my_dog.speak()


# In[ ]:




