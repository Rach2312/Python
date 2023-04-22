#!/usr/bin/env python
# coding: utf-8

# Explain GET and POST methods.

# GET Method:
# The GET method requests data from a specified resource, usually a URL (Uniform Resource Locator). The parameters of the 
# request are appended to the URL in the form of a query string. The query string is a series of key-value pairs separated 
# by an ampersand (&) and starts with a question mark (?). The GET method is considered safe and idempotent, which means it 
# can be repeated without changing the result. It is typically used to retrieve information, like fetching a webpage or 
# retrieving search results.
# 
# POST Method:
# The POST method submits an entity to the specified resource, usually a URL. The parameters of the request are sent in 
# the request body, rather than in the URL. The POST method is not considered safe or idempotent since it may change the 
# state of the resource on the server. It is typically used to send data, like submitting a form or uploading a file.

# Why is request used in Flask?

# Request is a built-in object in Flask, which represents an incoming HTTP request that is made by a client to a Flask web 
# application. The Flask request object contains all the data associated with the request, such as the headers, form data, 
# cookies, and query parameters.
# 
# The request object is an essential component of a Flask application, as it allows the application to process the client's 
# request and return the appropriate response. By accessing the data stored in the request object, Flask applications can 
# provide customized responses based on the client's request.

# Why is redirect() used in Flask?

# The redirect() function in Flask is used to redirect a client to a different URL. It is a built-in Flask function that 
# returns a response object with a 302 status code (Found), which tells the client to redirect to the specified URL.
# 
# The redirect() function is typically used in web applications when a user needs to be redirected to a different page or 
# URL after performing some action or when accessing a particular endpoint. For example, after a user logs into a web 
# application, they might be redirected to a dashboard page that displays their account information. Another example 
# is when a user tries to access a protected page without being logged in, they might be redirected to a login page.

# What are templates in Flask? Why is the render_template() function used?

# A template is essentially an HTML file with placeholders for dynamic data that will be filled in by the Flask application. 
# The placeholders are typically written using a template language, such as Jinja2, which is the default template engine used 
# by Flask.
# 
# The render_template() function in Flask is used to render a template with the dynamic data provided by the Flask application. 
# This function takes the name of the template file as its first argument and any additional keyword arguments that represent 
# the dynamic data to be rendered.

# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return 'Hello, World!'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




