#!/usr/bin/env python
# coding: utf-8

# What are the three measures of central tendency?

# Mean: It is the arithmetic average of a set of numbers. To calculate the mean, you add up all the numbers in the data set and
#     then divide the sum by the number of values in the set.
# 
# Median: It is the middle value in a sorted list of numbers. To find the median, you need to first arrange the values in the 
#     data set in order from smallest to largest, and then pick the middle value. If the data set has an even number of values,
#     then the median is the average of the two middle values.
# 
# Mode: It is the value that occurs most frequently in a set of data. If there are multiple values that occur with the same 
#     highest frequency, then the set is said to be bimodal, trimodal, etc.

# What is the difference between the mean, median, and mode? How are they used to measure the
# central tendency of a dataset?

# The mean is calculated by adding up all the values in a dataset and then dividing by the number of values. It represents the
# average value of the dataset. The mean is affected by outliers or extreme values in the dataset and can be biased if the 
# distribution of the data is skewed.
# 
# The median is the middle value in a dataset when the values are arranged in order from lowest to highest. It represents the 
# value that divides the dataset into two equal parts, with half of the values being greater than the median and half being less 
# than the median. The median is not affected by outliers and is a better measure of central tendency for datasets with skewed 
# distributions.
# 
# The mode is the value that occurs most frequently in a dataset. It represents the most common value or values in the dataset.
# The mode is useful for identifying the typical value of a dataset, especially when dealing with categorical data or discrete 
# values.
# 
# All three measures can be used to summarize the central tendency of a dataset, but the appropriate measure to use depends 
# on the nature of the data and the research question being addressed. In general, the mean is used for datasets with a normal 
# distribution, while the median is used for datasets with skewed distributions, and the mode is used for datasets with 
# categorical or discrete values.

# Measure the three measures of central tendency for the given height data:
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# Mean = (178+177+176+177+178.2+178+175+179+180+175+178.9+176.2+177+172.5+178+176.5)/16
# Mean = 176.96
# 
# Therefore, the mean height of the given data set is approximately 176.96 cm.
# 
# Median:
# 
# Sorted Data: [172.5, 175, 175, 176, 176.2, 176.5, 177, 177, 178, 178, 178, 178.2, 178.9, 179, 180]
# 
# Median = (176 + 176.5)/2
# Median = 176.25
# 
# Therefore, the median height of the given data set is approximately 176.25 cm.
# 
# Mode:
# 
# Mode = 178

# Find the standard deviation for the given data:
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# Standard DEviation Formula:
#     Standard deviation = sqrt(sum((x - mean)^2) / (n - 1))
# 
# Mean is: 
#     μ = (178+177+176+177+178.2+178+175+179+180+175+178.9+176.2+177+172.5+178+176.5)/16
#     μ = 176.96
# 
#  Sum of squares of deviations from the mean:
#     
# sum((x - mean)^2) = (178-176.96)^2 + (177-176.96)^2 + (176-176.96)^2 + (177-176.96)^2 + (178.2-176.96)^2 + (178-176.96)^2 + 
#                     (175-176.96)^2 + (179-176.96)^2 + (180-176.96)^2 + (175-176.96)^2 + (178.9-176.96)^2 + (176.2-176.96)^2 + 
#                     (177-176.96)^2 + (172.5-176.96)^2 + (178-176.96)^2 + (176.5-176.96)^2
# 
# sum((x - mean)^2) = 667.0066
# 
# Variance:
#     s^2 = sum((x - mean)^2) / (n - 1)
#     s^2 = 667.0066 / 15
#     s^2 = 44.4668
# 
# Standard Deviation:
#     
#     s = sqrt(s^2)
#     s = sqrt(44.4668)
#     s = 6.669
# 
# Therefore, the standard deviation of the given data set is approximately 6.669 cm.

# How are measures of dispersion such as range, variance, and standard deviation used to describe
# the spread of a dataset? Provide an example.

# Range: The range is the difference between the maximum and minimum values in a dataset. It gives a rough idea of how much the
#     data is spread out. A larger range indicates greater variability, while a smaller range indicates less variability. For 
#     example, if we have a dataset of the heights of 10 people and the range is 30 cm, this means that the difference between 
#     the tallest and shortest person in the dataset is 30 cm.
# 
# Variance: The variance is the average of the squared differences from the mean of the dataset. It measures how far each data 
#     point is from the mean. A higher variance indicates that the data is more spread out, while a lower variance indicates that 
#     the data is tightly clustered around the mean. For example, if we have a dataset of the weights of 10 people and the 
#     variance is 25 kg^2, this means that the data points are spread out and are on average 25 kg^2 away from the mean weight.
# 
# Standard deviation: The standard deviation is the square root of the variance. It is a commonly used measure of dispersion 
#     that gives an idea of how much the individual data points deviate from the mean. A higher standard deviation indicates 
#     that the data is more spread out, while a lower standard deviation indicates that the data is tightly clustered around 
#     the mean. For example, if we have a dataset of the ages of 10 people and the standard deviation is 5 years, this means
#     that the data points are on average 5 years away from the mean age.

# What is a Venn diagram?

# A Venn diagram is a graphical representation of sets, which shows all possible logical relations between a finite 
# collection of different sets. It consists of overlapping circles or other shapes, with each circle representing a set 
# and the overlap representing the intersection between the sets. The regions inside the circles represent the elements of 
# each set, and the regions outside the circles represent the elements that do not belong to any of the sets.

# For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
# (i) A B
# (ii) A ⋃ B

# (i) A B represents the set of elements that are in A or B, but not in both A and B. To find A B, we need to list the elements
# that are in A or B, but not in both:
# 
# A B = {0, 3, 4, 5, 7, 8, 10}
# 
# (ii) A ⋃ B represents the set of elements that are in either A or B, or in both. To find A ⋃ B, we need to list all the 
# elements that are in A, in B, or in both:
# 
# A ⋃ B = {0, 2, 3, 4, 5, 6, 7, 8, 10}

# What do you understand about skewness in data?

# Skewness is a measure of the asymmetry of a probability distribution or dataset. It indicates whether the data is skewed to 
# one side or the other relative to the mean of the data. A perfectly symmetric distribution has zero skewness.
# 
# If a distribution is skewed to the right, it means that the tail of the distribution is longer on the right-hand side and the
# mode and median are less than the mean. In other words, there are more low values in the dataset than high values. Conversely, 
# if a distribution is skewed to the left, it means that the tail of the distribution is longer on the left-hand side and the 
# mode and median are greater than the mean. In this case, there are more high values in the dataset than low values.

# If a data is right skewed then what will be the position of median with respect to mean?

# If a dataset is right-skewed, the median will be less than the mean. This is because the mean is sensitive to extreme values
# on the right side of the distribution, which pull the mean towards the right.

# Explain the difference between covariance and correlation. How are these measures used in
# statistical analysis?

# Covariance measures the extent to which two variables vary together. It is a measure of the direction of the linear 
# relationship between the two variables, as well as the magnitude of the relationship. A positive covariance indicates that 
# the two variables tend to increase or decrease together, while a negative covariance indicates that one variable tends to 
# increase when the other decreases.
# 
# Correlation, on the other hand, is a standardized measure of the relationship between two variables. It is a dimensionless
# measure that ranges between -1 and 1, where a correlation of +1 indicates a perfect positive linear relationship, a correlation
# of -1 indicates a perfect negative linear relationship, and a correlation of 0 indicates no linear relationship.
# 
# Both covariance and correlation are used in statistical analysis to measure the relationship between two variables. They are particularly useful in exploratory data analysis to identify patterns and relationships in data, as well as in predictive modeling to determine the most important variables to include in a model.
# 

# What is the formula for calculating the sample mean? Provide an example calculation for a
# dataset.

# The formula for calculating the sample mean (x̄) is:
# 
# x̄ = (sum of all values in the sample) / (number of values in the sample)
# 
# For example, let's say we have the following dataset of 5 values:
# 
# 4, 6, 8, 10, 12
# 
# To calculate the sample mean, we add up all the values in the dataset:
# 
# 4 + 6 + 8 + 10 + 12 = 40
# 
# Then, we divide the sum by the number of values in the dataset, which is 5:
# 
# x̄ = 40 / 5 = 8
# 
# Therefore, the sample mean for this dataset is 8.

# For a normal distribution data what is the relationship between its measure of central tendency?
# 

# For a normal distribution, the mean, median, and mode are all equal to each other. This is because a normal distribution is
# symmetric, with half of the values falling to the left of the mean and half falling to the right. Therefore, the median, which
# is the value in the middle of the distribution, will be the same as the mean. Additionally, the mode, which is the most common
# value in the distribution, will also be equal to the mean and median, since the distribution is unimodal and symmetric.
# 
# This relationship between the three measures of central tendency in a normal distribution makes it easier to describe the 
# distribution and make predictions based on it. For example, if we know the mean of a normally distributed dataset, we can use 
# the symmetry of the distribution to estimate the median and mode as well.

# How is covariance different from correlation?

# Covariance measures the extent to which two variables vary together. It is a measure of the direction of the linear relationship
# between the two variables, as well as the magnitude of the relationship. A positive covariance indicates that the two variables 
# tend to increase or decrease together, while a negative covariance indicates that one variable tends to increase when the other
# decreases. However, the value of covariance is dependent on the units of measurement of the two variables, making it difficult 
# to compare covariances across different datasets or different units of measurement.
# 
# Correlation, on the other hand, is a standardized measure of the relationship between two variables. It is a dimensionless 
# measure that ranges between -1 and 1, where a correlation of +1 indicates a perfect positive linear relationship, a correlation
# of -1 indicates a perfect negative linear relationship, and a correlation of 0 indicates no linear relationship. Unlike 
# covariance, correlation is unitless and easier to interpret, allowing for more meaningful comparisons of the strength and 
# direction of relationships between different datasets or different units of measurement.

# How do outliers affect measures of central tendency and dispersion? Provide an example.

# Outliers can have a significant impact on measures of central tendency and dispersion, especially on the mean and standard 
# deviation. This is because these measures are sensitive to extreme values that are far from the rest of the data.
# 
# For example, let's say we have a dataset of salaries for a company's employees:
# 
# [50, 60, 70, 80, 90, 100, 500]
# 
# In this dataset, the majority of the salaries are between 50 and 100, but there is one extreme value of 500 that is much 
# larger than the rest. If we calculate the mean salary for this dataset, we get:
# 
# mean = (50 + 60 + 70 + 80 + 90 + 100 + 500) / 7 = 112.9
# 
# Here, the mean salary is heavily influenced by the outlier value of 500, which is much higher than the rest of the salaries. 
# This can give an inaccurate representation of the "typical" salary for this company.

# In[ ]:




