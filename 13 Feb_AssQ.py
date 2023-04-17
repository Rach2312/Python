#!/usr/bin/env python
# coding: utf-8

# Explain why we have to use the Exception class while creating a Custom Exception.
# Note: Here Exception class refers to the base class for all the exceptions.

# When creating a custom exception in Python, it is generally recommended to derive it from the Exception class, which is the 
# base class for all the built-in exceptions in Python. This is because the Exception class provides a set of common methods and 
# properties that can be useful in handling exceptions.
# 
# For example, the Exception class defines the str method, which returns a string representation of the exception object. 
# This method is used when the exception is printed or logged, and it can be overridden in the custom exception to provide a 
# more meaningful error message.
# 
# Similarly, the Exception class also defines the repr method, which returns a string representation of the exception object 
# that can be used for debugging purposes. By deriving the custom exception from the Exception class, we inherit these methods 
# and properties, which can save us the trouble of having to define them ourselves.
# 
# In addition, deriving the custom exception from the Exception class also makes it easier to catch and handle the exception. 
# Since all exceptions are ultimately derived from the Exception class, we can catch our custom exception using a generic except 
# block that catches all exceptions,

# Write a python program to print Python Exception Hierarchy.

# In[1]:



base = Exception


while base is not object:
    print(base.__name__)
    base = base.__base__


print(object.__name__)


# What errors are defined in the ArithmeticError class? Explain any two with an example.

# The ArithmeticError class is a built-in exception class in Python that is used to handle errors that occur during arithmetic 
# operations. It is a subclass of the Exception class and a superclass of several more specific arithmetic exception classes.
# 
# The ArithmeticError class defines several error types that can occur during arithmetic operations. Here are two examples:
# 
# ZeroDivisionError: This error occurs when a number is divided by zero
# OverflowError: This error occurs when the result of an arithmetic operation is too large to be represented

# In[ ]:


x = 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero


# In[ ]:


x = 2 ** 1000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Numerical result out of range')


# Why LookupError class is used? Explain with an example KeyError and IndexError.

# In[ ]:


The LookupError class is a built-in exception class in Python that is used to handle errors that occur when looking up a 
value in a sequence or mapping. It is a superclass of several more specific lookup exception classes.

The LookupError class is used to catch any error that occurs during a lookup operation, such as trying to access an element 
of a list or dictionary that does not exist. It is also used when accessing a sequence with an index that is out of bounds.


# In[ ]:


d = {'a': 1, 'b': 2}
print(d['c'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'


# In[ ]:


l = [1, 2, 3]
print(l[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range


# Explain ImportError. What is ModuleNotFoundError?

# ImportError is a built-in exception class in Python that is raised when an import statement fails to find and load a module. 
# This error can occur when the module name is misspelled, the module does not exist, or there is a problem with the module's 
# code.
# 
# new exception called ModuleNotFoundError was added as a subclass of ImportError. This exception is raised specifically 
# when a module cannot be found.

# List down some best practices for exception handling in python.

# 1 Catch only the exceptions you expect: It's generally best to only catch exceptions that you know how to handle. Catching a 
#     broad exception such as Exception can make it difficult to debug errors and can result in unexpected behavior.
# 
# 2 Use the finally block for cleanup: If you need to perform cleanup tasks such as closing files or releasing resources, 
#     use the finally block to ensure that the cleanup code is always executed, regardless of whether an exception was raised.
# 
# 3 Use descriptive error messages: When raising an exception, use descriptive error messages that provide useful information 
#     about the error. This can make it easier to debug problems and can help users understand what went wrong.
# 
# 4 Don't suppress exceptions: Suppressing exceptions (i.e., catching them and doing nothing) is generally a bad idea. If you 
# catch an exception, you should do something with it, whether that means logging an error message or raising a different 
# exception.
# 
# 5 Use built-in exception classes when possible: If a built-in exception class such as ValueError or TypeError is appropriate 
#     for the error you want to raise, use it. This can make your code more readable and can ensure that other developers are 
#     familiar with the exceptions you're raising.

# In[ ]:




