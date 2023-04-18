#!/usr/bin/env python
# coding: utf-8

# What is a database? Differentiate between SQL and NoSQL databases.

# SQL Databases:
# 
# SQL (Structured Query Language) databases are relational databases that store data in tables with predefined columns and rows.
# They use a schema, which is a predefined structure that specifies the types of data that can be stored in each column of a table.
# SQL databases are best suited for applications that require complex queries and analysis, as they allow for efficient joining 
# of multiple tables and support for advanced SQL functionalities.
# Examples of popular SQL databases include MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and SQLite.
# 
# NoSQL Databases:
# 
# NoSQL (Not Only SQL) databases are non-relational databases that store data in a flexible, unstructured format.
# They do not require a predefined schema, which makes them highly scalable and adaptable to changing data models.
# NoSQL databases are best suited for applications that require high scalability, high availability, and fast data access, 
# such as web and mobile applications, real-time analytics, and IoT devices.
# Examples of popular NoSQL databases include MongoDB, Cassandra, Redis, Couchbase, and Amazon DynamoDB.
# In summary, SQL databases are best suited for applications that require complex queries and analysis, while NoSQL databases 
# are best suited for applications that require high scalability, high availability, and fast data access.
# 
# 

# What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

# DDL (Data Definition Language) is a subset of SQL (Structured Query Language) used to define the structure of a database and 
# its objects, such as tables, views, indexes, and procedures. DDL statements are used to create, modify, and delete database 
# objects. Here are the four most common DDL statements and their purposes:
# 
# CREATE: This statement is used to create a new database object, such as a table, view, index, or procedure
# DROP: This statement is used to delete an existing database object, such as a table, view, index, or procedure.
# ALTER: This statement is used to modify an existing database object, such as a table, view, index, or procedure.
# TRUNCATE: This statement is used to delete all the rows from a table, while keeping the table structure intact. This is 
#     useful when you want to remove all the data from a table but still keep the table for future use

# In[ ]:


CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  phone VARCHAR(20)
);


# In[ ]:


DROP TABLE customers;


# In[ ]:


ALTER TABLE customers
ADD address VARCHAR(200);


# In[ ]:


TRUNCATE TABLE customers;


# What is DML? Explain INSERT, UPDATE, and DELETE with an example.

# DML (Data Manipulation Language) is a subset of SQL (Structured Query Language) used to modify data in a database. DML 
# statements are used to insert, update, and delete data in database tables.
# INSERT: This statement is used to insert new data into a table. For example, to insert a new row of data into a "customers" 
#     table with values for the "name", "email", and "phone" columns, 
# UPDATE: This statement is used to modify existing data in a table. For example, to update the phone number for the customer
#     with an "id" of 1 in the "customers" table,
# DELETE: This statement is used to delete existing data from a table. For example, to delete the row for the customer with an
#     "id" of 2 in the "customers" table, 

# In[ ]:


INSERT INTO customers (name, email, phone)
VALUES ('John Doe', 'johndoe@example.com', '555-1234');


# In[ ]:


UPDATE customers
SET phone = '555-5678'
WHERE id = 1;


# In[ ]:


DELETE FROM customers
WHERE id = 2;


# What is DQL? Explain SELECT with an example.

# DQL stands for Data Query Language, which is a subset of SQL (Structured Query Language) used to retrieve data from a database.
# DQL includes the SELECT statement, which is the most commonly used SQL command for retrieving data from a database.
# 
# The SELECT statement is used to select data from one or more tables in a database.

# In[ ]:


SELECT column1, column2, ...
FROM table1
[WHERE condition];


# Explain Primary Key and Foreign Key.

# Primary Key: A primary key is a column or set of columns in a table that uniquely identifies each row in that table. It is 
#     used to enforce the integrity of the data and ensure that each row in the table is unique. Primary keys are typically 
#     created on columns that are important to the table and are never null. For example, in a table of customers, the primary 
#     key might be the "customer_id" column, which is unique for each customer.
# 
# Foreign Key: A foreign key is a column or set of columns in one table that refers to the primary key of another table. It is 
#     used to establish a relationship between two tables and enforce referential integrity. For example, in a table of orders, 
#     the "customer_id" column might be a foreign key that refers to the "customer_id" column in the table of customers. This 
#     ensures that each order is associated with a valid customer in the customers table

# Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

# In[ ]:


import mysql.connector


cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='localhost', database='your_database')


cursor = cnx.cursor()


query = "SELECT * FROM your_table"
cursor.execute(query)


results = cursor.fetchall()
for row in results:
    print(row)


cursor.close()
cnx.close()


# cursor(): The cursor() method creates a cursor object that can be used to execute SQL statements and fetch results. 
#     This method is called on the database connection object, and it returns a new cursor object.
# 
# execute(): The execute() method is used to execute an SQL statement on the database. It takes a single argument, which is the 
#     SQL statement to execute. The SQL statement can be a parameterized query, which allows you to pass values into the query 
# at runtime. After the statement is executed, you can use methods like fetchone(), fetchall(), or fetchmany() to retrieve the 
# results.

# Give the order of execution of SQL clauses in an SQL query.

# FROM: The FROM clause specifies the table or tables from which to retrieve data.
# 
# JOIN: If the query includes a JOIN clause, it is executed next to join the specified tables.
# 
# WHERE: The WHERE clause is used to filter the rows returned by the query. It is executed after the FROM and JOIN clauses.
# 
# GROUP BY: The GROUP BY clause is used to group the rows returned by the query based on one or more columns. It is executed 
#     after the WHERE clause.
# 
# HAVING: The HAVING clause is used to filter the grouped rows returned by the query. It is executed after the GROUP BY clause.
# 
# SELECT: The SELECT clause is used to specify the columns to include in the query result. It is executed after the HAVING clause.
# 
# DISTINCT: If the query includes a DISTINCT keyword, it is executed next to remove duplicate rows from the result set.
# 
# ORDER BY: The ORDER BY clause is used to sort the rows in the query result. It is executed after all other clauses.
# 
# LIMIT: If the query includes a LIMIT clause, it is executed last to limit the number of rows returned by the query.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




