#!/usr/bin/env python
# coding: utf-8

# What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
# Matplotlib.

# Matplotlib is a popular data visualization library in Python used for creating static, interactive, and animated visualizations
# in Python. It is used for creating high-quality charts, plots, and graphs to represent data in a visually appealing manner.
# 
# Matplotlib provides a range of functionalities, including different types of plots such as line plots, scatter plots, bar 
# plots, histograms, pie charts, and more. It is also highly customizable, allowing users to adjust various aspects of their 
# visualizations, including colors, fonts, and labels.
# 
# Line Plot: A simple line plot can be created using the plot() function in Pyplot. This is useful for visualizing trends in
#     continuous data.
# 
# Scatter Plot: A scatter plot can be created using the scatter() function in Pyplot. This is useful for visualizing the 
#     relationship between two continuous variables.
# 
# Bar Plot: A bar plot can be created using the bar() function in Pyplot. This is useful for visualizing the distribution of 
#     categorical data.
# 
# Histogram: A histogram can be created using the hist() function in Pyplot. This is useful for visualizing the distribution of 
#     continuous data.
# 
# Pie Chart: A pie chart can be created using the pie() function in Pyplot. This is useful for visualizing proportions of a 
#     categorical variable.

# What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.
# import numpy as np
# np.random.seed(3)
# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))
# Note: Also add title, xlabel, and ylabel to the plot.

# In[1]:


import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))


# In[2]:


x


# In[3]:


y


# In[6]:


import matplotlib.pyplot as plt

import numpy as np

plt.scatter(x,y)

plt.title("Relationship between x and y")

plt.xlabel("x")
plt.ylabel("y")

plt.show()


# Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# Use the following data:
# import numpy as np
# For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])

# The subplot() function takes three arguments that describes the layout of the figure. The layout is organized in rows and 
# columns, which are represented by the first and second argument. The third argument represents the index of the current 

# In[7]:


import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])


x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])


x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])


x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])


fig, axs = plt.subplots(2, 2, figsize=(8, 8))


axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Line 1')


axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line 2')


axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('Line 3')


axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('Line 4')


fig.suptitle('Four Line Plots')


plt.show()


# Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
# import numpy as np
# company = np.array(["Apple", "Microsoft", "Google", "AMD"])
# profit = np.array([3000, 8000, 1000, 10000])
# 

# The purpose of a bar graph is to convey relational information quickly in a visual manner. The bars display the value for a 
# particular category of data. The vertical axis on the left or right side of the bar graph is called the y-axis.

# In[8]:


import matplotlib.pyplot as plt
import numpy as np


company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])


plt.bar(company, profit)
plt.title("Profit by Company")
plt.xlabel("Company")
plt.ylabel("Profit")
plt.show()


plt.barh(company, profit)
plt.title("Profit by Company")
plt.xlabel("Profit")
plt.ylabel("Company")
plt.show()


# What is a box plot? Why is it used? Using the following data plot a box plot.
# box1 = np.random.normal(100, 10, 200)
# box2 = np.random.normal(90, 20, 200)

# Box plots are used to show distributions of numeric data values, especially when you want to compare them between multiple 
# groups. They are built to provide high-level information at a glance, offering general information about a group of data's 
# symmetry, skew, variance, and outliers.

# In[9]:


import matplotlib.pyplot as plt
import numpy as np


box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
data = [box1, box2]


plt.boxplot(data)
plt.title("Box Plot")
plt.xlabel("Data")
plt.ylabel("Values")
plt.xticks([1, 2], ['Box 1', 'Box 2'])
plt.show()


# In[ ]:




