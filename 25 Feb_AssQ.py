#!/usr/bin/env python
# coding: utf-8

# Consider following code to answer further questions:
# import pandas as pd
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})
# Q1. Write a code to print the data present in the second row of the dataframe, df.
# 

# In[32]:


print(df.iloc[1])


# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?

# loc: This function is used to select data from the DataFrame using labels (i.e., the row and column labels). It takes two 
#     arguments - the row label(s) and the column label(s). You can use this function to select data based on the row and column 
#     labels. For example, df.loc[2, 'duration'] will select the value in the 'duration' column for the row with label 2.
# 
# iloc: This function is used to select data from the DataFrame using integer indices (i.e., the row and column positions). 
#     It takes two arguments - the row index(es) and the column index(es). You can use this function to select data based on the
#     row and column positions. For example, df.iloc[2, 1] will select the value in the second column (i.e., 'duration') for the 
#     third row of the DataFrame.

# Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].
# 
# Did you observe any difference in both the outputs? If so then explain it.

# In[33]:


reindex = [3,0,1,2]
new_df = df.reindex(reindex)


# In[34]:


print(new_df.loc[2])
print(new_df.iloc[2])


# Yes, there will be a difference in the outputs of new_df.loc[2] and new_df.iloc[2].
# 
# new_df.loc[2] will return the row that has the label/index value of 2 after reindexing, which is the row with the course name 
# 'Big Data' and duration of 6.
# 
# new_df.iloc[2] will return the row that is located at the position/index of 2 after reindexing, which is the row with the 
# course name 'Machine Learning' and duration of 3.
# 
# So, new_df.loc[2] and new_df.iloc[2] will return different rows because they use different ways of indexing. .loc uses the 
# label/index value to retrieve rows, while .iloc uses the position/index to retrieve rows.

# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# (i) mean of each and every column present in the dataframe.
# (ii) standard deviation of column, ‘column_2’
# 

# In[ ]:


# (i) mean of each and every column present in the dataframe
df1.mean()

# (ii) standard deviation of column, ‘column_2’
df1['column_2'].std()


# In[ ]:





# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
# mean of column, column_2.
# If you are getting errors in executing it then explain why.
# [Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]

# In[ ]:


df1 = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']

df1.int[2, 'column_2'] = 'string variable'


mean_column_2 = df1['column_2'].mean()


# What do you understand about the windows function in pandas and list the types of windows
# functions?

# Rolling: This window function is used to apply a function over a rolling window of defined size on the DataFrame.
# 
# Expanding: This window function is used to apply a function to all the previous rows in the DataFrame.
# 
# EWM (Exponentially Weighted Moving): This window function is used to apply a function to a rolling window where the weights 
#     of the previous values decrease exponentially.
# 
# Rolling Apply: This window function is used to apply a custom function over a rolling window of defined size on the DataFrame.
# 
# Rolling Aggregate: This window function is used to apply multiple functions over a rolling window of defined size on the 
#     DataFrame.

# Write a code to print only the current month and year at the time of answering this question.
# [Hint: Use pandas.datetime function]

# In[46]:


from datetime import datetime

current_month_year = datetime.now().strftime('%B %Y')
print(current_month_year)


# Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The
# program should prompt the user to enter the dates and display the result.

# In[47]:


import pandas as pd


date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")


date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)


timedelta = date2 - date1


days = timedelta.days
hours = timedelta.seconds // 3600
minutes = (timedelta.seconds % 3600) // 60


print(f"The difference between {date1.date()} and {date2.date()} is {days} days, {hours} hours, and {minutes} minutes.")


# Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.

# In[ ]:


import pandas as pd


file_path = input("Enter the file path of the CSV file: ")
column_name = input("Enter the column name to convert: ")
category_order = input("Enter the category order (comma-separated): ").split(",")


df = pd.read_csv(file_path)

df[column_name] = pd.Categorical(df[column_name], categories=category_order)


df = df.sort_values(by=column_name)


print(df)


# Write a Python program that reads a CSV file containing sales data for different products and
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The
# program should prompt the user to enter the file path and display the chart.

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


file_path = input("Enter the file path of the CSV file: ")


df = pd.read_csv(file_path)


df['Date'] = pd.to_datetime(df['Date'])


df = df.set_index('Date')


df_resampled = df.groupby('Product Category').resample('M').sum()


df_resampled.plot(kind='bar', stacked=True)


plt.title('Sales by Product Category')
plt.xlabel('Month')
plt.ylabel('Sales')


plt.show()


# You are given a CSV file containing student data that includes the student ID and their test score. Write
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
# displays the results in a table.
# The program should do the followingM
# I Prompt the user to enter the file path of the CSV file containing the student dataR
# I Read the CSV file into a Pandas DataFrameR
# I Calculate the mean, median, and mode of the test scores using Pandas toolsR
# I Display the mean, median, and mode in a table.
# Assume the CSV file contains the following columnsM
# I Student ID: The ID of the studentR
# I Test Score: The score of the student's test.
# Example usage of the program:
# Enter the file path of the CSV file containing the student data: student_data.csv
# +-----------+--------+
# | Statistic | Value |
# +-----------+--------+
# | Mean | 79.6 |
# | Median | 82 |
# | Mode | 85, 90 |
# +-----------+--------+
# Assume that the CSV file student_data.csv contains the following data:
# Student ID,Test Score
# 1,85
# 2,90
# 3,80
# 4,75
# 5,85
# 6,82
# 7,78
# 8,85
# 9,90
# 10,85
# The program should calculate the mean, median, and mode of the test scores and display the results
# in a table.

# In[ ]:


import pandas as pd


file_path = input("Enter the file path of the CSV file containing the student data: ")


df = pd.read_csv(file_path)


mean = df["Test Score"].mean()
median = df["Test Score"].median()
mode = df["Test Score"].mode()


print("+-----------+--------+")
print("| Statistic | Value  |")
print("+-----------+--------+")
print(f"| Mean      | {mean:.1f}   |")
print("| Median    |", int(median), " "*(5-len(str(int(median)))), "|")
print(f"| Mode      | {', '.join(str(x) for x in mode)} |")
print("+-----------+--------+")


# In[ ]:





# In[ ]:




