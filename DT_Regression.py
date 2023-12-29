"""
Created on Thu Apr 27 13:21:26 2023
"""

import pandas as pd  

df = pd.read_csv("Boston.csv")  
df.shape
df.head() 
#df.info()

# split the variables as X and Y
Y = df["medv"]
X = df.iloc[:, 1:14]
X.head()

# data paritions
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y)

from sklearn.tree import DecisionTreeRegressor
DT = DecisionTreeRegressor()
DT.fit(X_train,Y_train)

DT.tree_.node_count # counting the number of nodes
DT.tree_.max_depth # number of levels

Y_Pred_train = DT.predict(X_train)
Y_Pred_test =  DT.predict(X_test)

import numpy as np
from sklearn.metrics import mean_squared_error
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))

mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("Single DT,Difference of Train and Test: ",(mse2-mse1).round(2))

#====================================================
# bagging
#====================================================

from sklearn.ensemble import BaggingRegressor
bag = BaggingRegressor(base_estimator=DecisionTreeRegressor(),n_estimators=100,
                 max_samples = 0.6,max_features=0.7)

# help(BaggingRegressor)
bag.fit(X_train,Y_train)
Y_Pred_train = bag.predict(X_train)
Y_Pred_test =  bag.predict(X_test)
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))
mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("Bagging - Difference of Train and Test: ",(mse2-mse1).round(2))

#====================================================
# Random Forests
#====================================================

from sklearn.ensemble import RandomForestRegressor
RFR = RandomForestRegressor(n_estimators=100,
                 max_samples = 0.6,max_features=0.7)

# help(BaggingRegressor)
RFR.fit(X_train,Y_train)
Y_Pred_train = RFR.predict(X_train)
Y_Pred_test =  RFR.predict(X_test)
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))
mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("Random Forests - Difference of Train and Test: ",(mse2-mse1).round(2))

#===============================================================================
# Gradient Boosting Regressor
#===============================================================================
from sklearn.ensemble import GradientBoostingRegressor
GBR = GradientBoostingRegressor(learning_rate=0.01,n_estimators=300,)

GBR.fit(X_train,Y_train)
Y_Pred_train = GBR.predict(X_train)
Y_Pred_test =  GBR.predict(X_test)
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))
mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("Gradient Boosting - Difference of Train and Test: ",(mse2-mse1).round(2))

#===============================================================================
# Adaptive Boosting Regressor
#===============================================================================
from sklearn.ensemble import AdaBoostRegressor
ABR = AdaBoostRegressor(n_estimators=100,learning_rate=0.1)

ABR.fit(X_train,Y_train)
Y_Pred_train = ABR.predict(X_train)
Y_Pred_test =  ABR.predict(X_test)
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))
mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("Adaptive Boosting - Difference of Train and Test: ",(mse2-mse1).round(2))

#=======================================================================

# pip install xgboost
from xgboost import XGBRegressor
XGB = XGBRegressor(gamma=10,reg_lambda=4,n_estimators=100,learning_rate=0.1)

XGB.fit(X_train,Y_train)
Y_Pred_train = XGB.predict(X_train)
Y_Pred_test =  XGB.predict(X_test)
mse1 = np.sqrt(mean_squared_error(Y_train,Y_Pred_train))
print("Training Error: ",mse1.round(3))
mse2 = np.sqrt(mean_squared_error(Y_test,Y_Pred_test))
print("Test Error: ",mse2.round(3))
print("XGB - Difference of Train and Test: ",(mse2-mse1).round(2))

# Grid Search CV
gamma = [5,10,20]
reg_lambda = [4,8,12]
n_estimators = [100,200,300]

#=======================================================================









