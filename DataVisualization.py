# DATA VISUALIZATION

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

