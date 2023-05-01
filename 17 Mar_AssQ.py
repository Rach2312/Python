#!/usr/bin/env python
# coding: utf-8

# What are missing values in a dataset? Why is it essential to handle missing values? Name some
# algorithms that are not affected by missing values.

# Missing values in a dataset refer to the absence of a particular value in a particular observation or attribute. The reasons for missing values can be varied and may include human error, data corruption, or data collection limitations.
# 
# It is essential to handle missing values in a dataset because they can adversely affect the quality and accuracy of data analysis and modeling. If left unaddressed, missing values can cause biased estimates, reduce statistical power, and lower the generalizability of a model. Therefore, handling missing values is crucial to ensure that the analysis results are reliable and trustworthy.
# 
# Some algorithms that are not affected by missing values include tree-based models such as decision trees, random forests, and gradient boosting machines.

# List down techniques used to handle missing data. Give an example of each with python code.

# Deleting Rows or Columns with Missing Values: One way to handle missing values is to remove the entire row or column that contains missing values. This technique is simple but may result in a loss of valuable information.
# 
# Imputation: Another way to handle missing data is to fill in the missing values with an estimate. The most common methods for imputation are mean, median, or mode imputation.
#     
# Interpolation: Interpolation is another imputation method that fills in missing values using a mathematical function based on the other data points in the series.

# In[ ]:


#Deleting Rows or Columns with Missing Values
import pandas as pd


df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})


df.dropna(axis=0, inplace=True)
print(df)


df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

df.dropna(axis=1, inplace=True)
print(df)


# In[ ]:


#Imputation:

df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

df.fillna(df.mean(), inplace=True)
print(df)


df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

df.fillna(df.median(), inplace=True)
print(df)


df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

df.fillna(df.mode().iloc[0], inplace=True)
print(df)


# In[ ]:


#Interpolation:

df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

df.interpolate(method='linear', axis=0, inplace=True)
print(df)


# 
# Explain the imbalanced data. What will happen if imbalanced data is not handled?

# Imbalanced data refers to a situation where the distribution of classes in a dataset is not equal, i.e., one class has significantly fewer samples than the other class(es). For example, in a binary classification problem, if the positive class has only 10% of the samples, while the negative class has 90% of the samples, the data is imbalanced.
# 
# If imbalanced data is not handled, it can cause several problems in the machine learning model's performance, such as:
# 
# Biased Model: An imbalanced dataset can cause the model to become biased towards the majority class, leading to poor performance on the minority class.
# 
# Low Precision and Recall: The model's low ability to correctly classify the minority class leads to low precision and recall, as the model will tend to predict the majority class more often.
# 
# Overfitting: In an imbalanced dataset, the model may overfit to the majority class and fail to generalize to new data, leading to poor performance on the minority class.

# What are Up-sampling and Down-sampling? Explain with an example when up-sampling and down-
# sampling are required.

# Upsampling is the process of randomly duplicating samples from the minority class to increase its representation in the dataset. This technique helps to ensure that the minority class is given equal weight during the model training.
# 
# Downsampling, on the other hand, is the process of randomly removing samples from the majority class to reduce its representation in the dataset. This technique helps to ensure that the majority class is not over-represented in the dataset, thereby making the model less biased towards it.
# 
# 
# Suppose you have a dataset of credit card transactions where the positive class represents fraudulent transactions, and the negative class represents legitimate transactions. If only 1% of the transactions are fraudulent, while the other 99% are legitimate, the dataset is imbalanced.
# 
# In this case, if you train a machine learning model on the imbalanced dataset, the model may become biased towards the majority class (legitimate transactions) and fail to detect fraudulent transactions correctly. To overcome this, you can either upsample the minority class (fraudulent transactions) or downsample the majority class (legitimate transactions) to balance the dataset.
# 
# For upsampling, you can randomly duplicate the fraudulent transactions to increase their representation in the dataset. For downsampling, you can randomly remove a portion of legitimate transactions to decrease their representation in the dataset.

# What is data Augmentation? Explain SMOTE.

# Data augmentation is a technique used to artificially increase the size of a dataset by creating new, synthetic samples from the existing data. This technique is commonly used in machine learning when the available dataset is small, or the data is imbalanced.
# 
# SMOTE (Synthetic Minority Over-sampling Technique) is a popular data augmentation technique used to address the problem of imbalanced data. The technique involves creating new synthetic samples for the minority class by interpolating between existing samples.
# 
# The SMOTE algorithm works as follows:
# 
# For each sample in the minority class, SMOTE selects k nearest neighbors (k is a user-defined parameter).
# 
# SMOTE creates a new sample by interpolating between the selected sample and one of its k nearest neighbors. The interpolation is done by randomly choosing a point on the line segment connecting the two samples and creating a new sample at that point.
# 
# The new synthetic sample is added to the dataset, increasing the representation of the minority class.
# 
# The SMOTE algorithm helps to balance the class distribution by creating new samples for the minority class, which improves the model's ability to correctly classify the minority class

# What are outliers in a dataset? Why is it essential to handle outliers?

# 
# Outliers are data points in a dataset that deviate significantly from the majority of the data points. These data points can be very high or very low in value, and they are considered to be anomalies that do not follow the expected pattern of the data.
# 
# Handling outliers is essential because they can have a significant impact on the accuracy and performance of a machine learning model. Outliers can cause problems in statistical analysis, leading to biased results and distorted conclusions.

# You are working on a project that requires analyzing customer data. However, you notice that some of
# the data is missing. What are some techniques you can use to handle the missing data in your analysis?

# Dropping missing data: If the percentage of missing data is small, dropping the missing data points can be a simple solution. However, this technique is not recommended if a large proportion of data is missing, as it can lead to loss of information and bias in the results.
# 
# Imputation: Imputation involves filling in the missing data with estimated values. The most common imputation techniques are mean imputation, median imputation, and mode imputation. The choice of imputation technique depends on the nature of the data and the distribution of missing values.
# 
# Hot-deck imputation: Hot-deck imputation involves filling in the missing data with values from another similar dataset. This technique is useful when there is a small proportion of missing data, and the missing values can be easily matched to a similar dataset.
# 
# Regression imputation: Regression imputation involves using regression analysis to estimate the missing data based on the available data. This technique is useful when the missing data is related to other variables in the dataset.
# 
# Multiple imputation: Multiple imputation involves creating several imputed datasets, each with slightly different estimates for the missing data, and then combining the results to obtain a final estimate. This technique is useful when there is a large amount of missing data.

# You are working with a large dataset and find that a small percentage of the data is missing. What are
# some strategies you can use to determine if the missing data is missing at random or if there is a pattern
# to the missing data?

# Descriptive analysis: Descriptive analysis involves examining the distribution of the missing data in the dataset. This can be done by calculating the percentage of missing data for each variable in the dataset and examining the pattern of missingness. For example, if the missing data is concentrated in a particular variable or set of variables, this may suggest that there is a pattern to the missing data.
# 
# Correlation analysis: Correlation analysis involves examining the relationship between the missing data and other variables in the dataset. If the missing data is correlated with other variables in the dataset, this may suggest that there is a pattern to the missing data.
# 
# Imputation analysis: Imputation analysis involves imputing the missing data and examining the impact of the imputed values on the results of the analysis. If the imputed values have a significant impact on the results, this may suggest that there is a pattern to the missing data.
# 
# Missing data tests: There are statistical tests, such as the Little's MCAR test, that can be used to test whether the missing data is missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR). If the missing data is found to be MCAR, this suggests that the missing data is random, and any imputation technique can be used. If the missing data is found to be MAR or MNAR, more advanced imputation techniques may be needed to handle the missing data.

# Suppose you are working on a medical diagnosis project and find that the majority of patients in the
# dataset do not have the condition of interest, while a small percentage do. What are some strategies you
# can use to evaluate the performance of your machine learning model on this imbalanced dataset?

# some strategies to evaluate the performance of the machine learning model on this imbalanced dataset:
# 
# Confusion matrix: A confusion matrix provides a detailed breakdown of the number of true positives, true negatives, false positives, and false negatives predicted by the model. It can be used to calculate various performance metrics, such as precision, recall, and F1 score.
# 
# ROC curve and AUC: The receiver operating characteristic (ROC) curve is a graphical representation of the true positive rate (TPR) against the false positive rate (FPR) at different threshold settings. The area under the curve (AUC) can be used as a single performance metric to compare different machine learning models.
# 
# Precision-Recall curve and AUC: The precision-recall (PR) curve is a graphical representation of the precision against the recall at different threshold settings. The area under the curve (AUC) can be used as a single performance metric to compare different machine learning models.
# 
# Resampling techniques: Resampling techniques, such as oversampling the minority class, undersampling the majority class, or generating synthetic samples using techniques such as SMOTE, can be used to balance the dataset and improve model performance.

# When attempting to estimate customer satisfaction for a project, you discover that the dataset is
# unbalanced, with the bulk of customers reporting being satisfied. What methods can you employ to
# balance the dataset and down-sample the majority class?

# some methods that can be used to downsample the majority class:
# 
# Random undersampling: In this method, a random subset of samples is selected from the majority class and discarded until the desired class balance is achieved. This method is simple and fast, but it can lead to a loss of information.
# 
# Cluster centroids: In this method, the majority class is clustered, and the centroid of each cluster is used as a representative sample. This method retains more information than random undersampling, but it can be computationally expensive.
# 
# NearMiss: This method selects samples from the majority class that are closest to the minority class samples. There are three variations of this method, namely NearMiss-1, NearMiss-2, and NearMiss-3. NearMiss-1 selects samples from the majority class that are closest to the average distance between each minority class sample and its three closest majority class samples. NearMiss-2 selects samples from the majority class that are farthest away from the three closest minority class samples. NearMiss-3 is a hybrid of the first two methods.

# You discover that the dataset is unbalanced with a low percentage of occurrences while working on a
# project that requires you to estimate the occurrence of a rare event. What methods can you employ to
# balance the dataset and up-sample the minority class?

# Random oversampling: In this method, samples from the minority class are randomly duplicated until the desired class balance is achieved. This method is simple and fast, but it can lead to overfitting and the duplication of noise.
# 
# SMOTE: SMOTE stands for Synthetic Minority Over-sampling Technique. It creates synthetic samples of the minority class by selecting two or more similar samples and then generating new samples along the line connecting them in feature space. This method is widely used and can help avoid overfitting.
# 
# ADASYN: ADASYN stands for Adaptive Synthetic Sampling. It generates synthetic samples for the minority class by focusing on the samples that are harder to classify. This method is similar to SMOTE, but it assigns a higher weight to those minority class samples that are more difficult to classify.

# In[ ]:





# In[ ]:


from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
import pandas as pd


X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.9, 0.1], n_informative=3,
                           n_redundant=1, flip_y=0, n_features=20,
                           n_clusters_per_class=1, n_samples=10000,
                           random_state=42)


df = pd.DataFrame(X)
df['target'] = y


majority = df[df['target'] == 0]
minority = df[df['target'] == 1]


smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X, y)


upsampled_df = pd.concat([majority, X_smote], axis=0)


upsampled_df = upsampled_df.sample(frac=1, random_state=42)


# In[ ]:




