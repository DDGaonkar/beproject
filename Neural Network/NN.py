#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:37:17 2019

@author: deepanshu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data1.csv')
# X: independent variable matrix & y: dependent variable vector
X = dataset.iloc[:,1:7].values
# X = pd.DataFrame(X)
Y  = dataset.iloc[:,0].values

# Encoding data
# from sklearn.preprocessing import LabelEncoder
# labelencoder_x = LabelEncoder()
# X = labelencoder_x.fit_transform(X)

# splitting the dataset into training set and testing set 
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

"""
# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

# Importing keras libraries and packages
import keras 
from keras.models import Sequential
from keras.layers import Dense 

# Initializing the ANN
model = Sequential()

# Adding the input layer and the first hidden layer
# model.add(Dense(4, kernel_initializer = 'uniform', activation = 'relu', input_dim == 6))    
model.add(Dense(4, kernel_initializer = 'uniform' , activation = 'relu', input_dim = 6))    

# Adding another hidden layer 
model.add(Dense(4, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer 
model.add(Dense(units= 1, kernel_initializer = 'uniform', activation = 'linear'))        

# Compiling the ANN
model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['accuracy'])

# Fitting the ANN to the training set 
model.fit(X_train, Y_train, batch_size = 10, epochs = 100, validation_split=0.2)

# predicting the test set result 
Y_pred = model.predict(X_test)

"""
# Applying k-fold cross validation 
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = model, X = X_train, y = Y_train, cv = 10)
accuracies.mean()
accuracies.std()
"""
"""
# Making the confusion matrix 

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred) 
"""

"""
# fitting Multiple Linear Regression to the training set 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# predicting test set results 
Y_pred = regressor.predict(X_test)
"""
