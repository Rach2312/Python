#!/usr/bin/env python
# coding: utf-8

# You are writing code for a company. The requirement of the company is that you create a python
# function that will check whether the password entered by the user is correct or not. The function should
# take the password as input and return the string “Valid Password” if the entered password follows the
# below-given password guidelines else it should return “Invalid Password”.
# 
# Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
# 2. The Password should contain at least a number and three special characters.
# 
# 3. The length of the password should be 10 characters long.

# In[34]:



def check_password(password):
    # check password length
    if len(password) != 10:
        return "Invalid Password: Password must be exactly 10 characters long"
    
    # check for uppercase letters
    uppercase_count = 0
    for char in password:
        if char.isupper():
            uppercase_count += 1
    if uppercase_count < 2:
        return "Invalid Password: Password must contain at least two uppercase letters"
    
    # check for lowercase letters
    lowercase_count = 0
    for char in password:
        if char.islower():
            lowercase_count += 1
    if lowercase_count < 2:
        return "Invalid Password: Password must contain at least two lowercase letters"
    
    # check for digits
    if not any(char.isdigit() for char in password):
        return "Invalid Password: Password must contain at least one digit"
    
    # check for special characters
    special_chars = "!@#$%^&*()_+-="
    special_count = 0
    for char in password:
        if char in special_chars:
            special_count += 1
    if special_count < 3:
        return "Invalid Password: Password must contain at least three special characters"
    
    # if all conditions are met, return "Valid Password"
    return "Valid Password"
password = input("Enter the password ")
print(check_password(password))


# Solve the below-given questions using at least one of the following:
# 1. Lambda function
# 2. Filter functioJ
# 3. Zap functioJ
# 4. List ComprehensioI
# B Check if the string starts with a particular letterY
# B Check if the string is numericY
# B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-
# B Find the squares of numbers from 1 to 10Y
# B Find the cube root of numbers from 1 to 10Y
# B Check if a given number is evenY
# B Filter odd numbers from the given list.
# [1,2,3,4,5,6,7,8,9,10-
# B Sort a list of integers into positive and negative integers lists.
# [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
#  

# In[35]:


##Check if the string starts with a particular letter:

strings = ["apple", "banana", "orange", "grape"]
letter = "a"
starts_with_letter = list(filter(lambda x: x.startswith(letter), strings))
print(starts_with_letter)

##Check if the string is numeric:


strings = ["123", "abc", "456"]
is_numeric = list(filter(lambda x: x.isnumeric(), strings))
print(is_numeric)

##Sort a list of tuples having fruit names and their quantity:

fruits = [("mango",99),("orange",80), ("grapes", 1000)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(sorted_fruits)

##Find the squares of numbers from 1 to 10:

squares = [x**2 for x in range(1, 11)]
print(squares)

## Find the cube root of numbers from 1 to 10:

import math
cube_roots = [math.pow(x, 1/3) for x in range(1, 11)]
print(cube_roots)

##Check if a given number is even:

num = 5
is_even = True if num % 2 == 0 else False
print(is_even)

##Filter odd numbers from the given list:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

##Sort a list of integers into positive and negative integers lists:

nums = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive_nums = sorted(list(filter(lambda x: x > 0, nums)))
negative_nums = sorted(list(filter(lambda x: x < 0, nums)))
print(positive_nums, negative_nums)




# In[ ]:




