#!/usr/bin/env python
# coding: utf-8

# 
# What is data encoding? How is it useful in data science?

# Data encoding is the process of converting data from one form to another, typically to facilitate the storage, processing, or transmission of data. In data science, data encoding is useful in various ways:
# 
# Categorical data encoding: When working with categorical data (e.g., colors, countries, etc.), we need to encode these categories as numerical values in order to use them as input to a machine learning model. This is often done using techniques such as one-hot encoding or label encoding.
# 
# Text encoding: When working with text data, we need to encode the text as numerical values so that we can use it as input to a machine learning model. This is typically done using techniques such as word embedding or bag-of-words encoding.
# 
# Image encoding: When working with image data, we need to encode the pixels in the image as numerical values so that we can use them as input to a machine learning model. This is typically done using techniques such as grayscale or RGB encoding.
# 
# Compression: Data encoding can also be useful in compressing data to reduce storage or transmission costs. This is often done using techniques such as Huffman encoding or Lempel-Ziv-Welch (LZW) encoding.

# What is nominal encoding? Provide an example of how you would use it in a real-world scenario.

# Nominal encoding, also known as one-hot encoding or dummy encoding, is a technique used to represent categorical data as numerical data in machine learning models.
# 
# In nominal encoding, each unique value in the categorical variable is assigned a binary value, where one value represents the presence of the category and zero represents its absence. This allows categorical data to be represented in a way that is compatible with many machine learning algorithms.
# 
# For example, consider a dataset of customer orders at a restaurant, where the "main course" menu item is a categorical variable with three possible values: "burger," "pizza," and "salad." In nominal encoding, each value of the "main course" variable would be represented by a binary feature. The resulting dataset would have three additional columns, one for each possible value of the "main course" variable, where each row would have a one in the column corresponding to the customer's chosen main course and zeros in the other two columns.

# In what situations is nominal encoding preferred over one-hot encoding? Provide a practical example.

# One such situation is when dealing with high-cardinality categorical variables, where the number of unique values in the variable is very large. One-hot encoding a high-cardinality variable can result in a large number of binary features, which can be computationally expensive and may result in overfitting. In these cases, nominal encoding can be a more efficient way of representing the variable as a smaller number of binary features.
# 
# For example, consider a dataset of online retail transactions, where the "product" variable is a categorical variable with a large number of unique values representing individual products. One-hot encoding the "product" variable would result in a very large number of binary features, which may not be feasible for analysis. In this case, nominal encoding could be used to represent the "product" variable as a smaller number of binary features, such as the product category or brand.
# 

# Suppose you have a dataset containing categorical data with 5 unique values. Which encoding
# technique would you use to transform this data into a format suitable for machine learning algorithms?
# Explain why you made this choice.

# The choice of encoding technique for transforming categorical data depends on various factors such as the number of unique values, the nature of the data, and the requirements of the machine learning algorithm.
# 
# If the categorical data contains a small number of unique values (in this case, 5), then nominal encoding could be a suitable choice. Nominal encoding assigns a unique integer value to each category, which can be useful when there is a natural ordering to the categories or when the categories can be represented by a continuous numerical scale. For example, if the categorical data represents different levels of education (e.g., high school, college, graduate school), nominal encoding could be used to represent these levels as 0, 1, and 2, respectively.

# In a machine learning project, you have a dataset with 1000 rows and 5 columns. Two of the columns
# are categorical, and the remaining three columns are numerical. If you were to use nominal encoding to
# transform the categorical data, how many new columns would be created? Show your calculations.

# The number of new columns created in nominal encoding depends on the number of unique values in the categorical columns.
# 
# Suppose the first categorical column has 4 unique values and the second categorical column has 6 unique values.
# 
# For the first column, nominal encoding would create 4 new columns (one for each unique value), and for the second column, it would create 6 new columns.
# 
# Therefore, the total number of new columns created by nominal encoding would be 4 + 6 = 10.
# 
# So the resulting dataset after nominal encoding would have 1000 rows and 10 columns.

# You are working with a dataset containing information about different types of animals, including their
# species, habitat, and diet. Which encoding technique would you use to transform the categorical data into
# a format suitable for machine learning algorithms? Justify your answer.

# The choice of encoding technique for categorical data depends on several factors, including the number of unique values, the type of data, and the specific machine learning algorithm being used.
# 
# In this case, since the dataset contains categorical data with multiple unique values, I would suggest using either one-hot encoding or binary encoding.
# 
# One-hot encoding creates a new binary column for each unique value in a categorical column. This technique is useful when the categorical data has a small number of unique values, and when each value is distinct and has a specific meaning. In this case, the animal species column may have a small number of unique values, making one-hot encoding a suitable choice.
# 
# Binary encoding is similar to one-hot encoding, but it creates fewer columns by encoding the unique values as binary digits. This technique is useful when the categorical data has a larger number of unique values, as it reduces the dimensionality of the data. However, it may not be the best choice if the unique values in the categorical column are not evenly distributed.
# 
# Therefore, depending on the specific nature of the categorical data, I would use either one-hot encoding or binary encoding to transform the categorical data into a format suitable for machine learning algorithms.
# 
# 
# 
# 
# 

# You are working on a project that involves predicting customer churn for a telecommunications
# company. You have a dataset with 5 features, including the customer's gender, age, contract type,
# monthly charges, and tenure. Which encoding technique(s) would you use to transform the categorical
# data into numerical data? Provide a step-by-step explanation of how you would implement the encoding.

# Create a dictionary to map the unique contract types to numerical values:
#     
# {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
# 
# Add a new column to the dataset called "contract_type_encoded" with the numerical values corresponding to each contract type:
#     
# customer_id gender  age     contract_type  monthly_charges  tenure  contract_type_encoded
# 1           Male    43      Two year       79.85            65      2
# 2           Female  23      Month-to-month  49.90            15      0
# 3           Male    56      One year       69.40            59      1
# ...         ...     ...     ...            ...              ...     ...
# 
# Drop the original "contract_type" column from the dataset.
# 
# customer_id gender  age     monthly_charges  tenure  contract_type_encoded
# 1           Male    43      79.85            65      2
# 2           Female  23      49.90            15      0
# 3           Male    56      69.40            59      1
# ...         ...     ...     ...              ...     ...
# 
# 
# Now, the dataset contains only numerical data, and we can use it to train machine learning algorithms.

# 
