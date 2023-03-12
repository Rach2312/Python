

 Which keyword is used to create a function? Create a function to return a list of odd numbers in the
 range of 1 to 25.
 
 The keyword used to create a function in Python is "def".

 In[2]:


def get_odd_numbers():
    odd_numbers = []
    for i in range(1, 26):
        if i % 2 == 1:
            odd_numbers.append(i)
    return odd_numbers

get_odd_numbers()


 Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
 demonstrate their use.
 
 In Python, *args and **kwargs are used in function definitions to allow a function to accept an arbitrary number of arguments.
 
 *args is used to pass a variable number of non-keyword arguments to a function. It allows you to pass a variable number of 
 arguments to a function without knowing beforehand how many arguments 
 will be passed or what their values will be. Inside the function, the arguments passed through *args are treated as a tuple.

 In[4]:


def sum_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_numbers(1, 2, 3))   Output: 6
print(sum_all_numbers(10, 20, 30, 40)) 


 In[5]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=25, city="New York")


 What is an iterator in python? Name the method used to initialise the iterator object and the method
 used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
 18, 20].
 
 An iterator in Python is an object that implements the iterator protocol, which consists of two methods: iter() and next(). 
     The iter() method returns the iterator object itself, and the next() method returns the next value from the iterator.
     When there are no more items to return, the next() method should raise the StopIteration exception.
 
 To initialize an iterator object in Python, you can call the iter() function on an iterable object such as a list or a string. 
 To iterate over the items in the iterable, you can use a for loop or call the next() method on the iterator object.
 

 In[6]:


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iter = iter(my_list)


for i in range(5):
    print(next(my_iter))


 What is a generator function in python? Why yield keyword is used? Give an example of a generator
 function.
 
 A generator function in Python is a special type of function that allows you to generate a sequence of values on-the-fly, 
 without needing to store them all in memory at once. Instead of returning a value using the "return" keyword, a generator 
 function uses the "yield" keyword to temporarily suspend the function's execution and return a value to the caller. 
 When the generator function is called again, it resumes where it left off and continues executing until it hits another 
 yield statement or reaches the end of the function.
 
 The yield keyword is used to define the values that the generator function will return. Each time the generator function is 
 called, it returns the next value in the sequence until there are no more values to yield. When the function reaches the end 
 of its code or executes a return statement, the generator is closed and cannot be used again.

 In[8]:


def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


 Create a generator function for prime numbers less than 1000. Use the next() method to print the
 first 20 prime numbers.
 
 
 
 

 In[9]:


def primes_less_than_1000():
   
    primes = [2, 3]

     Yield the first two primes
    yield 2
    yield 3

   
    for num in range(5, 1000, 2):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
            if prime * prime > num:
                break
        if is_prime:
            primes.append(num)
            yield num


prime_gen = primes_less_than_1000()
for i in range(20):
    print(next(prime_gen))


 In[ ]:




