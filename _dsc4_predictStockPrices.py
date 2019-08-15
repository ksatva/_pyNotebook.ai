#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Predict stock prices

Prerequisites:
    1. dependencies
    2. historical data from finance.google.com (csv file)

Created on Wed Aug 14 17:59:56 2019
@author: k as root
"""

import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates=[]
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates),1))
    
    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel = 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Data')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('/root/ai/_Datasets/GOOG.csv')

predicted_price = predict_prices(dates, prices, 29)

print(predicted_price)

#1. Efficient market hypothesis says stock prices are unpredictable
#2. Machine learning can give us slightly better than random predictions
#3. Support Vector Machines can be used for classification and regeressions

# TODO: Use a neural network to predict stock prices using sentiment analysis and price history
#https://www.youtube.com/watch?v=SSu00IRRraY&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=4