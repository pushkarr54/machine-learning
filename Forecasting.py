"""
Created on Tue May 16 13:25:08 2023
"""

import pandas as pd
df = pd.read_csv("footfalls.csv")
df

# lineplot
df.Footfalls.plot()



df["Date"] = pd.to_datetime(df.Month,format="%b-%y")
df

df["month"] = df.Date.dt.strftime("%b") # month extraction
df

df["year"] = df.Date.dt.strftime("%Y") # year extraction
df

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12,8))
heatmap_y_month = pd.pivot_table(data=df,values="Footfalls",index="year",columns="month",fill_value=0)
sns.heatmap(heatmap_y_month,annot=True,fmt="g") #fmt is format of the grid values


# Boxplot for ever
plt.figure(figsize=(8,6))
sns.boxplot(x="month",y="Footfalls",data=df)
plt.figure(figsize=(8,6))
sns.boxplot(x="year",y="Footfalls",data=df)


plt.figure(figsize=(12,3))
sns.lineplot(x="year",y="Footfalls",data=df)

#==============================================================================
# Splitting data
df.shape
Train = df.head(147)
Test = df.tail(12)

import statsmodels.formula.api as smf 
import numpy as np

# linear model
linear_model = smf.ols('Footfalls~t',data=Train).fit()
pred_linear = linear_model.predict(Test['t'])
rmse_linear = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
rmse_linear

# exponential model
Exp = smf.ols('log_footfalls~t',data=Train).fit()
pred_Exp = Exp.predict(Test['t'])
rmse_Exp = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp


#Quadratic 
Quad = smf.ols('Footfalls~t+t_square',data=Train).fit()
pred_Quad = Quad.predict(Test[["t","t_square"]])
rmse_Quad = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_Quad))**2))
rmse_Quad

#Additive seasonality 
add_sea = smf.ols('Footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec',data=Train).fit()
pred_add_sea = add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']])
rmse_add_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea

#Additive Seasonality Quadratic 
add_sea_Quad = smf.ols('Footfalls~t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea_quad = add_sea_Quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','t','t_square']])
rmse_add_sea_quad = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea_quad))**2))
rmse_add_sea_quad

##Multiplicative Seasonality
Mul_sea = smf.ols('log_footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data = Train).fit()
pred_Mult_sea = Mul_sea.predict(Test)
rmse_Mult_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_sea)))**2))
rmse_Mult_sea

#Multiplicative Additive Seasonality 
Mul_Add_sea = smf.ols('log_footfalls~t+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data = Train).fit()
pred_Mult_add_sea = Mul_Add_sea.predict(Test)
rmse_Mult_add_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_add_sea)))**2))
rmse_Mult_add_sea 

#Compare the results 
data = {"MODEL":pd.Series(["rmse_linear","rmse_Exp","rmse_Quad","rmse_add_sea","rmse_add_sea_quad","rmse_Mult_sea","rmse_Mult_add_sea"]),"RMSE_Values":pd.Series([rmse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_add_sea_quad,rmse_Mult_sea,rmse_Mult_add_sea])}

table_rmse=pd.DataFrame(data)
table_rmse.sort_values(['RMSE_Values'])

#=====================================================

new_data = pd.read_csv("Predict_new.csv")
new_data

#Build the model on entire data set
model_full = smf.ols('Footfalls~t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=df).fit()

pred_new  = pd.Series(model_full.predict(new_data))
pred_new

new_data["forecasted_Footfalls"] = pd.Series(pred_new)
new_var = pd.concat([df,new_data])

new_var


new_var[['Footfalls','forecasted_Footfalls']].reset_index(drop=True).plot()
