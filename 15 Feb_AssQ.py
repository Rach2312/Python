#!/usr/bin/env python
# coding: utf-8

# What is multiprocessing in python? Why is it useful?

# Multiprocessing in Python refers to the ability of a program to run multiple processes or tasks concurrently on a multi-core 
# or multi-CPU machine, in order to improve performance and reduce execution time. It allows a Python program to split a workload
# across multiple CPUs or cores, thereby achieving parallelism and improving the overall efficiency of the program.
# 
# Speed up the execution of CPU-bound tasks that can be parallelized, such as numerical computations, image processing, and 
# machine learning.
# 
# Take advantage of the processing power of multi-core or multi-CPU machines to run multiple tasks concurrently, such as 
# serving multiple clients in a web application.
# 
# Isolate the execution of long-running or potentially unstable tasks, such as network I/O or file I/O operations, 
# from the main program, thereby improving its stability and responsiveness.
# 
# Design distributed systems that can scale horizontally by running multiple processes on multiple machines.
# 

# What are the differences between multiprocessing and multithreading?
# 

# Multiprocessing involves running multiple processes concurrently, with each process running on a separate CPU or core. 
# Each process has its own memory space and can execute tasks independently of the other processes. Communication between 
# processes can be achieved through inter-process communication (IPC) mechanisms like pipes or queues.
# 
# On the other hand, multithreading involves running multiple threads of execution within a single process, with each thread 
# executing independently but sharing the same memory space. Threads share data and resources with each other, which can lead 
# to synchronization issues and race conditions if not properly managed. Communication between threads can be achieved through 
# synchronization mechanisms like locks, semaphores, and condition variables.
# 
# 

# Write a python code to create a process using the multiprocessing module.

# In[2]:


import multiprocessing

def my_process():
    print("This is my process!")

if __name__ == '__main__':
    process = multiprocessing.Process(target=my_process)
    process.start()
    process.join()


# What is a multiprocessing pool in python? Why is it used?

# A multiprocessing pool in Python is a collection of worker processes that can be used to execute multiple tasks in parallel. 
# It provides a simple and efficient way to distribute workloads across multiple CPUs or cores and achieve parallelism.
# 
# Improved performance: By distributing workloads across multiple CPUs or cores, a multiprocessing pool can improve the 
#     performance of CPU-bound tasks that can be parallelized, such as numerical computations, image processing, and machine 
#     learning.
# 
# Simplified code: A multiprocessing pool abstracts away the details of process creation and communication, making it easier 
#     to write parallel code without worrying about low-level details.
# 
# Load balancing: A multiprocessing pool automatically distributes tasks among worker processes, ensuring that each process 
#     has a roughly equal workload and preventing any single process from becoming a bottleneck.

# How can we create a pool of worker processes in python using the multiprocessing module?

# In[ ]:


import multiprocessing

def worker(num):
    """This is the function that will be executed by the worker process."""
    print(f"Worker {num} is starting")
    # do some work here...
    print(f"Worker {num} is done")

if __name__ == '__main__':
    num_processes = 4  
    with multiprocessing.Pool(num_processes) as pool:
     
        tasks = [1, 2, 3, 4, 5] 
        results = pool.map(worker, tasks)  
        print(results) 


# Write a python program to create 4 processes, each process should print a different number using the
# multiprocessing module in python.

# In[ ]:


import multiprocessing

def print_number(num):
    """This function prints a number."""
    print(f"Process {multiprocessing.current_process().name} printed {num}")

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=print_number, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# In[ ]:




