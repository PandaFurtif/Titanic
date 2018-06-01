# DATA EXPLORATORY

# Data analysis libraries
import numpy as np
import pandas as pd
#visualization libraries
import matplotlib as plt
import seaborn as sns

#ignore warnings
import warnings
warnings.filterwarnings('ignore')

"""Ctrl + K :      COMMIT
Ctrl + Maj + K :   PUSH
Machine learning program
Kaggle: titanic machine learning from disaster
By James-Martin TA"""

# Load the data
train = pd.read_csv('files/train.csv')
test = pd.read_csv('files/test.csv')

print(' Training Data:')
# len() gives the length of whatever is the input. We can filter the values we want with a condition.
print("Number of passengers:", len(train))
print("Number of survivors:", len(train[train['Survived'] == 1]))
print('-------------------')

"""
# Sample of data
print('Sample of data:')
print(train.sample(5))
print('-------------------')
"""

"""print(' Survivors related to sex:')
print('% of men who survived', 100*np.mean(pd_train['Survived'][pd_train['Sex'] == 'male'])) #Print 100x average of the "survived" colomn WHERE sex = "male"
print('% of women who survived', 100*np.mean(pd_train['Survived'][pd_train['Sex'] == 'female']))
print(' Survivors related to the class:')
print('% of 1st class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 1]))
print('% of 2nd class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 2]))
print('% of 3rd class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 3]))
print('-------------------')
"""

"""
# Column entitle
print('Column names')
print(train.columns)
print('-------------------')
"""

"""
# Count number of missing values per column
print(train.describe(include="all"))
print('-------------------')
"""

"""
# Checking for unusable values
print(pd.isnull(train).sum())
print('-------------------')
"""

