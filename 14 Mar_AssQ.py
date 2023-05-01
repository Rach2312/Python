#!/usr/bin/env python
# coding: utf-8

# Write a Python function that takes in two arrays of data and calculates the F-value for a variance ratio
# test. The function should return the F-value and the corresponding p-value for the test.

# In[12]:


import numpy as np
from scipy.stats import f

def variance_ratio_test(x, y):
    n = len(x)
    m = len(y)
    df1 = n - 1
    df2 = m - 1
    var_x = np.var(x, ddof=1)
    var_y = np.var(y, ddof=1)
    f_value = var_x / var_y
    p_value = f.cdf(f_value, df1, df2)
    return f_value, p_value


# Given a significance level of 0.05 and the degrees of freedom for the numerator and denominator of an
# F-distribution, write a Python function that returns the critical F-value for a two-tailed test.

# In[13]:


from scipy.stats import f

def critical_f_value(dfn, dfd, alpha=0.05):
    return f.ppf(alpha/2, dfn, dfd), f.ppf(1-alpha/2, dfn, dfd)


# Write a Python program that generates random samples from two normal distributions with known
# 
# variances and uses an F-test to determine if the variances are equal. The program should output the F-
# value, degrees of freedom, and p-value for the test.

# In[14]:


import numpy as np
from scipy.stats import f


n1, n2 = 30, 30  
mu1, mu2 = 0, 0  
var1, var2 = 1, 2  


x = np.random.normal(mu1, np.sqrt(var1), n1)
y = np.random.normal(mu2, np.sqrt(var2), n2)


f_value = np.var(x, ddof=1) / np.var(y, ddof=1)
dfn = n1 - 1
dfd = n2 - 1
p_value = f.cdf(f_value, dfn, dfd)


print("F-value: {:.2f}".format(f_value))
print("Degrees of freedom: {:d}, {:d}".format(dfn, dfd))
print("p-value: {:.4f}".format(p_value))


# variances of two populations are known to be 10 and 15. A sample of 12 observations is taken from
# each population. Conduct an F-test at the 5% significance level to determine if the variances are
# significantly different.

# The null hypothesis is that the variances are equal:
# 
# H0: σ1^2 = σ2^2
# 
# The alternative hypothesis is that the variances are not equal:
# 
# Ha: σ1^2 ≠ σ2^2
# 
#  level of significance, α = 0.05.
# 
# The F-statistic is calculated as the ratio of the larger sample variance to the smaller sample variance:
# 
# F = s1^2 / s2^2, where s1^2 = 10 and s2^2 = 15.
# 
# F = 15 / 10 = 1.5
# 
# 
# The degrees of freedom for the numerator is the sample size of the population with the larger variance minus one, and the degrees of freedom for the denominator is the sample size of the population with the smaller variance minus one:
# 
# dfn = 11
# dfd = 10
# 
# 
# The p-value is the probability of observing an F-statistic as extreme or more extreme than the one calculated, assuming the null hypothesis is true. We can use the scipy.stats.f.cdf function to calculate the p-value:
# 
# p_value = 2 * (1 - f.cdf(F, dfn, dfd))
# 
# If the p-value is less than the level of significance (i.e., p_value < α), we reject the null hypothesis and conclude that the variances are significantly different. Otherwise, we fail to reject the null hypothesis.
# 
# In this case, using the F-statistic and degrees of freedom calculated in steps 3 and 4, we have:
# 
# p_value = 2 * (1 - f.cdf(1.5, 11, 10)) = 0.252
# 
# Since the p-value (0.252) is greater than the level of significance (0.05), we fail to reject the null hypothesis and conclude that there is not enough evidence to suggest that the variances are significantly different at the 5% level of significance.
# 
# 
# 
# 
# 

# A manufacturer claims that the variance of the diameter of a certain product is 0.005. A sample of 25
# products is taken, and the sample variance is found to be 0.006. Conduct an F-test at the 1% significance
# level to determine if the claim is justified.

# The null hypothesis is that the variance is equal to the claimed value:
# 
# H0: σ^2 = 0.005
# 
# The alternative hypothesis is that the variance is greater than the claimed value:
# 
# Ha: σ^2 > 0.005
# 
# level of significance, α = 0.01.
# 
# 
# The F-statistic is calculated as the ratio of the sample variance to the claimed value:
# 
# F = s^2 / σ^2, where s^2 = 0.006 and σ^2 = 0.005.
# 
# F = 0.006 / 0.005 = 1.2
# 
# The degrees of freedom for the numerator is the sample size minus one, and the degrees of freedom for the denominator is the degrees of freedom associated with the claimed value of the variance, which is the sample size minus one:
# 
# dfn = 24
# dfd = 24
# 
# The p-value is the probability of observing an F-statistic as extreme or more extreme than the one calculated, assuming the null hypothesis is true. We can use the scipy.stats.f.cdf function to calculate the p-value:
# 
# p_value = 1 - f.cdf(F, dfn, dfd)
# 
# If the p-value is less than the level of significance (i.e., p_value < α), we reject the null hypothesis and conclude that the variance is greater than the claimed value. Otherwise, we fail to reject the null hypothesis.
# 
# In this case, using the F-statistic and degrees of freedom calculated in steps 3 and 4, we have:
# 
# p_value = 1 - f.cdf(1.2, 24, 24) = 0.264
# 
# Since the p-value (0.264) is greater than the level of significance (0.01), we fail to reject the null hypothesis and conclude that there is not enough evidence to suggest that the variance is greater than the claimed value at the 1% level of significance. Therefore, the claim that the variance of the diameter of the certain product is 0.005 is justified at the 1% significance level based on the sample data.
# 
# 
# 
# 
# 
# 

# Write a Python function that takes in the degrees of freedom for the numerator and denominator of an
# F-distribution and calculates the mean and variance of the distribution. The function should return the
# mean and variance as a tuple.

# In[15]:


mean = dfd / (dfd - 2)
variance = (2 * dfd ** 2 * (dfn + dfd - 2)) / (dfn * (dfd - 2) ** 2 * (dfd - 4))
def f_distribution_mean_variance(dfn, dfd):
    mean = dfd / (dfd - 2)
    variance = (2 * dfd ** 2 * (dfn + dfd - 2)) / (dfn * (dfd - 2) ** 2 * (dfd - 4))
    return mean, variance


# A random sample of 10 measurements is taken from a normal population with unknown variance. The
# sample variance is found to be 25. Another random sample of 15 measurements is taken from another
# normal population with unknown variance, and the sample variance is found to be 20. Conduct an F-test
# at the 10% significance level to determine if the variances are significantly different.

# In[16]:


from scipy.stats import f


s1_squared = 25
s2_squared = 20


n1 = 10
n2 = 15


dfn = n1 - 1
dfd = n2 - 1


F = s1_squared / s2_squared


p_value = 1 - f.cdf(F, dfn, dfd)


alpha = 0.1


if p_value < alpha:
    print("Reject the null hypothesis. The variances are significantly different.")
else:
    print("Fail to reject the null hypothesis. The variances are not significantly different.")


# The following data represent the waiting times in minutes at two different restaurants on a Saturday
# night: Restaurant A: 24, 25, 28, 23, 22, 20, 27; Restaurant B: 31, 33, 35, 30, 32, 36. Conduct an F-test at the 5%
# significance level to determine if the variances are significantly different.

# In[17]:


import numpy as np


a = np.array([24, 25, 28, 23, 22, 20, 27])


b = np.array([31, 33, 35, 30, 32, 36])


s1_squared = np.var(a, ddof=1)
s2_squared = np.var(b, ddof=1)


n1 = len(a)
n2 = len(b)


dfn = n1 - 1
dfd = n2 - 1


F = s1_squared / s2_squared


from scipy.stats import f
p_value = 1 - f.cdf(F, dfn, dfd)


alpha = 0.05


if p_value < alpha:
    print("Reject the null hypothesis. The variances are significantly different.")
else:
    print("Fail to reject the null hypothesis. The variances are not significantly different.")


# The following data represent the test scores of two groups of students: Group A: 80, 85, 90, 92, 87, 83;
# Group B: 75, 78, 82, 79, 81, 84. Conduct an F-test at the 1% significance level to determine if the variances
# are significantly different.

# In[18]:


import numpy as np


a = np.array([80, 85, 90, 92, 87, 83])


b = np.array([75, 78, 82, 79, 81, 84])


s1_squared = np.var(a, ddof=1)
s2_squared = np.var(b, ddof=1)


n1 = len(a)
n2 = len(b)


dfn = n1 - 1
dfd = n2 - 1


F = s1_squared / s2_squared


from scipy.stats import f
p_value = 1 - f.cdf(F, dfn, dfd)


alpha = 0.01


if p_value < alpha:
    print("Reject the null hypothesis. The variances are significantly different.")
else:
    print("Fail to reject the null hypothesis. The variances are not significantly different.")


# In[ ]:




