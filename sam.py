# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:34:56 2023


"""

import streamlit as st
import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd

st.title('Churn Prediction App')

feature_cols = ['Account_length', 'Voice_messages', 'International_plan',
       'International_minutes', 'International_calls', 'International_charge',
       'Day_mins', 'Day_calls', 'Day_Charge', 'Evening_minutes',
       'Evening_Calls', 'Evening_charge', 'Night_min', 'Night_calls',
       'Night_charge', 'Customer_calls']

# Load the trained model
model = joblib.load(open("./LogisticRegression.pkl", "rb"))

# Define the Streamlit app
def main():
    input={'no':0 , 'yes':1}
    # Create input fields for user to input data
    account_length = st.number_input('Account Length', 0, 243, 0)
    International_plan = st.selectbox('International_plan ', ['no', 'yes'])
    input_fields=[]
    for i in [ 'Voice_messages', 
           'International_minutes', 'International_calls', 'International_charge',
           'Day_mins', 'Day_calls', 'Day_Charge', 'Evening_minutes',
           'Evening_Calls', 'Evening_charge', 'Night_min', 'Night_calls',
           'Night_charge', 'Customer_calls'
       ]:
        input_fields.append(st.number_input(i))
    
    user_input=[account_length,*input_fields,input[International_plan]]

   
    # Make predictions
    if st.button('Predict'):
        prediction = model.predict([user_input])
        
        if prediction[0]==0:
            st.success('Prediction churn = No')
        else:
            st.success('prediction churn = Yes')

if __name__ == '__main__':
      main()






