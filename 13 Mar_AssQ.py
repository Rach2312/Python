#!/usr/bin/env python
# coding: utf-8

# Explain the assumptions required to use ANOVA and provide examples of violations that could impact
# the validity of the results.

# 
# ANOVA (Analysis of Variance) is a statistical technique used to test for differences in means between two or more groups. ANOVA is based on several assumptions that need to be met in order for the results to be valid. These assumptions are:
# 
# Independence: The observations in each group must be independent of each other. This means that the value of one observation should not affect the value of another observation.
# 
# Normality: The data should be normally distributed within each group. This means that the distribution of scores within each group should be roughly bell-shaped.
# 
# Homogeneity of Variance: The variances of the groups should be equal. This means that the spread of scores within each group should be roughly the same.
# 
# Random Sampling: The groups should be randomly selected from the population.

# What are the three types of ANOVA, and in what situations would each be used?

# One-Way ANOVA: This type of ANOVA is used when there is one independent variable with three or more levels or groups. For example, if a researcher wants to compare the mean scores of three different groups on a single dependent variable, one-way ANOVA would be appropriate.
# 
# Two-Way ANOVA: This type of ANOVA is used when there are two independent variables, and the interaction between these variables is of interest. For example, if a researcher wants to investigate the effects of two different treatments (independent variables) on a dependent variable, two-way ANOVA would be appropriate.
# 
# Three-Way ANOVA: This type of ANOVA is used when there are three independent variables, and the interaction between these variables is of interest. For example, if a researcher wants to investigate the effects of different factors such as gender, age, and education level on a dependent variable, three-way ANOVA would be appropriate.

# What is the partitioning of variance in ANOVA, and why is it important to understand this concept?

# The partitioning of variance in ANOVA refers to the division of the total variance of a dependent variable into separate components that can be attributed to different sources or factors. This partitioning is essential for understanding the relative importance of these sources of variation and determining their contributions to the variation in the dependent variable.
# 
# Understanding the partitioning of variance is important because it helps researchers to identify which factors are most important in explaining the variation in the dependent variable. This information can be used to develop theories about the underlying causes of the observed differences between groups and to guide future research. Moreover, partitioning the variance helps researchers to identify potential confounding variables that may affect the results of the analysis and control for them in subsequent analyses.

# How would you calculate the total sum of squares (SST), explained sum of squares (SSE), and residual
# sum of squares (SSR) in a one-way ANOVA using Python?

# In[69]:


import numpy as np
from scipy.stats import f_oneway


group1 = np.array([1, 2, 3, 4, 5])
group2 = np.array([2, 4, 6, 8, 10])
group3 = np.array([3, 6, 9, 12, 15])


data = np.concatenate([group1, group2, group3])


f_statistic, p_value = f_oneway(group1, group2, group3)


sst = np.sum((data - np.mean(data)) ** 2)


sse = np.sum((np.mean(group1, axis=0) - np.mean(data)) ** 2) +       np.sum((np.mean(group2, axis=0) - np.mean(data)) ** 2) +       np.sum((np.mean(group3, axis=0) - np.mean(data)) ** 2)


ssr = sst - sse


print("SST:", sst)
print("SSE:", sse)
print("SSR:", ssr)
print("F statistic:", f_statistic)
print("p-value:", p_value)


# In a two-way ANOVA, how would you calculate the main effects and interaction effects using Python?

# In[68]:


import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


data = pd.DataFrame({'dependent_variable': [5, 8, 9, 12, 7, 6, 10, 11, 15, 16, 14, 18],
                     'factor_A': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
                     'factor_B': ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y']})


model = ols('dependent_variable ~ factor_A + factor_B + factor_A:factor_B', data=data).fit()


main_effect_A = sm.stats.anova_lm(model, typ=2)['sum_sq']['factor_A']
main_effect_B = sm.stats.anova_lm(model, typ=2)['sum_sq']['factor_B']
interaction_effect = sm.stats.anova_lm(model, typ=2)['sum_sq']['factor_A:factor_B']

print("Main effect of factor A: ", main_effect_A)
print("Main effect of factor B: ", main_effect_B)
print("Interaction effect: ", interaction_effect)


# Suppose you conducted a one-way ANOVA and obtained an F-statistic of 5.23 and a p-value of 0.02.
# What can you conclude about the differences between the groups, and how would you interpret these
# results?

# 
# If you conducted a one-way ANOVA and obtained an F-statistic of 5.23 and a p-value of 0.02, this indicates that there is a significant difference between the groups. Specifically, it means that the variability between the group means is larger than would be expected by chance, and that the difference between at least two of the groups is statistically significant.
# 
# The F-statistic is a ratio of the variability between the groups to the variability within the groups. A high F-statistic and a low p-value indicate that the variability between the groups is significantly greater than the variability within the groups.
# 
# In this case, a p-value of 0.02 indicates that the probability of observing an F-statistic at least as large as 5.23 under the null hypothesis (i.e., that there is no difference between the group means) is only 0.02. Typically, a p-value threshold of 0.05 is used to determine statistical significance, which means that the probability of observing such a large F-statistic by chance is less than 5%. Therefore, we can reject the null hypothesis and conclude that there is a statistically significant difference between the groups.

# In a repeated measures ANOVA, how would you handle missing data, and what are the potential
# consequences of using different methods to handle missing data?

# Handling missing data in a repeated measures ANOVA can be challenging since the repeated nature of the data means that missing values may be correlated with the outcome variable or with other predictor variables. There are several methods for handling missing data, each with its own advantages and disadvantages:
# 
# Complete case analysis: This involves analyzing only the cases that have complete data for all variables of interest. The advantage of this method is that it is simple to implement, and it can produce unbiased estimates if the missing data are missing completely at random (MCAR). However, this method can result in a loss of statistical power and precision if the amount of missing data is large or if the missing data are not MCAR.
# 
# Pairwise deletion: This involves analyzing all available data for each variable separately, ignoring missing data in the other variables. The advantage of this method is that it maximizes the use of available data, but it can also result in a loss of statistical power and precision if the amount of missing data is large or if the missing data are not MCAR.
# 
# Imputation: This involves replacing missing values with estimated values based on the observed data. There are several methods of imputation, including mean imputation, regression imputation, and multiple imputation. The advantage of this method is that it can produce unbiased estimates and increase statistical power and precision. However, the validity of the imputed values depends on the imputation model, and imputation can introduce additional variability into the data.

# What are some common post-hoc tests used after ANOVA, and when would you use each one? Provide
# an example of a situation where a post-hoc test might be necessary.

# Post-hoc tests are used after conducting an ANOVA to determine which specific group means differ significantly from each other. Some common post-hoc tests include:
# 
# Tukey's HSD: This test is used to compare all possible pairs of means and control the family-wise error rate. It is a conservative test that is suitable when the sample sizes are equal and the variances are homogenous.
# 
# Bonferroni correction: This test is used to control the family-wise error rate by adjusting the alpha level for multiple comparisons. It is a conservative test that is suitable when the sample sizes are small and the variances are heterogeneous.
# 
# Scheffe's test: This test is used to control the family-wise error rate by adjusting the alpha level for multiple comparisons. It is a more liberal test that is suitable when the sample sizes are unequal or the variances are heterogeneous.
# 
# Games-Howell test: This test is used when the assumptions of equal variances and normality are violated. It is a more liberal test that does not assume equal variances or sample sizes.
# 
# Dunnett's test: This test is used to compare multiple treatments to a control group. It is a more powerful test than Bonferroni correction and is suitable when there is a clear control group.
# 
# Post-hoc tests may be necessary when a significant F-test is obtained in an ANOVA, indicating that there is a significant difference among the groups, but we do not know which specific groups differ from each other. For example, suppose we conduct an ANOVA on a dataset comparing the effectiveness of three different treatments for reducing blood pressure. If the ANOVA reveals a significant difference among the treatments, we would need to use a post-hoc test to determine which specific treatments differ from each other.
# 
# 

# A researcher wants to compare the mean weight loss of three diets: A, B, and C. They collect data from
# 50 participants who were randomly assigned to one of the diets. Conduct a one-way ANOVA using Python
# to determine if there are any significant differences between the mean weight loss of the three diets.
# Report the F-statistic and p-value, and interpret the results.

# In[70]:


import scipy.stats as stats


weight_loss_A = [3.2, 4.5, 1.2, 2.3, 2.8, 3.9, 4.1, 3.3, 1.8, 2.1, 2.5, 3.7, 4.4, 2.6, 1.7, 2.9, 3.1, 4.8, 3.5, 2.7,
                 3.8, 2.2, 2.9, 1.5, 2.6]
weight_loss_B = [2.5, 1.8, 3.9, 3.3, 2.7, 1.5, 2.2, 2.9, 1.7, 3.5, 3.1, 4.5, 2.8, 3.2, 2.6, 2.1, 1.2, 2.3, 2.6, 1.4,
                 2.4, 3.8, 4.1, 3.7, 4.4]
weight_loss_C = [1.3, 3.5, 2.7, 2.9, 1.2, 2.5, 3.8, 4.5, 2.8, 1.5, 2.1, 1.7, 3.3, 3.1, 4.4, 2.6, 2.2, 3.9, 3.7, 2.3,
                 1.8, 3.2, 2.9, 1.7, 2.6]


f_statistic, p_value = stats.f_oneway(weight_loss_A, weight_loss_B, weight_loss_C)


print("F-Statistic: ", f_statistic)
print("P-Value: ", p_value)


# A company wants to know if there are any significant differences in the average time it takes to
# complete a task using three different software programs: Program A, Program B, and Program C. They
# randomly assign 30 employees to one of the programs and record the time it takes each employee to
# complete the task. Conduct a two-way ANOVA using Python to determine if there are any main effects or
# interaction effects between the software programs and employee experience level (novice vs.
# experienced). Report the F-statistics and p-values, and interpret the results.

# In[81]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

np.random.seed(1234)

n = 30
programs = ['A', 'B', 'C']
exp_levels = ['novice', 'experienced']
data = pd.DataFrame({'program': np.random.choice(programs, n),
                     'exp_level': np.random.choice(exp_levels, n),
                     'time': np.random.normal(10, 2, n)})

model = ols('time ~ C(program) + C(exp_level) + C(program):C(exp_level)', data=data).fit()

print(model.summary())


# An educational researcher is interested in whether a new teaching method improves student test
# scores. They randomly assign 100 students to either the control group (traditional teaching method) or the
# experimental group (new teaching method) and administer a test at the end of the semester. Conduct a
# two-sample t-test using Python to determine if there are any significant differences in test scores
# between the two groups. If the results are significant, follow up with a post-hoc test to determine which
# group(s) differ significantly from each other.

# In[83]:


import numpy as np
from scipy import stats

np.random.seed(1234)

n = 100
control_scores = np.random.normal(70, 10, n)
exp_scores = np.random.normal(75, 10, n)

t_stat, p_value = stats.ttest_ind(control_scores, exp_scores)

if p_value < 0.05:
    print("There is a significant difference between the control and experimental groups (p = {:.3f}).".format(p_value))
else:
    print("There is no significant difference between the control and experimental groups (p = {:.3f}).".format(p_value))

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(np.concatenate([control_scores, exp_scores]), 
                                  np.concatenate([np.repeat('control', n), np.repeat('experimental', n)]), 
                                  alpha=0.05)
print(tukey_results)



# A researcher wants to know if there are any significant differences in the average daily sales of three
# retail stores: Store A, Store B, and Store C. They randomly select 30 days and record the sales for each store
# on those days. Conduct a repeated measures ANOVA using Python to determine if there are any
# 
# significant differences in sales between the three stores. If the results are significant, follow up with a post-
# hoc test to determine which store(s) differ significantly from each other.

# In[85]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

np.random.seed(1234)

n_days = 30
sales_a = np.random.normal(1000, 100, n_days)
sales_b = np.random.normal(1200, 150, n_days)
sales_c = np.random.normal(800, 80, n_days)

df = pd.DataFrame({
    'store': np.repeat(['A', 'B', 'C'], n_days),
    'sales': np.concatenate([sales_a, sales_b, sales_c])
})


model = ols('sales ~ store', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

if anova_table['PR(>F)']['store'] < 0.05:
    print("There is a significant difference in sales between the three stores (p = {:.3f}).".format(anova_table['PR(>F)']['store']))
else:
    print("There is no significant difference in sales between the three stores (p = {:.3f}).".format(anova_table['PR(>F)']['store']))

tukey_results = pairwise_tukeyhsd(df['sales'], df['store'], alpha=0.05)
print(tukey_results)


# In[ ]:




