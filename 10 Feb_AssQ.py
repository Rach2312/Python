#!/usr/bin/env python
# coding: utf-8

# Which function is used to open a file? What are the different modes of opening a file? Explain each mode
# of file opening.

# In Python, the built-in function open() is used to open a file.
# 
# The open() function takes two arguments: the first argument is the name of the file to be opened, and the 
# second argument is the mode in which the file should be opened.
# 
# The different modes of opening a file are:
# 
# "r": read mode. This is the default mode. It opens the file for reading, and if the file does not exist, it raises an error.
# 
# "b": binary mode. It opens the file in binary mode, which is used for non-text files like images, videos, etc.
# 
# "x": exclusive creation mode. It opens the file for writing, but it only succeeds if the file does not already exist. 
#     If the file already exists, it raises an error.
#     
# "a": append mode. It opens the file for writing, but it does not truncate the file. If the file does not exist, it creates a 
#     new file.
#     
# "t": text mode. This is the default mode. It opens the file in text mode, which is used for text files like .txt, .csv, etc.
# 
# "+": read and write mode. It opens the file for both reading and writing.
# 
# "w": write mode. It opens the file for writing. If the file does not exist, it creates a new file. If the file already exists, 
#     it truncates the file to zero length.
#     
#  Always close the file after you are done working with it by calling the close() method of the file object.

# Why close() function is used? Why is it important to close a file?

# The close() function is used to close a file after it has been opened in Python.
# 
# It is important to close a file after you are done working with it for several reasons:
#     
# Release resources: When you open a file in Python, it uses system resources to maintain the connection with the file. 
# If you don't close the file, those resources may not be released until the program terminates, which could cause issues 
# with memory usage or file locking.
# 
# Saving changes: When you write to a file in Python, the changes are not immediately written to the file. 
# Instead, they are buffered in memory until the buffer is full or until you close the file. If you don't close the file, 
# the changes may not be saved properly.
# 
# Other programs: If you don't close a file, other programs may not be able to access or modify it until your program terminates.
# This can cause conflicts or errors when multiple programs are trying to access the same file.
# 
# To close a file in Python, you can simply call the close() method on the file object

# Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then
# close the file. Open this file and read the content of the file.

# In[1]:


file = open("data_science.txt", "w")


file.write("I want to become a Data Scientist")


file.close()


file = open("data_science.txt", "r")


contents = file.read()


print(contents)


file.close()


# Explain the following with python code: read(), readline() and readlines().

# read(): The read() method reads the entire contents of the file as a string. 
#     It takes an optional argument that specifies the number of characters to read from the file. 
#     If no argument is provided, it reads the entire file.

# In[ ]:


file = open("example.txt", "r")

contents = file.read()

print(contents)

file.close()


# readline(): The readline() method reads a single line from the file and returns it as a string. 
#     It reads from the current position in the file until it encounters a newline character (\n), and then returns 
#     the line that was read.
# 

# In[ ]:



file = open('example.txt', 'r')

line = file.readline()

print(line)

line = file.readline()

print(line)

file.close()


# readlines(): This method is used to read all the lines of a file and returns them as a list of strings. 
#     Each string in the list represents a single line from the file.

# In[ ]:



file = open('example.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line)

file.close()


# Explain why with statement is used with open(). What is the advantage of using with statement and
# open() together?

# In Python, the with statement is used in conjunction with the open() function to work with files. 
# The with statement ensures that the file is properly closed after it's been used, regardless of whether an exception is 
# raised or not.
# 
# The advantage of using the with statement with open() is that it simplifies the code and makes it more readable. 
# It also ensures that the file is properly closed, which is important for several reasons:
# 
# If a file is not properly closed, it can lead to data loss or corruption.
# Leaving a file open can consume system resources and cause other issues.
# It's good programming practice to always clean up after oneself.
# 
# Here's an example of how to use the with statement with open():

# In[ ]:



with open('example.txt', 'r') as file:

    data = file.read()

    print(data)


# In the above example, the with statement is used to open the file, and the file object is assigned to the variable file. 
# The code inside the with block is executed, and when the block is exited, the file is automatically closed. 
# This ensures that the file is properly closed, 
# even if an exception is raised.

# Explain the write() and writelines() functions. Give a suitable example.

# write(): This method is used to write a string to a file. It takes a string argument that represents the data to be written. 
#     It writes the string to the file, starting at the current position, and returns the number of characters written.

# In[4]:


file = open('example.txt', 'w')

file.write('Hello, world!\n')
file.write('How are you?\n')

file.close()


# writelines(): This method is used to write a list of strings to a file. Each string in the list represents a line of text to be 
#     written to the file. It writes each string to the file, starting at the current position.

# In[5]:


file = open('example.txt', 'w')

lines = ['Hello, world!\n', 'How are you?\n']
file.writelines(lines)

file.close()


# In[ ]:




