#!/usr/bin/env python
# coding: utf-8

# Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
# scatter plot for age and fare columns in the titanic dataset.

# In[17]:


import seaborn as sns
import plotly.express as px


titanic_data = sns.load_dataset("titanic")


scatter_plot = px.scatter(titanic_data, x="age", y="fare")


scatter_plot.show()


# Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

# In[18]:


import plotly.express as px
import seaborn as sns


tips = sns.load_dataset("tips")


fig = px.box(tips, x="day", y="total_bill", color="smoker", title="Tips Dataset - Total Bill per Day")
fig.show()


# Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.

# In[19]:


import seaborn as sns
import plotly.express as px


tips = sns.load_dataset("tips")


fig = px.histogram(tips, x="sex", y="total_bill", color="day", barmode="group", histfunc="sum",
                   pattern_shape="smoker")


fig.show()


# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.

# In[29]:


import plotly.express as px
df = px.data.iris()
fig = px.scatter_matrix(df, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species")
fig.show()


# What is Distplot? Using Plotly express, plot a distplot.

# A distplot (distribution plot) is a graphical representation of the distribution of data. It is essentially a histogram with
# a smooth curve drawn over it. It is useful for visualizing the probability density function of a continuous variable.

# In[30]:


import plotly.express as px
import numpy as np


np.random.seed(1)
x = np.random.randn(1000)


fig = px.histogram(x, nbins=30, marginal="rug", opacity=0.7, color_discrete_sequence=['blue'])

fig.update_layout(
    title_text="Distplot",
    xaxis_title_text="Value",
    yaxis_title_text="Density",
)

fig.show()


# In[ ]:




