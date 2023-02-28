#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= "Xyz"


# In[2]:


type(a)


# In[3]:


int()


# In[4]:


int("123")


# In[5]:


int(abc)


# In[6]:


age= 23
print("My age is:", age)
# for formating purpose f is added
print(f"My age is: {age}")


# In[7]:


## format()
name= "Prachi"
age= 23
print("My name is {} and age is {}".format(name,age))
print("My name is {} and age is {}".format(age,name))


# In[ ]:


## Issue in print("My name is {} and age is {}".format(age,name)) this. to over come that Place holder is used


# In[8]:


## place holder
print("My name is {firstname} and age is {firstage}".format(firstage=age,firstname=name))


# In[11]:


## Practices
name= "Prachi Khare"
age= 23
degree= "MSc"
print("My age is {firstage} and i have completed: my degree of {firstdegree} with the name of {firstname}".format(firstage=age,firstdegree=degree,firstname=name))


# In[12]:


print("My age is {firstage} and i have completed: my degree of {firstdegree} with the name of {firstname}".format(firstage=age,firstdegree=degree,firstname=name))


# In[13]:


name= "Prachi Khare"
age= 23
degree= "MSc"
print("My age is {firstage} and i have completed: my degree of {firstdegree} with the name of {firstname}".format(firstage=age,firstdegree=degree,firstname=name))


# In[ ]:


## Control Flow
### Decision making statement
1 if
2 if else
3 if elif else
4 Nested if
5 single statement suites


# In[14]:


## If statement
## colon indicates start of the statement
age=18
if age>=18:
    print("You are eligible to drink")
if age<18:
    print("You are eligible to drink")


# In[15]:


## default data type of input is string
name=input("Enter the name ")


# In[ ]:


name


# In[16]:


age=int(input("Enter your age"))
## as input is string for numerical value add int before


# In[ ]:


age


# In[ ]:


## Task
# input of age
## Wether age >=18 and <=45
## display you are young blood


# In[17]:


age=int(input("Enter your age "))
if age>=18 and age<=45:
    print("You are young blood")


# In[18]:


age=int(input("Enter your age "))
if age>=18 and age<=45:
    print("You are young blood")


# In[19]:


## if else
age=int(input("Enter your age "))
if age>=18 and age<=45:
    print("You are young blood")
else:
    print("Thank you for application we will let you know")


# In[ ]:


##  input product price
# product > 1000 rs 20% 
#  print price after discount
# product <= 1000rs 30% 
#  print price after discount


# In[20]:


product_price=int(input("Enter product price "))
if product_price> 1000:
    print(f"Price of product is {product_price*0.8}")
else:
    print(f"Price of product is {product_price*0.7}")


# In[21]:


product_price=int(input("Enter product price "))
if product_price> 1000:
    print(f"Price of product is {product_price*0.8}")
else:
    print(f"Price of product is {product_price*0.7}")


# In[ ]:


##  input product price
# product > 3000 rs 20% 
#  print price after discount
## product >= 2000 rs and <=3000 30% 
#  print price after discount
# product <= 1000rs and <=2000 40% 
#  print price after discount


# In[22]:


product_price=int(input("Enter product price "))
if product_price> 3000:
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    print(f"Price of product is {product_price*0.7}")
else:
    print(f"Price of product is {product_price*0.6}")


# In[23]:


product_price=int(input("Enter product price "))
if product_price> 3000:
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    print(f"Price of product is {product_price*0.7}")
else:
    print(f"Price of product is {product_price*0.6}")


# In[24]:


product_price=int(input("Enter product price "))
if product_price> 3000:
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    print(f"Price of product is {product_price*0.7}")
else:
    print(f"Price of product is {product_price*0.6}")


# In[25]:


product_price=int(input("Enter product price "))
if product_price> 3000:
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    print(f"Price of product is {product_price*0.7}")
elif product_price>=1000 and product_price<=2000:
    print(f"Price of product is {product_price*0.6}")
else:
    print("Lets go to park")


# In[ ]:


##  input product price
# product > 3000 rs 20% 
#  print price after discount
## product >= 2000 rs and <=3000 30% 
## price== 2999 - Get a gift
#  print price after discount
# product <= 1000rs and <=2000 40% 
#  print price after discount


# In[26]:


product_price=int(input("Enter product price "))
if product_price> 3000:
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    if product_price==2999:
        print("Congrats Won Additional gift")
    print(f"Price of product is {product_price*0.7}")
else:
    print(f"Price of product is {product_price*0.6}")


# In[ ]:


##  input product price
# product > 3000 rs 20% 
## Price == 4000 - Trip t0o Bali
#  print price after discount
## product >= 2000 rs and <=3000 30% 
## price== 2999 - Get a gift
#  print price after discount
# product <= 1000rs and <=2000 40% 
#  print price after discount


# In[27]:


## Comparision Operator
product_price=int(input("Enter product price "))
if product_price> 3000:
    if product_price==4000:
        print("Won a Bali Trip")
    print(f"Price of product is {product_price*0.8}")
elif product_price>=2000 and product_price<=3000:
    if product_price==2999:
        print("Congrats Won Additional gift")
    print(f"Price of product is {product_price*0.7}")
else:
    print(f"Price of product is {product_price*0.6}")


# In[28]:


## Single statement
val=int(input("Enter the number"))
if(val<=999): print("Value is less than 1000")


# In[ ]:


# Loop Statement
## While Loop
## for Loop
## nested Loop
## Loop Control (Break, Continue, Pass)


# In[35]:


## While Loop
joining_age=30
while joining_age<=60:
    joining_age=joining_age+1
    print(joining_age)
else:
    print("Its time to retire")


# In[36]:


## While Loop - the repetition of a process or utterance.
joining_age=30
while joining_age<=60:
    print(joining_age)
    joining_age=joining_age+1
else:
    print("Its time to retire")


# In[39]:


## ATM == 1000rs
total_amount=1000
while total_amount!=0:
    print(total_amount)
    total_amount=total_amount-100
else:
    print("Fill up Machine")


# In[46]:


## For Loop- 
lst=["Apple","Prachi",1,2,3,"pineapple"]
type(lst)
lst[3]


# In[47]:


lst[4]


# In[48]:


for x in lst:
    print(x)


# In[53]:


for x in lst:
    print(x)
    if x=="Prachi":
        print("Prachi Khare Here")


# In[59]:


for x in lst:
    print(x,end='')
    if x=="Prachi":
        print("Prachi Khare Here")


# In[60]:


## nested Loop
n=7
## Range - Return an object that produces a sequence of integers from start (inclusive)to stop (exclusive) by step
range(1,7)


# In[61]:


for i in range(1,7):
    print(i)


# In[63]:


for i in range(1,20,3):
    print(i)


# In[64]:


n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')


# In[65]:


n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='\n')


# In[68]:


n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print('\r')


# In[71]:


n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print('\n')


# In[78]:


n=10
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end='')
    print('\r')


# In[80]:


## Loop controls
## Break stop the loop completely
lst=["Apple","Prachi",1,2,3,"pineapple"]
for i in lst:
    if i=="Prachi":
        print("Prachi Khare Here")
        break
    print(i)


# In[81]:


## Pass doesnt do anything
lst=["Apple","Prachi",1,2,3,"pineapple"]
for i in lst:
    if i=="Prachi":
        print("Prachi Khare Here")
        pass
    print(i)


# In[82]:


# In continue its skips only  one step
lst=["Apple","Prachi",1,2,3,"pineapple"]
for i in lst:
    if i=="Prachi":
        print("Prachi Khare Here")
        continue
    print(i)


# In[ ]:





# In[ ]:




