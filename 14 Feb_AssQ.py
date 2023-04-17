#!/usr/bin/env python
# coding: utf-8

#  What is multithreading in python? Why is it used? Name the module used to handle threads in python.

# Multithreading is a programming technique that allows multiple threads of execution to run concurrently within a single process. 
# In Python, multithreading is achieved using the threading module.
# 
# Multithreading is used to improve the performance and responsiveness of a program, particularly when dealing with I/O-bound 
# tasks or tasks that can be parallelized. By allowing multiple threads to run concurrently, a program can perform multiple tasks 
# simultaneously, potentially reducing the overall time it takes to complete a task.
# 
# The threading module in Python provides a simple and efficient way to create and manage threads. It includes functions for 
# creating and starting new threads, as well as for synchronizing the execution of multiple threads. The module also includes 
# tools for handling common threading problems, such as race conditions and deadlocks.

# Why threading module used? Write the use of the following functions activeCount() currentThread() enumerate()

# The threading module is used in Python to create and manage threads of execution. It provides a simple and efficient way to 
# run multiple tasks concurrently within a single process.
# 
# activeCount(): This function returns the number of Thread objects that are currently active in the current Python interpreter. 
#     It can be useful for monitoring the progress of a program that uses multiple threads, as it provides a way to check how 
#     many threads are currently running.
# 
# currentThread(): This function returns a reference to the currently executing Thread object. It can be used to obtain 
#     information about the current thread, such as its name or identification number.
# 
# enumerate(): This function returns a list of all active Thread objects in the current Python interpreter. It can be useful 
#     for monitoring the status of all threads in a program, as it provides a way to iterate over all threads and obtain 
#     information about each one.

#  Explain the following functions run() start() join() isAlive()

# run(): This method is called when a new thread is started and contains the code that will be executed in the new thread. 
#     To create a new thread, you create a new instance of the Thread class and pass in the function that you want to run in 
# the new thread as the target parameter. The run method of the Thread class will then be called automatically when the thread is 
# started.
# 
# start(): This method is used to start a new thread. It calls the run method of the Thread object in a new thread of execution. 
#     It is important to note that the run method should not be called directly, as it will execute in the current thread of 
#     execution rather than in a new thread.
# 
# join(): This method is used to wait for a thread to finish executing before continuing with the main thread of execution. 
#     When the join method is called on a Thread object, the main thread will block until the target thread has finished 
#     executing.
# 
# isAlive(): This method returns a boolean value indicating whether the thread is currently executing. It can be used to 
#     check the status of a thread at any point during the program's execution.
# 

# Write a python program to create two threads. Thread one must print the list of squares and thread two must print the list of 
# cubes.

# In[1]:


import threading

def print_squares(numbers):
    for num in numbers:
        square = num * num
        print(f"{num} squared is {square}")

def print_cubes(numbers):
    for num in numbers:
        cube = num * num * num
        print(f"{num} cubed is {cube}")


numbers = [1, 2, 3, 4, 5]


t1 = threading.Thread(target=print_squares, args=(numbers,))
t2 = threading.Thread(target=print_cubes, args=(numbers,))


t1.start()
t2.start()


t1.join()
t2.join()


# State advantages and disadvantages of multithreading.

# Advantages:
# 
# Improved performance: Multithreading can improve the performance of an application by allowing multiple threads to execute 
#     concurrently. This can reduce the amount of time it takes to complete a task and increase the overall throughput of the 
#     application.
# 
# Improved responsiveness: Multithreading can improve the responsiveness of an application by allowing the user interface to 
#     remain responsive while long-running tasks are executed in the background.
# 
# Resource sharing: Multithreading allows threads to share resources such as memory, which can reduce the amount of memory 
#     needed by the application.
#     
#     
# Disadvantages:
# 
# Complexity: Multithreaded applications can be more complex to develop and debug than single-threaded applications. This is 
#     because threads must coordinate with each other and share resources in a way that avoids conflicts.
# 
# Synchronization overhead: Multithreading can introduce synchronization overhead, as threads must coordinate with each other 
#     to avoid conflicts when accessing shared resources.
# 
# Race conditions: Multithreading can introduce race conditions, where the outcome of a computation depends on the order in 
#     which threads execute. These can be difficult to detect and debug.

# Explain deadlocks and race conditions.

# Deadlocks occur when two or more threads are blocked waiting for each other to release resources. This can happen when each 
# thread holds a resource that the other thread needs, and neither thread is willing to release its resource until it has 
# obtained the other resource. This can result in a situation where both threads are blocked and cannot make progress, even 
# though there are no technical errors in the code.
# 
# Race conditions occur when the outcome of a computation depends on the order in which threads execute. This can happen when 
# multiple threads access and modify shared resources without proper synchronization. For example, if two threads try to modify 
# the same variable at the same time, it's possible that the final value of the variable will depend on the order in which the 
# threads execute.

# In[ ]:




