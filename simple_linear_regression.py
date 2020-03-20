# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:14:52 2020

@author: User
"""
#placing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


#Splitting the dataset into training and test set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)


#feature scaling
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train=sc_X.fit_transform(X_train)
#X_test=sc_X.transform(X_test)

#fitting simple linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#predicting the test set results
y_pred=regressor.predict(X_test)


#visualizing the training set result
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience {Training Set}')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


#visualizing the training set result
plt.scatter(X_test,y_test,color='red')
#we don't need to change on the plot from train to test as our regressor is already on train
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience {Training Set}')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()











