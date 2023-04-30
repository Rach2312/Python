#!/usr/bin/env python
# coding: utf-8

# What is the difference between a t-test and a z-test? Provide an example scenario where you would
# use each type of test.

# A z-test is used when the population standard deviation is known, or when the sample size is large (typically above 30) and 
# the population standard deviation is assumed to be the same as the sample standard deviation. In contrast, a t-test is used 
# when the population standard deviation is unknown, and the sample size is small (typically less than 30).
# 
# Here's an example scenario for each test:
# 
# T-Test: Suppose you want to test whether there is a significant difference between the mean heights of two groups of college
#     students, one from a university in the United States and the other from a university in Europe. Since you don't know the
#     population standard deviation, you would use a t-test to compare the means of the two groups.
# 
# Z-Test: Suppose you want to test whether there is a significant difference between the mean scores of two groups of students
# on a standardized test, and you know the population standard deviation. In this case, you could use a z-test to compare the 
# means of the two groups.

# Differentiate between one-tailed and two-tailed tests.

# In statistical hypothesis testing, a one-tailed test (also known as a directional test) is a test of significance that looks 
# for a difference in only one direction between the sample statistic and the population parameter. In contrast, a two-tailed 
# test (also known as a non-directional test) is a test of significance that looks for a difference in either direction between 
# the sample statistic and the population parameter.

# Explain the concept of Type 1 and Type 2 errors in hypothesis testing. Provide an example scenario for
# each type of error.

# Type 1 Error: A Type 1 error occurs when the null hypothesis is rejected when it is actually true. In other words, a Type 1 
#     error occurs when we conclude that there is a significant effect or difference when in reality there is not. The probability
#     of a Type 1 error is denoted by the Greek letter alpha (α) and is typically set at 0.05 or 0.01.
# Example scenario for Type 1 error: Suppose a new drug is being tested for its effectiveness in treating a certain disease. A 
#     Type 1 error would occur if the study concludes that the drug is effective when in fact it is not. This could lead to 
#     patients being prescribed a drug that is not effective, potentially harming their health and wasting resources.
# 
# Type 2 Error: A Type 2 error occurs when the null hypothesis is not rejected when it is actually false. In other words, a Type
#     2 error occurs when we fail to conclude that there is a significant effect or difference when in reality there is one. The
#     probability of a Type 2 error is denoted by the Greek letter beta (β).
# Example scenario for Type 2 error: Suppose a new drug is being tested for its effectiveness in treating a certain disease. A Type 2 error would occur if the study fails to conclude that the drug is effective when in fact it is. This could lead to patients not being prescribed a drug that could be effective, potentially harming their health and wasting resources.

# Explain Bayes's theorem with an example.

# Bayes's theorem is a mathematical formula used to calculate the probability of an event based on prior knowledge or evidence. The formula is named after Reverend Thomas Bayes, an 18th-century statistician and theologian.
# 
# The formula for Bayes's theorem is:
# 
# P(A|B) = P(B|A) * P(A) / P(B)
# 
# where:
# 
# P(A|B) is the probability of event A given that event B has occurred.
# P(B|A) is the probability of event B given that event A has occurred.
# P(A) is the prior probability of event A.
# P(B) is the prior probability of event B.
# An example scenario for Bayes's theorem is as follows:
# 
# a hospital has a new test to detect a certain disease that affects 1% of the population. The test is 95% accurate, meaning that if a person has the disease, there is a 95% chance that the test will detect it. If a person does not have the disease, there is a 5% chance that the test will incorrectly indicate that they do.
# 
# What is the probability that they actually have the disease?
# 
# Using Bayes's theorem, we can calculate this probability as follows:
# 
# Let A be the event that the patient has the disease, and let B be the event that the patient tests positive for the disease.
# 
# P(A) = 0.01 (the prior probability of the disease in the population)
# P(B|A) = 0.95 (the probability of testing positive given that the patient has the disease)
# P(B|~A) = 0.05 (the probability of testing positive given that the patient does not have the disease)
# P(~A) = 0.99 (the prior probability of not having the disease in the population)
# Using these values, we can calculate the probability of the patient having the disease given that they tested positive using Bayes's theorem:
# 
# P(A|B) = P(B|A) * P(A) / [P(B|A) * P(A) + P(B|~A) * P(~A)]
# P(A|B) = 0.95 * 0.01 / (0.95 * 0.01 + 0.05 * 0.99)
# P(A|B) = 0.161
# 
# Therefore, the probability of the patient actually having the disease given that they tested positive is approximately 16.1%. This calculation takes into account both the prior probability of the disease and the accuracy of the test, and can be useful in determining the appropriate course of treatment for the patient.
# 
# 
# 
# 
# 
# 
# 

# What is a confidence interval? How to calculate the confidence interval, explain with an example.

# A confidence interval is a range of values that is likely to contain the true population parameter with a certain level of confidence, typically expressed as a percentage.
# 
# For example, if we want to estimate the average height of all students in a particular school with a 95% confidence interval, we might calculate a range of values that we are 95% confident contains the true average height.
# 
# To calculate a confidence interval, we typically use a point estimate of the population parameter (such as the sample mean or proportion) and a measure of variability (such as the standard deviation or standard error). The formula for a confidence interval depends on the specific type of parameter and the distribution of the sample data.
# 

# Use Bayes' Theorem to calculate the probability of an event occurring given prior knowledge of the
# event's probability and new evidence. Provide a sample problem and solution.

# Suppose a company produces two types of computer chips: type A and type B. Type A chips have a defect rate of 5%, while type B chips have a defect rate of 10%. The company randomly selects a chip from its inventory and tests it. The test is 90% accurate in identifying defective chips.
# 
# If the test indicates that the selected chip is defective, what is the probability that it is a type B chip?
# 
# Let's use Bayes' Theorem to solve this problem. We want to find the probability of the chip being a type B chip given that it has tested defective. Let A denote the event that the selected chip is type B and B denote the event that the chip tests defective. Then, we have:
# 
# P(A) = 0.5 (assuming an equal number of type A and type B chips in inventory)
# P(B|A) = 0.1 (the probability of a defective test result given that the chip is type B)
# P(B|~A) = 0.05 (the probability of a defective test result given that the chip is type A)
# P(~A) = 0.5 (assuming an equal number of type A and type B chips in inventory)
# P(B) = P(B|A) * P(A) + P(B|~A) * P(~A) = 0.1 * 0.5 + 0.05 * 0.5 = 0.075
# Using Bayes' Theorem, we can compute the probability of the chip being type B given a defective test result as follows:
# 
# P(A|B) = P(B|A) * P(A) / P(B)
# P(A|B) = 0.1 * 0.5 / 0.075 = 2/3 = 0.67
# 
# Therefore, the probability that the selected chip is a type B chip given a defective test result is 0.67 or 67%. This means that the test result increases the probability that the chip is a type B chip, but there is still a significant chance that it is a type A chip.
# 
# 
# 
# 
# 
# 
# 

# Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
# of 5. Interpret the results.

# CI = X ± Z * (σ / sqrt(n))
# 
# CI = 50 ± 1.96 * (5 / sqrt(n))
# 
# To find a sample size that will make this interval small enough to be useful, we need to make an assumption about the maximum desired margin of error. For example, if we want the margin of error to be no larger than 1 unit, we can solve for n as follows:
# 
# 1 = 1.96 * (5 / sqrt(n))
# sqrt(n) = 1.96 * 5 / 1
# sqrt(n) = 9.8
# n = 96.04
# 
# Since we need a whole number for the sample size, we can round up to n = 97. Plugging this into the formula above, we get:
# 
# CI = 50 ± 1.96 * (5 / sqrt(97))
# CI = 50 ± 1.08
# 
# Therefore, the 95% confidence interval for the population mean is (48.92, 51.08). This means that if we were to repeat the sampling and estimation process many times, we would expect the true population mean to be within this range in about 95% of the cases.

# What is the margin of error in a confidence interval? How does sample size affect the margin of error?
# Provide an example of a scenario where a larger sample size would result in a smaller margin of error.

# The margin of error is a measure of the precision of an estimate in a confidence interval. It represents the maximum distance between the sample estimate and the true population parameter that we are willing to tolerate, given a certain level of confidence. In other words, it is the range of values above and below the point estimate that is likely to contain the true population parameter.
# 
# The margin of error is calculated as the product of the critical value from the standard normal distribution (or t-distribution, for small samples) and the standard error of the estimate. The standard error is a measure of the variability of the sample estimate and is calculated by dividing the standard deviation of the population (or the sample, if it is used as an estimate) by the square root of the sample size.
# 
# Therefore, sample size has a direct impact on the margin of error. As the sample size increases, the standard error decreases, which in turn leads to a smaller margin of error. This is because a larger sample size provides more information about the population, which reduces the uncertainty in the estimate.
# 
# For example, suppose we want to estimate the average height of students in a university. If we take a random sample of 50 students and calculate the mean height to be 170 cm with a standard deviation of 5 cm, and we want to construct a 95% confidence interval, the margin of error would be:
# 
# Margin of error = 1.96 * (5 / sqrt(50)) = 1.39 cm
# 
# This means that we are 95% confident that the true population mean falls within the range of 168.61 cm to 171.39 cm.
# 
# Now suppose we increase the sample size to 200. The new margin of error would be:
# 
# Margin of error = 1.96 * (5 / sqrt(200)) = 0.99 cm
# 
# As we can see, the margin of error has decreased by almost 30% with the larger sample size. This means that the larger sample size provides a more precise estimate of the population mean.

# Calculate the z-score for a data point with a value of 75, a population mean of 70, and a population
# standard deviation of 5. Interpret the results.

# The z-score, also known as the standard score, is a measure of how many standard deviations a data point is away from the mean of its population. It is calculated using the formula:
# 
# z = (x - μ) / σ
# 
# where x is the data point, μ is the population mean, and σ is the population standard deviation.
# 
# In this case, the data point is x = 75, the population mean is μ = 70, and the population standard deviation is σ = 5. Plugging these values into the formula, we get:
# 
# z = (75 - 70) / 5 = 1
# 
# This means that the data point of 75 is one standard deviation above the mean of the population. In other words, it is higher than 68.27% of the data points in the population, which is the proportion of data points within one standard deviation of the mean in a normal distribution.

# In a study of the effectiveness of a new weight loss drug, a sample of 50 participants lost an average
# of 6 pounds with a standard deviation of 2.5 pounds. Conduct a hypothesis test to determine if the drug is
# significantly effective at a 95% confidence level using a t-test.

# null hypothesis is that the weight loss drug is not significantly effective, or in other words, that the population mean weight loss is not significantly different from 0 pounds. Our alternative hypothesis is that the weight loss drug is significantly effective, or in other words, that the population mean weight loss is significantly less than 0 pounds.
# 
# Ho: µ = 0
# Ha: µ < 0
# 
# t = (x̄ - µ) / (s / sqrt(n))
# 
# where x̄ is the sample mean, µ is the hypothesized population mean under the null hypothesis, s is the sample standard deviation, and n is the sample size.
# 
# 
# t = (6 - 0) / (2.5 / sqrt(50)) = 15.81
# 
# The degrees of freedom for the t-distribution are n-1, or 49 in this case. Using a t-table or a calculator, we find that the critical value for a one-tailed t-test with 49 degrees of freedom and a 95% confidence level is -1.676.
# 
# Since our calculated t-value of 15.81 is greater than the critical value of -1.676, we reject the null hypothesis and conclude that the weight loss drug is significantly effective at a 95% confidence level

# In a survey of 500 people, 65% reported being satisfied with their current job. Calculate the 95%
# confidence interval for the true proportion of people who are satisfied with their job.

# CI = p ± zsqrt((p(1-p))/n)
# 
# where CI is the confidence interval, p is the sample proportion, z is the z-score corresponding to the desired level of confidence, and n is the sample size.
# 
# In this case, the sample proportion is p = 0.65, the sample size is n = 500, and the desired level of confidence is 95%. The z-score corresponding to a 95% confidence level is 1.96.
# 
# Plugging in the values, we get:
# 
# CI = 0.65 ± 1.96sqrt((0.65(1-0.65))/500)
# = 0.65 ± 0.045
# = (0.605, 0.695)
# 
# Therefore, we can say with 95% confidence that the true proportion of people who are satisfied with their job is between 60.5% and 69.5%, based on the survey of 500 people.

# A researcher is testing the effectiveness of two different teaching methods on student performance.
# Sample A has a mean score of 85 with a standard deviation of 6, while sample B has a mean score of 82
# with a standard deviation of 5. Conduct a hypothesis test to determine if the two teaching methods have a
# significant difference in student performance using a t-test with a significance level of 0.01.

# null hypothesis is that there is no significant difference between the two teaching methods in terms of student performance. Our alternative hypothesis is that there is a significant difference between the two teaching methods in terms of student performance.
# 
# Ho: µA - µB = 0
# Ha: µA - µB ≠ 0
# 
# 
# t = (x̄A - x̄B - (µA - µB)) / sqrt((sA^2/nA) + (sB^2/nB))
# 
# where x̄A and x̄B are the sample means, µA and µB are the population means, sA and sB are the sample standard deviations, nA and nB are the sample sizes.
# 
# 
# 
# t = (85 - 82 - 0) / sqrt((6^2/100) + (5^2/100)) = 1.1785
# 
# The degrees of freedom for the t-distribution are calculated using the formula:
# 
# df = ((sA^2/nA + sB^2/nB)^2) / ((sA^2/nA)^2 / (nA - 1) + (sB^2/nB)^2 / (nB - 1))
# 
# df = ((6^2/100 + 5^2/100)^2) / ((6^2/100)^2 / (100 - 1) + (5^2/100)^2 / (100 - 1)) = 197.59
# 
# Using a t-table or a calculator, we find that the critical value for a two-tailed t-test with 197 degrees of freedom and a significance level of 0.01 is ±2.576.
# 
# Since our calculated t-value of 1.1785 is not greater than the critical value of 2.576 or less than -2.576, we fail to reject the null hypothesis and conclude that there is insufficient evidence to support the claim that there is a significant difference between the two teaching methods in terms of student performance at a significance level of 0.01.

# A population has a mean of 60 and a standard deviation of 8. A sample of 50 observations has a mean
# of 65. Calculate the 90% confidence interval for the true population mean.

# CI = x̄ ± z*(σ / sqrt(n))
# 
# where x̄ is the sample mean, σ is the population standard deviation, n is the sample size, z is the z-score corresponding to the desired confidence level (in this case, 90% corresponds to a z-score of 1.645).
# 
# Plugging in the values, we get:
# 
# CI = 65 ± 1.645*(8 / sqrt(50)) = (62.08, 67.92)
# 
# Therefore, we can say with 90% confidence that the true population mean falls within the interval of (62.08, 67.92).

# In a study of the effects of caffeine on reaction time, a sample of 30 participants had an average
# reaction time of 0.25 seconds with a standard deviation of 0.05 seconds. Conduct a hypothesis test to
# determine if the caffeine has a significant effect on reaction time at a 90% confidence level using a t-test.

# Null hypothesis (H0): The true population mean reaction time with caffeine is equal to 0.25 seconds.
# Alternative hypothesis (Ha): The true population mean reaction time with caffeine is not equal to 0.25 seconds.
# We will use a significance level of 0.1 (corresponding to a 90% confidence level).
# 
# The test statistic for a one-sample t-test is calculated as:
# 
# t = (x̄ - μ) / (s / sqrt(n))
# 
# where x̄ is the sample mean, μ is the hypothesized population mean (in this case, 0.25 seconds), s is the sample standard deviation, and n is the sample size.
# 
# Plugging in the values, we get:
# 
# t = (0.25 - 0.25) / (0.05 / sqrt(30)) = 0
# 
# The calculated t-statistic is 0. Since the t-distribution is symmetric around 0, the p-value will be twice the area to the right of the t-statistic. We can look up the p-value using a t-distribution table or calculator with 29 degrees of freedom (df = n - 1).
# 
# Assuming a two-tailed test, the critical t-value at a significance level of 0.1 with 29 degrees of freedom is ±1.699. Since our calculated t-value of 0 falls within the range of -1.699 to +1.699, we cannot reject the null hypothesis.
# 
# Therefore, we do not have enough evidence to conclude that caffeine has a significant effect on reaction time at a 90% confidence level.
# 
# 
# 
# 
# 

# 

# In[ ]:




