#!/usr/bin/env python
# coding: utf-8

# What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use
# MongoDB over SQL databases?

# MongoDB is a popular document-oriented NoSQL database that uses JSON-like documents with optional schemas. It is designed 
# to be highly scalable, flexible, and easily accessible from many different programming languages.
# 
# Scalability is a key requirement: MongoDB is designed to be highly scalable, making it a good choice for applications that 
#     need to handle large volumes of data and traffic.
# 
# Dynamic and changing data model: MongoDB's flexible document-oriented data model makes it easy to work with data that has 
#     variable schema and structure.
# 
# Faster development cycle: MongoDB's flexible data model allows developers to quickly iterate and adapt their applications 
#     as the requirements change.
# 
# Horizontal scaling: MongoDB's sharding capabilities make it easy to scale out across multiple servers, allowing for high 
#     availability and improved performance.

# State and Explain the features of MongoDB.

# MongoDB is a popular NoSQL document-oriented database that offers many features that set it apart from traditional SQL databases. Some of the key features of MongoDB include:
# 
# Document-oriented data model: MongoDB's data model is based on the concept of documents, which are self-contained units of 
#     data that can contain nested sub-documents and arrays. This makes it easy to store and work with complex, hierarchical 
#     data structures.
# 
# Dynamic schema: Unlike traditional SQL databases that use a fixed schema, MongoDB allows for dynamic schemas, meaning that 
#     documents within a collection can have different fields and data types. This allows for greater flexibility and agility 
#     when working with data.
# 
# Rich query language: MongoDB's query language is designed to be expressive and powerful, allowing for complex queries that 
#     can handle data with nested arrays and documents. It includes features such as aggregation, indexing, and full-text search.

# Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

# In[ ]:




import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = client["mydatabase"]


mycol = mydb["customers"]


mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)


print(x.inserted_id)


# Using the database and the collection created in question number 3, write a code to insert one record,
# and insert many records. Use the find() and find_one() methods to print the inserted record.

# In[ ]:



import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = client["mydatabase"]


mycol = mydb["customers"]


mydict = { "name": "Jane", "address": "Main Street 1" }
x = mycol.insert_one(mydict)


mylist = [
  { "name": "Amy", "address": "Apple Street 1" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean Blvd 2" }
]
y = mycol.insert_many(mylist)


print(x.inserted_id)
print(y.inserted_ids)


for x in mycol.find():
    print(x)


x = mycol.find_one({"name": "Jane"})
print(x)


# Explain how you can use the find() method to query the MongoDB database. Write a simple code to
# demonstrate this.

# In MongoDB, the find() method is used to query a collection and retrieve the documents that match a specified set of criteria.
# The find() method returns a cursor object, which can be iterated over to access each matching document.

# In[ ]:



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


result = mycol.find({})


for doc in result:
    print(doc)


# In[ ]:


Explain the sort() method. Give an example to demonstrate sorting in MongoDB.


# In[ ]:



import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = client["mydatabase"]


mycol = mydb["customers"]


mydict = { "name": "Jane", "address": "Main Street 1" }
x = mycol.insert_one(mydict)


mylist = [
  { "name": "Amy", "address": "Apple Street 1" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean Blvd 2" }
]
y = mycol.insert_many(mylist)


print(x.inserted_id)
print(y.inserted_ids)


for x in mycol.find():
    print(x)


x = mycol.find_one({"name": "Jane"})
print(x)


# Explain why delete_one(), delete_many(), and drop() is used.

# delete_one() is used to remove a single document from a collection that matches a given filter. If multiple documents 
# match the filter, only the first matching document will be deleted.
# 
# delete_many() is used to remove all documents from a collection that match a given filter. This method can be used to 
# delete multiple documents at once.
# 
# drop() is used to remove an entire collection from the database. This method is irreversible and permanently deletes all the
# documents in the collection.

# In[ ]:





# In[ ]:




