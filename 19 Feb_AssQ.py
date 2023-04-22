#!/usr/bin/env python
# coding: utf-8

# What is Flask Framework? What are the advantages of Flask Framework?

# Flask is a micro web framework for Python that is used to build web applications. It is a lightweight framework that is easy 
# to use and requires minimal setup, making it a popular choice for small to medium-sized projects.
# 
# 
# Lightweight and flexible: Flask is a minimalistic framework that allows developers to customize and build web applications 
#     according to their specific needs. It doesn't come with any particular project structure or database support, which makes 
#     it flexible and allows developers to use their preferred tools and libraries.
# 
# Easy to learn: Flask is relatively easy to learn and use, especially for developers who are already familiar with Python. 
#     The framework has a simple and intuitive API, and its documentation is clear and concise.
# 
# Modular design: Flask follows a modular design, which means that developers can easily add or remove functionality as needed. 
#     It supports extensions that provide additional features, such as database support, authentication, and testing

# Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in
# Jupyter Notebook.

# In[ ]:





# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()


# ![Hello%20world.png](attachment:Hello%20world.png)

# What is App routing in Flask? Why do we use app routes?

# 
# In Flask, routing refers to the process of mapping a URL endpoint to a specific function in your application. 
# This is done using the @app.route() decorator in your Flask application.
# 
# We use app routes in Flask to create different URL endpoints for our application. This allows users to navigate to different 
# parts of the application and access different functionalities

# Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
# route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999
# Attach the screenshot of the output in Jupyter Notebook.

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_info():
    return 'Company Name: ABC Corporation<br>Location: India<br>Contact Detail: 999-999-9999'

if __name__ == '__main__':
    app.run()


# ![ABC%20company.png](attachment:ABC%20company.png)

# What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
# url_for() function.

# In Flask, the url_for() function is used for URL building. It generates a URL to a specific function within your 
# application based on the endpoint name specified in the @app.route() decorator.

# In[ ]:


from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/get-url')
def get_url():
    url = url_for('hello', name='Alice')
    return f'The URL for hello(Alice) is: {url}'

if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




