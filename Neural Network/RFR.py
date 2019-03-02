#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:32:54 2019

@author: deepanshu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data2.csv')
# X: independent variable matrix & y: dependent variable vector
X = dataset.iloc[:,1:7].values
# X = pd.DataFrame(X)
Y  = dataset.iloc[:,0].values

# Splitting the dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler 
sc_x = StandardScaler()
sc_y = StandardScaler()
X_train = sc_x.fit_transform(X_train)
Y_train = sc_y.fit_transform(Y_train)

# fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X, Y)
"""
# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=55, random_state=10)
regressor.fit(X_train, Y_train)

# predicting new result
ypred = regressor.predict(X_test[13])
# regressor.score(X, Y)

errors = abs(ypred - Y_test[13])

print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / Y_test)

# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
# Y_pred = sc_y.inverse_transform(regressor.predict(sc_x.fit_transform(X_test)))

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(regressor, X = X_train, y = Y_train, cv=5, scoring='accuracy')
accuracies.mean()
accuracies.std()

from sklearn import metrics
score = np.sqrt(metrics.mean_squared_error(ypred,Y_test))
