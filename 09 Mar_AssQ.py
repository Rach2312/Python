#!/usr/bin/env python
# coding: utf-8

# What are the Probability Mass Function (PMF) and Probability Density Function (PDF)? Explain with
# an example.

# PMF is used for discrete random variables, which take a finite or countably infinite set of possible values. It gives the 
# probability of the random variable taking on each of its possible values.
# 
# For example, consider a six-sided die. The PMF of this discrete random variable would be the probability of getting each of 
# the six possible values (1, 2, 3, 4, 5, or 6). If each outcome is equally likely, then the PMF would be a uniform distribution, 
# where the probability of each value is 1/6.
# 
# PDF is used for continuous random variables, which take on an uncountably infinite set of possible values. It gives the 
# probability of the random variable being within a certain range of values, rather than taking on a specific value.
# 
# For example, consider the height of adult humans. The PDF of this continuous random variable would describe the probability 
# of a randomly selected adult human having a height within a certain range (e.g., between 5 feet 10 inches and 6 feet tall). 
# The PDF for human height is typically a normal distribution, where the peak of the curve represents the most common height 
# and the tails of the distribution represent the less common heights.

# What is Cumulative Density Function (CDF)? Explain with an example. Why CDF is used?

# Cumulative Density Function (CDF) is a function that describes the probability that a random variable takes on a value less 
# than or equal to a given value. It is used for both discrete and continuous random variables.
# 
# For discrete random variables, the CDF is the sum of the probabilities of all the possible outcomes less than or equal to a 
# given value. For continuous random variables, the CDF is the area under the probability density curve up to a given value.
# 
# For example, let's consider a fair six-sided die. The CDF for this discrete random variable can be calculated as follows:
# 
# P(X ≤ 1) = 1/6
# P(X ≤ 2) = 2/6
# P(X ≤ 3) = 3/6
# P(X ≤ 4) = 4/6
# P(X ≤ 5) = 5/6
# P(X ≤ 6) = 6/6 = 1
# The resulting CDF would be a step function, increasing by 1/6 at each value of X.
# 
# CDF is used to determine the likelihood of a random variable taking on a value less than or equal to a given value. It is
# useful for finding percentiles and probabilities associated with a certain range of values. For example, if the CDF of a 
# normal distribution tells us that the probability of a value less than or equal to 2 is 0.9772, we know that 97.72% of the 
# values in the distribution are less than or equal to 2.

# What are some examples of situations where the normal distribution might be used as a model?
# Explain how the parameters of the normal distribution relate to the shape of the distribution.

# The normal distribution is a very common probability distribution that can be used to model a wide variety of real-world
# phenomena. Some examples of situations where the normal distribution might be used as a model include:
# 
# Heights and weights of individuals in a population
# IQ scores
# Test scores and grades
# Blood pressure and other physiological measurements
# Economic data such as stock prices and returns
# Errors in measurements and experimental data
# The normal distribution is characterized by two parameters: the mean (μ) and the standard deviation (σ). The mean 
#     represents the central tendency of the distribution and the standard deviation represents the spread of the distribution.
# 
# The mean determines the location of the peak of the bell-shaped curve. If the mean is larger, the peak will be shifted to
# the right, and if the mean is smaller, the peak will be shifted to the left.
# 
# The standard deviation determines the width of the curve. If the standard deviation is larger, the curve will be flatter and 
# more spread out, and if the standard deviation is smaller, the curve will be narrower and more peaked.
# 

# Explain the importance of Normal Distribution. Give a few real-life examples of Normal
# Distribution.

# The importance of normal distribution lies in its key properties, including:
# 
# Symmetry: Normal distribution is symmetric around the mean, which means that the probability of observing values above the
#     mean is the same as the probability of observing values below the mean.
# 
# Central Limit Theorem: Normal distribution arises as the limit of the sum of independent, identically distributed random 
#     variables. This means that even if the individual data points are not normally distributed, their sum tends to be normally 
#     distributed as the sample size increases, making normal distribution a powerful tool in statistical inference.
# 
# Ease of computation: Normal distribution has a simple mathematical formula and many statistical tools and methods are based on
#     the assumption of normality, making it easy to perform calculations and analyze data.
# 
# Some real-life examples of normal distribution include:
# 
# Height: The distribution of human height in a population tends to follow a normal distribution with a mean around 5'7" and a 
#     standard deviation of 2-3 inches.
# 
# Test Scores: Standardized test scores such as the SAT and ACT are designed to follow a normal distribution with a mean of 
#     around 500-600 and a standard deviation of around 100.
# 
# Body Mass Index (BMI): The distribution of BMI scores in a population tends to follow a normal distribution with a mean around 
#     25 and a standard deviation of around 3-5.

# What is Bernaulli Distribution? Give an Example. What is the difference between Bernoulli
# Distribution and Binomial Distribution?

# The Bernoulli distribution is a probability distribution that describes the outcomes of a single binary experiment or trial. 
# The experiment can result in only two possible outcomes, typically labeled as success (S) and failure (F). The Bernoulli 
# distribution is named after the Swiss mathematician Jacob Bernoulli.
# 
# The Bernoulli distribution has a single parameter p, which represents the probability of success. The probability mass 
# function (PMF) of the Bernoulli distribution is given by:
# 
# P(X=x) = p^x * (1-p)^(1-x)
# 
# where X is the random variable representing the outcome of the experiment, and x can take on the values 0 or 1.
# 
# An example of the Bernoulli distribution is flipping a coin. Let's say we define success as getting heads and failure as 
# getting tails. If the coin is fair, the probability of success is 0.5. Thus, the probability of getting heads (success) on a 
# single coin flip is given by the Bernoulli distribution with p=0.5.
# 
# The main difference between the Bernoulli distribution and the binomial distribution is that the Bernoulli distribution 
# describes the outcome of a single trial, while the binomial distribution describes the outcome of a sequence of n independent 
# Bernoulli trials. In other words, the Bernoulli distribution is a special case of the binomial distribution with n=1.
# 
# The binomial distribution has two parameters, n and p, where n represents the number of independent Bernoulli trials and p 
# represents the probability of success in each trial. The probability mass function of the binomial distribution is given by:
# 
# P(X=x) = (n choose x) * p^x * (1-p)^(n-x)
# 
# where X is the random variable representing the number of successes in n trials, and x can take on integer values from 0 to n.
# 
# An example of the binomial distribution is the number of heads obtained in flipping a coin n times. If we flip a fair coin 10
# times, the number of heads obtained follows a binomial distribution with n=10 and p=0.5.

# Consider a dataset with a mean of 50 and a standard deviation of 10. If we assume that the dataset
# is normally distributed, what is the probability that a randomly selected observation will be greater
# than 60? Use the appropriate formula and show your calculations.
# 

# To calculate the probability that a randomly selected observation from a normally distributed dataset with mean 50 and
# standard deviation 10 will be greater than 60, we can use the standard normal distribution formula:
# 
# Z = (X - μ) / σ
# 
# where X is the observed value, μ is the mean, σ is the standard deviation, and Z is the standard normal score.
# 
# In this case, we want to find the probability of X > 60. We can standardize this value by subtracting the mean and dividing 
# by the standard deviation:
# 
# Z = (60 - 50) / 10 = 1
# 
# Next, we use a standard normal distribution table or calculator to find the probability of Z > 1. This probability is 
# approximately 0.1587.
# 
# Therefore, the probability that a randomly selected observation from this normally distributed dataset will be greater than 
# 60 is approximately 0.1587 or 15.87%.

# Explain uniform Distribution with an example.

# 
# The uniform distribution is a continuous probability distribution that is used to model random variables where all values 
# within a certain range are equally likely to occur. This means that the probability density function of a uniform distribution
# is constant between a lower and an upper bound, and zero outside that range.
# 
# For example, consider the height of a randomly selected person in a certain population. If we assume that the heights are 
# uniformly distributed between 5 and 7 feet, then any height between 5 and 7 feet is equally likely to be selected. The 
# probability density function of this uniform distribution would be:
# 
# f(x) = 1/2, for 5 ≤ x ≤ 7
# 
# f(x) = 0, otherwise
# 
# where f(x) is the probability density function of the uniform distribution and x is the height of a randomly selected person.
# 
# This means that the probability of selecting a person with a height between 5 and 6 feet is the same as the probability of 
# selecting a person with a height between 6 and 7 feet. 
# The probability of selecting a person with a height outside this range is zero.

# What is the z score? State the importance of the z score.

# The z-score, also known as the standard score, is a dimensionless value that represents the number of standard deviations that 
# a data point is above or below the mean of a distribution. It is calculated by subtracting the mean from the data point and 
# then dividing the difference by the standard deviation of the distribution. The resulting z-score tells us how many standard 
# deviations away from the mean a particular data point is.
# 
# The z-score is important because it provides a standardized way to compare data points from different distributions. By
# converting data points to z-scores, we can compare them to each other in terms of their relative positions within their
# respective distributions, regardless of the scale or units of measurement of the original data.

# What is Central Limit Theorem? State the significance of the Central Limit Theorem.

# 
# The Central Limit Theorem is a fundamental concept in statistics that states that, under certain conditions, the sampling 
# distribution of the sample means (or sample sums) from a population with any distribution approaches a normal distribution as
# the sample size increases. This means that even if the underlying population is not normally distributed, the distribution of 
# the sample means will become approximately normal if the sample size is large enough.
# 
# The Central Limit Theorem is significant because it allows us to make statistical inferences about a population based on a
# sample, even if we do not know the exact distribution of the population. It provides a way to estimate the parameters of the 
# population, such as the mean and standard deviation, by using the properties of the normal distribution. It also allows us to
# calculate confidence intervals and perform hypothesis testing based on the sample means, which can be used to make predictions
# and decisions in a variety of fields, including finance, economics, engineering, and social sciences.

# State the assumptions of the Central Limit Theorem.

# The Central Limit Theorem (CLT) makes several assumptions, including:
# 
# Random Sampling: The samples are randomly selected from the population.
# 
# Sample Size: The sample size is sufficiently large. A general rule of thumb is that the sample size should be greater than or 
#     equal to 30. However, for certain non-normal populations, a larger sample size may be necessary.
# 
# Independence: The samples are independent of each other. In other words, the value of one sample does not influence the value 
#     of another sample.
# 
# Finite Variance: The population has a finite variance. If the population has an infinite variance, then the CLT may not hold.
# 
# Identical Distribution: Each sample is drawn from the same population distribution.

# In[ ]:




