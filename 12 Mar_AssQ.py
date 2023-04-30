#!/usr/bin/env python
# coding: utf-8

# Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
# of 5 using Python. Interpret the results.

# In[50]:


from scipy import stats

sample_mean = 50
sample_std_dev = 5
sample_size = 100

confidence_level = 0.95
z_score = stats.norm.ppf((1 + confidence_level) / 2)

lower_bound = sample_mean - z_score * (sample_std_dev / sample_size**0.5)
upper_bound = sample_mean + z_score * (sample_std_dev / sample_size**0.5)

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)


# Conduct a chi-square goodness of fit test to determine if the distribution of colors of M&Ms in a bag
# matches the expected distribution of 20% blue, 20% orange, 20% green, 10% yellow, 10% red, and 20%
# brown. Use Python to perform the test with a significance level of 0.05.

# In[52]:


import numpy as np
from scipy.stats import chisquare


observed = np.array([10, 15, 20, 8, 12, 15])


expected = np.array([0.2, 0.2, 0.2, 0.1, 0.1, 0.2]) * np.sum(observed)


test_stat, p_value = chisquare(observed, expected)


print("Test statistic:", test_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis. The distribution of colors in the bag does not match the expected distribution.")
else:
    print("Fail to reject null hypothesis. The distribution of colors in the bag matches the expected distribution.")


# Interpretation:
# 
# The chi-square goodness of fit test indicates that the observed distribution of colors in the bag does not significantly differ from the expected distribution at a significance level of 0.05. We fail to reject the null hypothesis that the observed distribution matches the expected distribution.

# Use Python to calculate the chi-square statistic and p-value for a contingency table with the following
# data:
# 
# Interpret the results of the test.
# 
# Group A
# 
# Outcome 1 20 
# Outcome 2 10 
# Outcome 3 15 
# Group B
# 
# Outcome 1 15
# Outcome 2  25
# Outcome 3 20

# In[53]:


import numpy as np
from scipy.stats import chi2_contingency


observed = np.array([[20, 10, 15], [15, 25, 20]])


test_stat, p_value, dof, expected = chi2_contingency(observed)


print("Test statistic:", test_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis. There is a significant association between the groups and outcomes.")
else:
    print("Fail to reject null hypothesis. There is no significant association between the groups and outcomes.")


# Interpretation:
# 
# The chi-square test indicates that there is no significant association between the groups and outcomes at a significance level of 0.05. We fail to reject the null hypothesis that the groups and outcomes are independent.

# A study of the prevalence of smoking in a population of 500 individuals found that 60 individuals
# smoked. Use Python to calculate the 95% confidence interval for the true proportion of individuals in the
# population who smoke.

# In[54]:


from statsmodels.stats.proportion import proportion_confint


n = 500


x = 60


ci = proportion_confint(x, n, alpha=0.05, method='normal')


print("95% confidence interval:", ci)


# Calculate the 90% confidence interval for a sample of data with a mean of 75 and a standard deviation
# of 12 using Python. Interpret the results.

# In[55]:


import scipy.stats as stats


mean = 75


std = 12


n = 1000


ci = stats.norm.interval(0.9, loc=mean, scale=std/(n**0.5))


print("90% confidence interval:", ci)


# Use Python to plot the chi-square distribution with 10 degrees of freedom. Label the axes and shade the
# area corresponding to a chi-square statistic of 15.

# In[56]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


df = 10


x = np.linspace(0, 30, 500)


chi2 = stats.chi2(df)

#
pdf = chi2.pdf(x)


plt.plot(x, pdf, label=f"df={df}")


mask = x >= 15
plt.fill_between(x[mask], pdf[mask], alpha=0.5)


plt.xlabel("Chi-square statistic")
plt.ylabel("Probability density")
plt.title("Chi-square distribution")


plt.show()


# A random sample of 1000 people was asked if they preferred Coke or Pepsi. Of the sample, 520
# preferred Coke. Calculate a 99% confidence interval for the true proportion of people in the population who
# prefer Coke.

# In[58]:


#CI = (p - z*sqrt(p*(1-p)/n), p + z*sqrt(p*(1-p)/n))
import scipy.stats as stats
import math


n = 1000


x = 520


p = x/n

z = stats.norm.ppf(0.995)


m = z*math.sqrt(p*(1-p)/n)


CI = (p - m, p + m)

print(f"99% confidence interval: {CI}")


# A researcher hypothesizes that a coin is biased towards tails. They flip the coin 100 times and observe
# 45 tails. Conduct a chi-square goodness of fit test to determine if the observed frequencies match the
# expected frequencies of a fair coin. Use a significance level of 0.05.

# In[60]:


#X^2 = Σ ((O - E)^2 / E)
#df = k - 1
import scipy.stats as stats


obs = [45, 55]


exp = [50, 50]


df = len(obs) - 1


chi2, p = stats.chisquare(obs, f_exp=exp)


crit = stats.chi2.ppf(0.95, df)


if chi2 > crit:
    print("Reject the null hypothesis: The observed frequencies do not match the expected frequencies of a fair coin.")
else:
    print("Fail to reject the null hypothesis: The observed frequencies match the expected frequencies of a fair coin.")
    
print(f"Chi-square test statistic: {chi2}")
print(f"Critical value: {crit}")


# A study was conducted to determine if there is an association between smoking status (smoker or
# non-smoker) and lung cancer diagnosis (yes or no). The results are shown in the contingency table below.
# Conduct a chi-square test for independence to determine if there is a significant association between
# smoking status and lung cancer diagnosis.
# 
# Use a significance level of 0.05.
# 
# Lung Cancer: Yes
# 
# Smoker 60 
# Non-smoker 30 
# 
# Lung Cancer: No
#     
# Smoker  140
# Non-smoker  170
# 

# In[66]:


#Null hypothesis: There is no association between smoking status and lung cancer diagnosis.
#Alternative hypothesis: There is an association between smoking status and lung cancer diagnosis.

import scipy.stats as stats

obs = [[60, 30], [140, 170]]
chi2, pval, dof, expected = stats.chi2_contingency(obs)
print("Chi-square statistic:", chi2)
print("p-value:", pval)


# The p-value is very small (less than 0.05), which means we reject the null hypothesis and conclude that there is a significant association between smoking status and lung cancer diagnosis.

# A study was conducted to determine if the proportion of people who prefer milk chocolate, dark
# chocolate, or white chocolate is different in the U.S. versus the U.K. A random sample of 500 people from
# the U.S. and a random sample of 500 people from the U.K. were surveyed. The results are shown in the
# contingency table below. Conduct a chi-square test for independence to determine if there is a significant
# association between chocolate preference and country of origin.
# 
# Use a significance level of 0.01.
# 
# Milk Chocolate
# 
# U.S. (n=500) 200
# U.K. (n=500) 225
# 
# Dark Chocolate 
# 
# U.S. (n=500) 150 
# U.K. (n=500) 175 
# 
# 
# White Chocolate
# 
# U.S. (n=500) 150
# U.K. (n=500) 100

# In[65]:


#Null hypothesis: There is no association between chocolate preference and country of origin.
#Alternative hypothesis: There is an association between chocolate preference and country of origin.

import scipy.stats as stats

obs = [[200, 225], [150, 175], [150, 100]]
chi2, pval, dof, expected = stats.chi2_contingency(obs)
print("Chi-square statistic:", chi2)
print("p-value:", pval)


# A random sample of 30 people was selected from a population with an unknown mean and standard
# deviation. The sample mean was found to be 72 and the sample standard deviation was found to be 10.
# Conduct a hypothesis test to determine if the population mean is significantly different from 70. Use a
# significance level of 0.05.

# In[64]:


#Null hypothesis: The population mean is equal to 70 (μ = 70)
#Alternative hypothesis: The population mean is not equal to 70 (μ ≠ 70)

import scipy.stats as stats

sample_mean = 72
n = 30
s = 10
pop_mean = 70
alpha = 0.05

t_stat, p_val = stats.ttest_1samp([sample_mean]*n, pop_mean)
p_val = p_val/2 
if p_val < alpha:
    print("Reject null hypothesis. The population mean is significantly different from 70.")
else:
    print("Fail to reject null hypothesis. There is not enough evidence to conclude that the population mean is different from 70.")


# In[ ]:




