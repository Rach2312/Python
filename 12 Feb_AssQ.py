#!/usr/bin/env python
# coding: utf-8

# What is an Exception in python? Write the difference between Exceptions and Syntax errors.

# An exception in Python is an error that occurs during the execution of a program, causing the program to halt. When an exception occurs, the program will stop executing and raise an error message that provides information about what went wrong.
# 
# Exceptions in Python can be caused by a variety of reasons, including division by zero, accessing an undefined variable, 
# trying to perform an operation on an incompatible data type, and more. However, Python provides a way to handle these 
# exceptions, so that the program can continue running without halting completely.
# 
# Syntax errors, on the other hand, occur before the program begins executing. They are caused by incorrect syntax in the code, 
# such as a missing parentheses, a misspelled keyword, or a missing colon. These errors prevent the program from being compiled 
# or interpreted correctly.

# What happens when an exception is not handled? Explain with an example.

# When an exception is not handled in Python, it results in an error message being displayed and the program stopping its 
# execution abruptly. This can be problematic, especially if the program is part of a larger application or system, as it can 
# lead to unintended consequences such as data corruption or data loss.

# In[10]:


def divide_numbers(a, b):
    return a/b

result = divide_numbers(10, 0)
print(result)


# In[ ]:


Traceback (most recent call last):
  File "example.py", line 4, in <module>
    result = divide_numbers(10, 0)
  File "example.py", line 2, in divide_numbers
    return a/b
ZeroDivisionError: division by zero


#  Which Python statements are used to catch and handle exceptions? Explain with an example.

# Python provides a try-except block for catching and handling exceptions. The try block is used to enclose the code that might 
# raise an exception, and the except block is used to handle the exception if it is raised. 

# In[12]:


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        result = None
    return result

result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)

print(result1) 
print(result2) 


# Explain with an example: try and else, finally, raise 

# In[14]:


def read_file(file_path):
    try:
        file = open(file_path, 'r')
        contents = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    else:
        print(f"File contents: {contents}")
    finally:
        file.close()

def write_file(file_path, text):
    try:
        file = open(file_path, 'w')
        file.write(text)
    except:
        print(f"Error: Could not write to file at path {file_path}")
        raise
    else:
        print(f"Successfully wrote text to file at path {file_path}")
    finally:
        file.close()


read_file("example.txt")  

write_file("example.txt", "Hello, world!") 

read_file("example.txt")  


# What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example

# Custom Exceptions are user-defined exceptions in Python. They allow us to define our own types of exceptions based on the 
# requirements of our program. Custom exceptions are created by subclassing the built-in Exception class or any of its subclasses,
# and can be raised in the same way as built-in exceptions.
# 
# We need Custom Exceptions for several reasons:
# 
# Better error handling: Custom exceptions can provide more specific and meaningful error messages than the built-in exceptions, 
#     making it easier to identify and handle errors in our code.
# 
# Modularity: Custom exceptions can be used to encapsulate error handling code within a module or class, making it easier to 
#     reuse and maintain.
# 
# Consistency: Custom exceptions can help maintain consistency in the way errors are handled throughout a project.
# 
# 

# In[15]:


class InvalidPasswordError(Exception):
    def __init__(self, message="Invalid password"):
        self.message = message
        super().__init__(self.message)

def check_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long")
    elif not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Password must contain at least one digit")

password1 = "1234"
password2 = "password"

try:
    check_password(password1)
except InvalidPasswordError as e:
    print(e.message)

try:
    check_password(password2)
except InvalidPasswordError as e:
    print(e.message)


# Create a custom exception class. Use this class to handle an exception.

# In[16]:


class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError()
    else:
        return number ** 0.5

try:
    result1 = calculate_square_root(16)
    print(result1)  # Output: 4.0
    result2 = calculate_square_root(-16)
    print(result2)
except NegativeNumberError as e:
    print(e.message) 


# In[ ]:




