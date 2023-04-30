#!/usr/bin/env python
# coding: utf-8

# What is Estimation Statistics? Explain point estimate and interval estimate.

# Estimation statistics is a branch of inferential statistics that involves using sample data to make inferences about the 
# characteristics of a larger population. It involves using statistical techniques to estimate the value of a population 
# parameter based on sample data.
# 
# There are two main types of estimates in estimation statistics: point estimates and interval estimates.
# 
# Point estimate refers to a single numerical value that is calculated from a sample and is used to estimate an unknown 
# population parameter. For example, if we want to estimate the mean salary of a particular profession, we can take a random 
# sample of individuals from that profession and calculate their mean salary. This calculated mean is a point estimate of the
# true population mean salary.
# 
# Interval estimate refers to a range of values that is likely to contain the true population parameter. It takes into account 
# the uncertainty associated with the point estimate. The range is called a confidence interval and is typically expressed as a
# range of values with an associated level of confidence. For example, a 95% confidence interval for the population mean salary 
# of a profession might be expressed as $50,000 to $60,000, which means that we are 95% confident that the true population mean 
# salary lies within this range.

# Write a Python function to estimate the population mean using a sample mean and standard
# deviation.

# In[43]:


import math

def estimate_population_mean(sample_mean, sample_std_dev, sample_size):
    """Estimate the population mean given a sample mean, standard deviation, and sample size"""
    standard_error = sample_std_dev / math.sqrt(sample_size)  
    margin_of_error = 1.96 * standard_error  
    lower_bound = sample_mean - margin_of_error  
    upper_bound = sample_mean + margin_of_error  
    return (lower_bound + upper_bound) / 2  


# What is Hypothesis testing? Why is it used? State the importance of Hypothesis testing.

# Hypothesis testing is a statistical method used to evaluate a hypothesis or claim about a population parameter. The hypothesis
# is formulated as two mutually exclusive statements: the null hypothesis and the alternative hypothesis. The null hypothesis 
#     assumes that there is no significant difference or relationship between two variables, while the alternative hypothesis 
#     assumes that there is a significant difference or relationship between them.
# 
# Hypothesis testing is used to determine whether the null hypothesis should be rejected or not, based on the available evidence
# from a sample of data. This involves calculating a test statistic and comparing it to a critical value or p-value, which is a 
# measure of the probability of obtaining a test statistic as extreme as the one observed, assuming that the null hypothesis is
# true.
# 
# The importance of hypothesis testing lies in its ability to help us make informed decisions based on available data. By 
# testing hypotheses, we can determine whether a particular claim or assumption about a population parameter is supported by 
# the evidence or not. This can be used to guide decision-making in various fields, such as medicine, engineering, economics, 
# and social sciences.

# Create a hypothesis that states whether the average weight of male college students is greater than
# the average weight of female college students.

# A possible hypothesis that states whether the average weight of male college students is greater than the average weight of 
# female college students is:
# 
# Null hypothesis: The average weight of male college students is equal to or less than the average weight of female college 
#     students.
# 
# Alternative hypothesis: The average weight of male college students is greater than the average weight of female college 
#     students.
# 
# This hypothesis can be tested by collecting a random sample of male and female college students, measuring their weights, and 
# comparing the sample means using a statistical test, such as a t-test or a z-test. The result of the test will help us
# determine whether we can reject or fail to reject the null hypothesis, and make conclusions about the population means.

# Write a Python script to conduct a hypothesis test on the difference between two population means,
# given a sample from each population.

# In[44]:


import scipy.stats as stats

alpha = 0.05


sample1 = [1, 2, 3, 4, 5]
sample2 = [3, 4, 5, 6, 7]


mean1 = sum(sample1) / len(sample1)
mean2 = sum(sample2) / len(sample2)
std_dev1 = stats.tstd(sample1)
std_dev2 = stats.tstd(sample2)


pooled_std_dev = ((len(sample1) - 1) * std_dev1**2 + (len(sample2) - 1) * std_dev2**2) / (len(sample1) + len(sample2) - 2)
pooled_std_dev = pooled_std_dev**0.5


test_statistic = (mean1 - mean2) / (pooled_std_dev * (1/len(sample1) + 1/len(sample2)))**0.5


df = len(sample1) + len(sample2) - 2


t_crit = stats.t.ppf(alpha/2, df)


p_value = stats.t.sf(abs(test_statistic), df) * 2


if abs(test_statistic) > t_crit or p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


# What is a null and alternative hypothesis? Give some examples.

# A null hypothesis is a statement that assumes that there is no significant difference or relationship between two variables or
# populations. It is usually denoted by H0. The null hypothesis is the default assumption, and it is assumed to be true unless 
# there is sufficient evidence to reject it. The alternative hypothesis, on the other hand, is a statement that assumes that 
# there is a significant difference or relationship between two variables or populations. It is usually denoted by Ha or H1.
# 
# Here are some examples of null and alternative hypotheses:
# 
# Example 1: A company claims that their new product increases sales.
# Null hypothesis: The new product has no effect on sales.
# 
# Alternative hypothesis: The new product increases sales.
# 
# Example 2: A researcher wants to investigate whether there is a difference in the mean height of male and female students in
#     a college.
# Null hypothesis: The mean height of male and female students in the college is the same.
# 
# Alternative hypothesis: The mean height of male and female students in the college is different.

# Write down the steps involved in hypothesis testing.

# Step 1: State the null hypothesis (H0) and the alternative hypothesis (Ha)
# 
# H0 is the default assumption that there is no significant difference or relationship between two variables or populations.
# Ha is the opposite of H0 and assumes that there is a significant difference or relationship between two variables or populations.
# Step 2: Determine the level of significance (alpha)
# 
# The level of significance (alpha) is the probability of rejecting the null hypothesis when it is actually true. It is typically 
# set at 0.05 or 0.01.
# Step 3: Select an appropriate test statistic and calculate the test statistic
# 
# The choice of test statistic depends on the type of data being analyzed and the hypothesis being tested.
# The test statistic measures the degree of difference or relationship between the sample data and the null hypothesis.
# Step 4: Determine the p-value
# 
# The p-value is the probability of obtaining a test statistic at least as extreme as the one calculated from the sample data,
# assuming that the null hypothesis is true.
# If the p-value is less than or equal to the level of significance (alpha), then reject the null hypothesis.
# Step 5: Interpret the results
# 
# If the null hypothesis is rejected, then there is sufficient evidence to support the alternative hypothesis.
# If the null hypothesis is not rejected, then there is insufficient evidence to support the alternative hypothesis.
# It is important to interpret the results in the context of the problem being studied and to consider the practical significance
# of the findings.
# Step 6: Draw conclusions and make recommendations
# 
# Based on the results of the hypothesis test, draw conclusions about the hypothesis being tested.
# If the alternative hypothesis is supported, make recommendations or take actions based on the findings.

# Define p-value and explain its significance in hypothesis testing.

# The p-value is a statistical measure that represents the probability of obtaining a test statistic at least as extreme as the
# one calculated from the sample data, assuming that the null hypothesis is true. In other words, it measures the strength of 
# evidence against the null hypothesis based on the available data.
# 
# The significance of the p-value in hypothesis testing is that it is used to make a decision about whether to reject or fail to
# reject the null hypothesis. The p-value is compared to the level of significance (alpha) to determine whether the null 
# hypothesis can be rejected.

# Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom
# parameter set to 10.

# In[45]:


import numpy as np
import matplotlib.pyplot as plt


df = 10
x = np.linspace(-4, 4, 1000)
y = stats.t.pdf(x, df)


fig, ax = plt.subplots()
ax.plot(x, y, label=f"t-distribution with df = {df}")
ax.legend()
ax.set_title("Student's t-distribution")
ax.set_xlabel("x")
ax.set_ylabel("PDF")
plt.show()


# Write a Python program to calculate the two-sample t-test for independent samples, given two
# random samples of equal size and a null hypothesis that the population means are equal.

# In[46]:


import numpy as np
from scipy.stats import t

def two_sample_t_test(sample1, sample2, alpha):
    n1 = len(sample1)
    n2 = len(sample2)
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    std1 = np.std(sample1, ddof=1)
    std2 = np.std(sample2, ddof=1)
    se = np.sqrt((std1**2 / n1) + (std2**2 / n2))
    t_stat = (mean1 - mean2) / se
    df = n1 + n2 - 2
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    if p_value < alpha:
        print("Reject null hypothesis. There is a significant difference between the population means.")
    else:
        print("Fail to reject null hypothesis. There is not enough evidence to suggest a significant difference between the population means.")
    return t_stat, p_value


sample1 = [2, 3, 5, 6, 7, 9, 11, 13, 15, 18]
sample2 = [1, 4, 6, 8, 9, 10, 12, 13, 14, 17]
alpha = 0.05
t_stat, p_value = two_sample_t_test(sample1, sample2, alpha)
print("t-statistic:", t_stat)
print("p-value:", p_value)


# What is Student’s t distribution? When to use the t-Distribution.

# 
# Student's t-distribution is a probability distribution that arises when estimating the population mean of a normally 
# distributed population in situations where the sample size is small or the population standard deviation is unknown. The
# t-distribution is similar in shape to the normal distribution, but has heavier tails, which means that it has more probability
# in the tails than the normal distribution.
# 
# The t-distribution is used when:
# 
# The sample size is small (typically less than 30)
# The population standard deviation is unknown
# The population is normally distributed or the sample size is large enough for the Central Limit Theorem to apply.

# What is t-statistic? State the formula for t-statistic.
# 

# The t-statistic is a measure of the difference between the sample mean and the hypothesized population mean in standard error
# units. It tells us how much the sample mean deviates from the hypothesized population mean, taking into account the variability
# of the data.
# 
# The formula for the t-statistic is:
# 
# t = (x̄ - μ) / (s / √n)
# 
# where:
# 
# x̄ is the sample mean
# μ is the hypothesized population mean under the null hypothesis
# s is the sample standard deviation
# n is the sample size

# A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
# sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
# Estimate the population mean revenue with a 95% confidence interval.

# CI = x̄ ± t*(s/√n)
# 
# x̄ = $500
# s = $50
# n = 50
# 
# 
# Plugging in the values, we get:
# 
# CI = $500 ± 2.009*($50/√50)
# 
# Simplifying, we get:
# 
# CI = $500 ± $14.14
# 
# Therefore, the 95% confidence interval for the population mean revenue is ($485.86, $514.14). We can interpret this interval 
# as follows: we are 95% confident that the true population mean revenue falls between $485.86 and $514.14 based on the given 
#     sample data.
# 
# 
# 
# 
# 

# A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a
# clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a
# standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.

# To test the hypothesis that the new drug will decrease blood pressure by 10 mmHg, we can use a one-sample t-test with the following null and alternative hypotheses:
# 
# Null hypothesis (H0): The true population mean decrease in blood pressure is equal to 10 mmHg.
# Alternative hypothesis (Ha): The true population mean decrease in blood pressure is less than 10 mmHg.
# 
# The formula for the t-statistic is:
# 
# t = (x̄ - μ) / (s / √n)
# 
# where:
# 
# x̄ is the sample mean decrease in blood pressure
# μ is the hypothesized population mean decrease in blood pressure under the null hypothesis (i.e., 10 mmHg)
# s is the sample standard deviation
# n is the sample size
# Plugging in the values, we get:
# 
# t = (8 - 10) / (3 / √100) = -2.82
# 
# The critical value of t for a significance level of 0.05 and 99 degrees of freedom is -1.660. Since our calculated t-statistic
# (-2.82) is less than the critical value (-1.660), we reject the null hypothesis.
# 
# Therefore, we have sufficient evidence to conclude that the new drug decreases blood pressure by less than 10 mmHg at a 
# significance level of 0.05.
# 

# An electronics company produces a certain type of product with a mean weight of 5 pounds and a
# standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight
# is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5
# pounds with a significance level of 0.01.

# To test the hypothesis that the true mean weight of the products is less than 5 pounds, we can use a one-sample t-test with the following null and alternative hypotheses:
# 
# Null hypothesis (H0): The true population mean weight of the products is equal to 5 pounds.
# Alternative hypothesis (Ha): The true population mean weight of the products is less than 5 pounds.
# 
# The formula for the t-statistic is:
# 
# t = (x̄ - μ) / (s / √n)
# 
# where:
# 
# x̄ is the sample mean weight
# μ is the hypothesized population mean weight under the null hypothesis (i.e., 5 pounds)
# s is the sample standard deviation
# n is the sample size
# Plugging in the values, we get:
# 
# t = (4.8 - 5) / (0.5 / √25) = -2
# 
# The critical value of t for a significance level of 0.01 and 24 degrees of freedom is -2.492. Since our calculated t-statistic 
# (-2) is greater than the critical value (-2.492), we fail to reject the null hypothesis.
# 
# Therefore, we do not have sufficient evidence to conclude that the true mean weight of the products is less than 5 pounds at a 
# significance level of 0.01.
# 
# 

# Two groups of students are given different study materials to prepare for a test. The first group (n1 =
# 30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean
# score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two
# groups are equal with a significance level of 0.01.

# To test the hypothesis that the population means for the two groups are equal, we can use a two-sample t-test with the following 
# null and alternative hypotheses:
# 
# Null hypothesis (H0): The population mean score for group 1 is equal to the population mean score for group 2.
# Alternative hypothesis (Ha): The population mean score for group 1 is not equal to the population mean score for group 2.
# We can use a significance level of 0.01, which corresponds to a critical value of t with 68 degrees of freedom and a two-tailed
# test.
# 
# The formula for the t-statistic is:
# 
# t = (x̄1 - x̄2) / (sqrt((s1^2 / n1) + (s2^2 / n2)))
# 
# where:
# 
# x̄1 and x̄2 are the sample means for group 1 and group 2, respectively
# s1 and s2 are the sample standard deviations for group 1 and group 2, respectively
# n1 and n2 are the sample sizes for group 1 and group 2, respectively
# Plugging in the values, we get:
# 
# t = (80 - 75) / (sqrt((10^2 / 30) + (8^2 / 40))) = 2.15
# 
# The critical value of t for a significance level of 0.01 and 68 degrees of freedom is ±2.627. Since our calculated t-statistic
# (2.15) is less than the critical value (2.627), we fail to reject the null hypothesis.
# 
# Therefore, we do not have sufficient evidence to conclude that the population means for the two groups are not equal at a 
# significance level of 0.01.
# 
# 
# 
# 
# 
# 

# A marketing company wants to estimate the average number of ads watched by viewers during a TV
# program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard
# deviation of 1.5. Estimate the population mean with a 99% confidence interval.

# To estimate the population mean with a 99% confidence interval, we can use the following formula:
# 
# CI = x̄ ± Zα/2 * (σ/√n)
# 
# Where:
# 
# x̄ = sample mean
# Zα/2 = the critical value of the standard normal distribution at a significance level of α/2 (0.005 in this case, since we 
#  want a 99% confidence interval)
# σ = population standard deviation (unknown)
# n = sample size
# Since we don't know the population standard deviation, we'll use the sample standard deviation as an estimate.
# 
# find the critical value of the standard normal distribution at a significance level of 0.005 (since we want 
#  a 99% confidence interval):

# In[48]:


import scipy.stats as stats

alpha = 0.01  
z_critical = stats.norm.ppf(1 - alpha/2) 
print("z_critical:", z_critical)



import math

sample_mean = 4
sample_std = 1.5
sample_size = 50

margin_of_error = z_critical * (sample_std / math.sqrt(sample_size))
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print(f"The population mean lies in the interval [{lower_bound}, {upper_bound}]")


# In[ ]:




