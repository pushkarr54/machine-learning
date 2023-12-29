# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:18:44 2023

@author: excel
"""

import pandas as pd
df = pd.read_csv("Sales.csv")
df.head()
df.dtypes
df.shape

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df["ShelveLoc"] = LE.fit_transform(df["ShelveLoc"])
df["Urban"] = LE.fit_transform(df["Urban"])
df["US"] = LE.fit_transform(df["US"])
df["high"] = LE.fit_transform(df["high"])

# split the variables as X and Y
Y = df["high"]
X = df.iloc[:, 1:11]
X.head()

# data paritions
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y)


from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier(criterion='gini',max_depth=6)

DT.fit(X_train,Y_train)

DT.tree_.node_count # counting the number of nodes
DT.tree_.max_depth # number of levels


Y_Pred_train = DT.predict(X_train)
Y_Pred_test =  DT.predict(X_test)

from sklearn.metrics import accuracy_score
ac1 = accuracy_score(Y_train,Y_Pred_train)
print("Training Accuracy: ",ac1.round(3))

ac2 = accuracy_score(Y_test,Y_Pred_test)
print("Test Accuracy: ",ac2.round(3))






















