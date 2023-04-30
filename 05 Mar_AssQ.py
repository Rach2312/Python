#!/usr/bin/env python
# coding: utf-8

# How can you create a Bokeh plot using Python code?

# In[31]:


from bokeh.plotting import figure, output_file, show


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


p = figure(title="Simple Bokeh plot", x_axis_label='x', y_axis_label='y')


p.line(x, y, legend_label="Line")


output_file("bokeh_plot.html")


show(p)


# What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.

# In Bokeh, glyphs are the visual elements that represent data points in a plot. They can take on a variety of shapes, 
# including circles, squares, triangles, and more, and can be customized in various ways, such as changing their size, color, 
# and transparency.

# In[32]:


from bokeh.plotting import figure, output_file, show


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


p = figure(title="Glyphs in Bokeh", x_axis_label='x', y_axis_label='y')


p.circle(x, y, size=20, color="blue", alpha=0.5)


p.square(x, y, size=15, color="red", alpha=0.8)


output_file("bokeh_glyphs.html")


show(p)


# Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?

# In[33]:


from bokeh.plotting import figure, output_file, show


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


p = figure(title="Customizing a Bokeh Plot", x_axis_label='X Axis Label', y_axis_label='Y Axis Label', 
           width=800, height=400, toolbar_location='above')


p.title.text_font_size = '18pt'
p.title.align = 'center'
p.title.text_color = 'blue'


p.xaxis.axis_label_text_font_size = '14pt'
p.yaxis.axis_label_text_font_size = '14pt'
p.xaxis.major_label_text_font_size = '12pt'
p.yaxis.major_label_text_font_size = '12pt'
p.xaxis.axis_line_color = 'red'
p.xaxis.axis_label_standoff = 20


p.circle(x, y, size=20, color="blue", alpha=0.5, legend_label="Circle Glyph")
p.square(x, y, size=15, color="red", alpha=0.8, legend_label="Square Glyph")
p.legend.location = "top_left"
p.legend.label_text_font_size = "14pt"
p.legend.background_fill_alpha = 0.5


output_file("bokeh_customization.html")


show(p)


# What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
# real time?

# A Bokeh server is a way to create interactive data visualization applications using Bokeh in Python. With Bokeh server, 
# you can build a web application that allows users to interact with your data visualization in real-time, using widgets and 
# callbacks to update the plot based on user input.

# In[37]:


from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
import numpy as np


source = ColumnDataSource(data=dict(x=[], y=[], color=[]))


plot = figure(title="Real-time scatter plot")
plot.circle('x', 'y', color='color', source=source)


def update():
    new_data = dict(
        x=np.random.normal(size=100),
        y=np.random.normal(size=100),
        color=np.random.choice(['red', 'blue', 'green'], size=100)
    )
    source.stream(new_data)


curdoc().add_periodic_callback(update, 1000)


curdoc().title = "Real-time scatter plot"
curdoc().add_root(plot)


# How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?

# Both Flask and Django are popular web frameworks in Python that can be used to build web applications that include Bokeh plots.

# In[36]:


from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
   
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    plot = figure(title="My Bokeh Plot", x_axis_label="X", y_axis_label="Y")
    plot.circle(x, y)

    
    script, div = components(plot, CDN)

  
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




