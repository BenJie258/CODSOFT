import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

titanic=pd.read_csv(r'C:/Users/C-Note/Desktop/CODSOFT/Task 1/titanic_dataset.csv')
print(titanic.head()) 

print(titanic.shape)




