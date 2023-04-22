#!/usr/bin/env python
# coding: utf-8

# List any five functions of the pandas library with execution.

# ##### read_csv() - This function reads a CSV file into a pandas DataFrame object.
# 
# import pandas as pd
# df = pd.read_csv('example.csv')
# print(df.head())
# 
# 
# ###describe() - This function provides summary statistics for numerical columns in a pandas DataFrame.
# 
# import pandas as pd
# df = pd.read_csv('example.csv')
# print(df.describe())
# 
# 
# ####groupby() - This function groups rows of a pandas DataFrame based on a specified column and performs an aggregation operation 
# (e.g. sum, mean, count) on each group.
# 
# 
# ###import pandas as pd
# df = pd.read_csv('example.csv')
# grouped_df = df.groupby('category').sum()
# print(grouped_df)
# 
# 
# dropna() - This function removes any rows in a pandas DataFrame that contain missing (NaN) values.
# 
# ###import pandas as pd
# df = pd.read_csv('example.csv')
# cleaned_df = df.dropna()
# print(cleaned_df.head())
# 
# ###pivot_table() - This function creates a pivot table from a pandas DataFrame, which summarizes the data by aggregating 
# values based on two or more columns.
# 
# import pandas as pd
# df = pd.read_csv('example.csv')
# pivot_df = df.pivot_table(values='sales', index='category', columns='region', aggfunc='sum')
# print(pivot_df)
# 

# In[20]:


pip install pandas


# Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[17]:


def reindex_dataframe(df):
    new_index = range(1, 2*len(df)+1, 2)
    df = df.set_index(pd.Index(new_index))
    return df


# In[ ]:





# You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.

# In[15]:


import pandas as pd

def sum_first_three(df):
    values_sum = 0
    for i, row in df.iterrows():
        if i < 3:
            values_sum += row['Values']
    print("Sum of first three values in 'Values' column:", values_sum)


# In[16]:


df = pd.DataFrame({'Values': [10, 20, 30, 40, 50]})
sum_first_three(df)


# How are DataFrame.size() and DataFrame.shape() different?

# DataFrame.size returns the total number of elements in the DataFrame, i.e., the number of rows multiplied by the number of 
# columns.
# DataFrame.shape returns a tuple representing the dimensions of the DataFrame, i.e., the number of rows and columns.

# Which function of pandas do we use to read an excel file?

# The function used to read an Excel file in pandas is pandas.read_excel().

# You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.
# The username is the part of the email address that appears before the '@' symbol. For example, if the
# email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your
# function should extract the username from each email address and store it in the new 'Username'
# column.

# In[20]:


import pandas as pd

def extract_username(df):
    df['Username'] = df['Email'].apply(lambda x: x.split('@')[0])
    return df


# In[21]:


df = pd.DataFrame({'Email': ['john.doe@example.com', 'jane.doe@example.com']})
df = extract_username(df)


# You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# For example, if df contains the following values:
# A B C
# 0 3 5 1
# 1 8 2 7
# 2 6 9 4
# 3 2 3 5
# 4 9 1 2
# Your function should select the following rows: A B C
# 1 8 2 7
# 4 9 1 2
# The function should return a new DataFrame that contains only the selected rows.

# In[22]:


import pandas as pd

def select_rows(df):
    return df[(df['A'] > 5) & (df['B'] < 10)]


# In[23]:


df = pd.DataFrame({'A': [3, 8, 6, 2, 9], 'B': [5, 2, 9, 3, 1], 'C': [1, 7, 4, 5, 2]})
selected_df = select_rows(df)


# Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.

# In[24]:


import pandas as pd

def calculate_statistics(df):
    values = df['Values']
    mean = values.mean()
    median = values.median()
    std_dev = values.std()
    return mean, median, std_dev


# In[25]:


df = pd.DataFrame({'Values': [1, 2, 3, 4, 5]})
mean, median, std_dev = calculate_statistics(df)


# Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

# In[26]:


import pandas as pd

def add_moving_average(df):
    # Calculate the rolling mean with a window of size 7 and including the current day
    rolling_mean = df['Sales'].rolling(window=7, min_periods=1).mean()
    # Add the rolling mean as a new column to the DataFrame
    df['MovingAverage'] = rolling_mean
    return df


# In[27]:


df = pd.DataFrame({'Date': pd.date_range('2022-01-01', periods=10, freq='D'), 'Sales': [10, 15, 13, 17, 19, 21, 18, 16, 14, 12]})
df_with_ma = add_moving_average(df)


# You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.
# For example, if df contains the following values:
# Date
# 0 2023-01-01
# 1 2023-01-02
# 2 2023-01-03
# 3 2023-01-04
# 4 2023-01-05
# Your function should create the following DataFrame:
# 
# Date Weekday
# 0 2023-01-01 Sunday
# 1 2023-01-02 Monday
# 2 2023-01-03 Tuesday
# 3 2023-01-04 Wednesday
# 4 2023-01-05 Thursday
# The function should return the modified DataFrame.

# In[28]:


import pandas as pd

def add_weekday(df):
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    # Extract the weekday name from the 'Date' column and store it in a new column 'Weekday'
    df['Weekday'] = df['Date'].dt.day_name()
    return df


# In[29]:


df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']})
df_with_weekday = add_weekday(df)


# Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# In[30]:


import pandas as pd

def select_january(df):
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    # Select all rows where the date is between '2023-01-01' and '2023-01-31'
    mask = (df['Date'] >= '2023-01-01') & (df['Date'] <= '2023-01-31')
    result = df.loc[mask]
    return result


# To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

# In[31]:


import pandas as pd


# In[ ]:




