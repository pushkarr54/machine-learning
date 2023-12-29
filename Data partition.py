"""
Created on Tue Apr 18 12:25:35 2023
"""

# step1: 
# import the data
import pandas as pd
df = pd.read_csv("breast_cancer.csv")
df
df.dtypes
df.shape

# step2: 
# split the variables
Y = df["Class"]
X = df.iloc[:,1:10]
df.head()
# df[df.columns[[1,2,3,4,5,6,7,8,9]]]
list(X)

# step3: 
# Data transformation
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
Y = LE.fit_transform(Y)

# step4: Data partition
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.30,random_state=42)

# training samples --> 478
X_train.shape
Y_train.shape

# test samples --> 205
X_test.shape
Y_test.shape

# step5:  model fitting
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

logreg.fit(X_train,Y_train) # fitting the model

# predictions
Y_pred_train = logreg.predict(X_train)
Y_pred_test  = logreg.predict(X_test)

# step6: Metrics
from sklearn.metrics import accuracy_score
print('Training Accuracy score: ' ,accuracy_score(Y_train,Y_pred_train).round(2))
print('Test Accuracy score: ' ,accuracy_score(Y_test,Y_pred_test).round(2))


Traning_accuracy = []
Test_accuracy = []

for i in range(0,1000):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.30,random_state=i)
    logreg.fit(X_train,Y_train)
    Y_pred_train = logreg.predict(X_train)
    Y_pred_test  = logreg.predict(X_test)
    Traning_accuracy.append(accuracy_score(Y_train,Y_pred_train).round(2))
    Test_accuracy.append(accuracy_score(Y_test,Y_pred_test).round(2))

import numpy as np    
print('Average Training Accuracy',np.mean(Traning_accuracy).round(2))
print('Average Test Accuracy',np.mean(Test_accuracy).round(2))

#=============================================================================

