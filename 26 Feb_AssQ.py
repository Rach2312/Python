#!/usr/bin/env python
# coding: utf-8

# 
# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
# to print the data types of both the variables.

# Yes, there is a difference in the data type of list_ and array_list.
# 
# list_ is a list object that contains string elements, while array_list is a numpy array object that contains integer 
# elements (since the original list elements are converted to integers during the creation of the array using np.array()).

# In[8]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print(type(list_))
print(type(array_list)) 


# Write a code to print the data type of each and every element of both the variables list_ and
# arra_list.

# In[9]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)


for element in list_:
    print(type(element))


for element in array_list:
    print(type(element))


# Considering the following changes in the variable, array_list:
# array_list = np.array(object = list_, dtype = int)
# Will there be any difference in the data type of the elements present in both the variables, list_ and
# arra_list? If so then print the data types of each and every element present in both the variables, list_
# and arra_list.

# Yes, there will be a difference in the data type of the elements present in list_ and array_list after applying the dtype=int 
# argument.
# 
# By default, when creating a NumPy array from a list of strings like list_, the elements of the resulting array will be of the 
# numpy.str_ data type. However, when we specify the dtype=int argument, NumPy will attempt to convert the elements to the int 
# data type.

# In[10]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print("Data type of elements in original list:")
for element in list_:
    print(type(element))

array_list = np.array(object=list_, dtype=int)

print("\nData type of elements in updated array:")
for element in array_list:
    print(type(element))


# Consider the below code to answer further questions:
# import numpy as np
# num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
# num_array = np.array(object = num_list)
# Q4. Write a code to find the following characteristics of variable, num_array:
# (i) shape
# (ii) size

# In[11]:


import numpy as np

num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)


print("Shape of the array:", num_array.shape)


print("Size of the array:", num_array.size)


# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
# creation function.
# [Hint: The size of the array will be 9 and the shape will be (3,3).]

# In[12]:


import numpy as np

zeros_array = np.zeros(shape=(3,3))
print("Array of zeros:\n", zeros_array)


# Create an identity matrix of shape (5,5) using numpy functions?
# [Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]

# In[13]:


import numpy as np

identity_matrix = np.eye(N=5)
print("Identity matrix:\n", identity_matrix)


# In[ ]:





# In[ ]:




