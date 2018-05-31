#Machine learning program 20180101
#Kaggle: titanic machine learning from disaster
#By James-Martin TA

import numpy as np      #Import NumPy for the maths functions and array
import pandas as pd     #Import Pandas for using csv doc


#Load the data
pd_train = pd.read_csv("files/train.csv")
pd_test = pd.read_csv('files/test.csv')

'#Normalization'



#Exploratory Data Anlysis
print('Training Data:')
print("Number of passengers:", len(pd_train))
print("Number of survivors:", len(pd_train[pd_train['Survived'] == 1]))
print('Survivors related to sex')
print('% of men who survived', 100*np.mean(pd_train['Survived'][pd_train['Sex'] == 'male']))
print('% of women who survived', 100*np.mean(pd_train['Survived'][pd_train['Sex'] == 'female']))
print('Survivors related to the class')
print('% of 1st class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 1]))
print('% of 2nd class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 2]))
print('% of 3rd class who survived', 100*np.mean(pd_train['Survived'][pd_train['Pclass'] == 3]))

