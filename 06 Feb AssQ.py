#!/usr/bin/env python
# coding: utf-8

# 1. Create a function which will take a list as an argument and return the product of all the numbers
# after creating a flat list.
# Use the below-given list as an argument for your function.
# list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
# 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
# Note: you must extract numeric keys and values of the dictionary also.

# In[7]:


def product_of_numbers(lst):
    
    flat_lst = []
    for item in lst:
        if isinstance(item, (list, tuple, set)):
            flat_lst.extend(item)
        elif isinstance(item, dict):
            flat_lst.extend([val for val in item.values() if isinstance(val, (int, float))])
        else:
            flat_lst.append(item)
    
   
    product = 1
    for num in flat_lst:
        if isinstance(num, (int, float)):
            product *= num
    
    return product

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34,"key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

result = product_of_numbers(list1)
print(result)


# 2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
# should be such that, for a the output should be z. For b, the output should be y. For c, the output should
# be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
# marks unchanged.
# Input Sentence: I want to become a Data Scientist.
# Encrypt the above input sentence using the program you just created.
# Note: Convert the given input sentence into lowercase before encrypting. The final output should be
# lowercase.

# In[10]:


def encrypt_message(message):
    encrypted = ""
    for char in message.lower():
        if char == " ":
            encrypted += "$"
        elif char.isalpha():
            encrypted += chr(ord("a") + (ord("z") - ord(char)))
        elif char.isalpha():
            encrypted += chr(ord("b") + (ord("y") - ord(char)))
        elif char.isalpha():
            encrypted += chr(ord("c") + (ord("x") - ord(char)))
        else:
            encrypted += char
    return encrypted.lower()


# In[15]:


input_sentence = "I want to become a Data Scientist."
encrypted_message = encrypt_message(input_sentence)
print(encrypted_message) 


# In[ ]:




