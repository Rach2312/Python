#!/usr/bin/env python
# coding: utf-8

# Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[9]:


import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)
print(series)


# Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[1]:


import pandas as pd

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_series = pd.Series(my_list)
print(my_series)


# Q3. Create a Pandas DataFrame that contains the following data:
# 
# Then, print the DataFrame.

# In[2]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}

df = pd.DataFrame(data)
print(df)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In Pandas, DataFrame is a two-dimensional labeled data structure with columns of potentially different types, whereas 
# Series is a one-dimensional labeled array with homogeneous data type.
# 
# In other words, a DataFrame can be thought of as a table with rows and columns, similar to an Excel spreadsheet, while a 
# Series is a single column of data.

# In[3]:


import pandas as pd


fruits = pd.Series(['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry'])
print(fruits)


data = {'Fruit': ['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry'], 'Color': ['Red', 'Yellow', 'Red', 'Green', 'Purple']}
df = pd.DataFrame(data)
print(df)


# What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# head() and tail(): Used to show the first or last few rows of the DataFrame.
# 
# describe(): Used to generate a statistical summary of the DataFrame, including count, mean, standard deviation, minimum, 
#     maximum, and quartiles.
# 
# loc[] and iloc[]: Used to select data by label or by integer position.
# 
# groupby(): Used to group the data in the DataFrame based on one or more columns.

# In[4]:


import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'B', 'C', 'C'],
    'Sales': [100, 200, 150, 250, 300, 350],
    'Profit': [10, 20, 15, 25, 30, 35]
}

df = pd.DataFrame(data)

sales_by_region = df.groupby('Region').sum()
print(sales_by_region)


# Which of the following is mutable in nature Series, DataFrame, Panel?

# In Pandas, both Series and DataFrame are mutable in nature, which means that their values can be modified after they are 
# created.

# Create a DataFrame using multiple Series. Explain with an example.

# In[5]:


import pandas as pd


names = pd.Series(['Alice', 'Bob', 'Claire'])
ages = pd.Series([25, 30, 27])
genders = pd.Series(['Female', 'Male', 'Female'])


df = pd.concat([names, ages, genders], axis=1)
df.columns = ['Name', 'Age', 'Gender'] # Set column names

print(df)


# In[ ]:




