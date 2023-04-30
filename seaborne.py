#!/usr/bin/env python
# coding: utf-8

# Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.

# Histograms: A histogram is used to visualize the distribution of a numerical variable. Seaborn provides the distplot() 
#     function to plot histograms.
# 
# Scatter plots: A scatter plot is used to visualize the relationship between two numerical variables. Seaborn provides the 
#     scatterplot() function to plot scatter plots.
# 
# Line plots: A line plot is used to visualize the trend of a numerical variable over time. Seaborn provides the lineplot() 
#     function to plot line plots.
# 
# Box plots: A box plot is used to visualize the distribution of a numerical variable across different categories. Seaborn 
#     provides the boxplot() function to plot box plots.
# 
# Heat maps: A heat map is used to visualize the relationship between two categorical variables. Seaborn provides the heatmap() 
#     function to plot heat maps.

# Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
# "timepoint" and y = "signal" for different events and regions.
# Note: timepoint, signal, event, and region are columns in the fmri dataset.

# In[10]:


import seaborn as sns


fmri_data = sns.load_dataset("fmri")


sns.lineplot(x="timepoint", y="signal", hue="event", style="region", data=fmri_data)


# Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
# 'pclass', y = 'age' and y = 'fare'.
# Note: pclass, age, and fare are columns in the titanic dataset.

# In[11]:


import seaborn as sns


titanic_data = sns.load_dataset("titanic")


sns.boxplot(x="pclass", y="age", data=titanic_data)


sns.boxplot(x="fare", y="age", data=titanic_data)


# Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
# parameter for the 'cut' column of the diamonds dataset.

# In[12]:


import seaborn as sns


diamonds_data = sns.load_dataset("diamonds")


sns.histplot(data=diamonds_data, x="price", hue="cut")


# Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
# of the iris dataset.

# In[13]:


import seaborn as sns


iris_data = sns.load_dataset("iris")


sns.pairplot(data=iris_data, hue="species")


# Use the "flights" dataset from seaborn to plot a heatmap.

# In[14]:


import seaborn as sns


flights_data = sns.load_dataset("flights")


flights_pivot = flights_data.pivot("month", "year", "passengers")


sns.heatmap(flights_pivot, annot=True, fmt="d")


# In[ ]:




