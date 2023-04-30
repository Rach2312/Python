#!/usr/bin/env python
# coding: utf-8

# What is the Probability density function?

# A probability density function (PDF) is a mathematical function that describes the relative likelihood of observing a 
# particular value or range of values of a random variable in a probability distribution. It is used to calculate the 
# probability of a random variable falling within a particular range of values.

# What are the types of Probability distribution?

# Normal Distribution: Also known as the Gaussian distribution, it is a continuous probability distribution that is often used to 
#     model real-world phenomena such as measurement errors, IQ scores, and physical characteristics such as height and weight.
# 
# Binomial Distribution: A discrete probability distribution that models the number of successes in a fixed number of independent 
#     trials, where each trial has only two possible outcomes (success or failure). It is often used to model the results of 
#     experiments or surveys where the outcomes are binary.
# 
# Poisson Distribution: A discrete probability distribution that models the number of occurrences of a rare event in a fixed 
#     interval of time or space. It is often used to model the number of arrivals in a queue or the number of defects in a
#     manufacturing process.
# 
# Exponential Distribution: A continuous probability distribution that models the time between events in a Poisson process. 
#     It is often used to model the lifetimes of products or the time between failures in a system.
# 
# Uniform Distribution: A continuous probability distribution that assigns equal probability to all values within a specified 
#     range. It is often used to model situations where all outcomes are equally likely, such as rolling a fair die or selecting
#     a random number from a given range.
# 
# Gamma Distribution: A continuous probability distribution that is used to model the time until a specified number of events 
#     occurs in a Poisson process. It is often used in reliability engineering and queueing theory.
# 
# 

# Write a Python function to calculate the probability density function of a normal distribution with
# given mean and standard deviation at a given point.

# In[38]:


import math

def normal_pdf(x, mu, sigma):
    """
    Calculates the probability density function of a normal distribution with
    mean mu and standard deviation sigma at point x.
    """
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))


# What are the properties of Binomial distribution? Give two examples of events where binomial
# distribution can be applied.

# Some of the key properties of the Binomial distribution include:
# 
# The number of trials is fixed and denoted by n.
# Each trial has only two possible outcomes, which are typically labeled as success and failure.
# The probability of success is denoted by p, and the probability of failure is denoted by q = 1 - p.
# The trials are assumed to be independent, meaning that the outcome of one trial does not affect the outcome of any other trial.
# The probability mass function (PMF) of the Binomial distribution gives the probability of observing k successes in n independent trials.
# 
# Two examples of events where the Binomial distribution can be applied are:
# 
# In a medical study, researchers want to know the probability that a new drug will cure a particular disease. They test the 
# drug on a sample of 100 patients, and record whether each patient is cured or not. The Binomial distribution can be used to 
# model the number of cured patients in the sample, with n = 100 and p representing the unknown probability of cure.
# 
# In an election, a candidate wants to know the probability of winning a particular state based on the results of a poll. The
# poll asks a random sample of 500 voters whether they plan to vote for the candidate or not. The Binomial distribution can be 
# used to model the number of voters who plan to vote for the candidate, with n = 500 and p representing the unknown proportion 
# of voters who plan to vote for the candidate.

# Generate a random sample of size 1000 from a binomial distribution with probability of success 0.4
# and plot a histogram of the results using matplotlib.

# In[39]:


import numpy as np
import matplotlib.pyplot as plt


n = 1000  
p = 0.4   
sample = np.random.binomial(n, p, size=1000)


plt.hist(sample, bins=range(n+2), density=True, alpha=0.75)
plt.xlabel('Number of successes')
plt.ylabel('Probability')
plt.title('Histogram of Binomial Distribution')
plt.show()


# Write a Python function to calculate the cumulative distribution function of a Poisson distribution
# with given mean at a given point.

# In[40]:


from scipy.stats import poisson

def poisson_cdf(mean, x):
    """
    Calculates the cumulative distribution function (CDF) of a Poisson
    distribution with a given mean at a given point.
    
    Parameters:
    mean (float): the mean of the Poisson distribution
    x (int): the point at which to evaluate the CDF
    
    Returns:
    float: the probability of observing x or fewer events in a Poisson process with mean lambda
    """
    return poisson.cdf(x, mu=mean)


# In[41]:



result = poisson_cdf(2.5, 3)
print(f"Result: {result:.4f}")


# How Binomial distribution different from Poisson distribution?

# 
# Number of trials: A Binomial distribution is used to model the number of successes in a fixed number of independent trials with
#     a constant probability of success, while a Poisson distribution is used to model the number of events occurring in a fixed
#     interval of time or space.
# 
# Probability of success: In a Binomial distribution, the probability of success is constant across all trials, while in a
#     Poisson distribution, the probability of an event occurring is proportional to the length of the time or space interval.
# 
# Limiting conditions: A Poisson distribution is a limiting case of a Binomial distribution where the number of trials is very 
#     large and the probability of success is very small, but the product of the two (the mean) remains constant.
# 
# Type of events: Binomial distribution is used for discrete events with two possible outcomes (success or failure), while 
#     Poisson distribution is used for counting the number of rare events in a fixed interval.

# Generate a random sample of size 1000 from a Poisson distribution with mean 5 and calculate the
# sample mean and variance.

# In[42]:


import numpy as np


np.random.seed(123)


sample = np.random.poisson(5, size=1000)


sample_mean = np.mean(sample)
sample_variance = np.var(sample, ddof=1)

print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_variance)


# How mean and variance are related in Binomial distribution and Poisson distribution?

# In a Binomial distribution, the mean is equal to the product of the number of trials n and the probability of success p, and 
# the variance is equal to the product of n, p, and 1-p. That is:
# 
# Mean = np
# Variance = np(1-p)
# 
# In a Poisson distribution, the mean is equal to the parameter lambda, and the variance is also equal to lambda. That is:
# 
# Mean = Variance = lambda
# 
# This means that in a Binomial distribution, the variance increases as the probability of success moves away from 0.5 towards 
# either 0 or 1, while in a Poisson distribution, the variance is always equal to the mean.

# In normal distribution with respect to mean position, where does the least frequent data appear?

# In a normal distribution, the least frequent data appears at the tails of the distribution, farthest away from the mean. 
# The normal distribution is a symmetric bell-shaped curve, with the mean located at the center. As you move away from the mean
# towards the tails of the distribution, the frequency of occurrence of data decreases.

# In[ ]:




