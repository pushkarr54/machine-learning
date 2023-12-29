"""
Created on Fri Apr  7 12:49:14 2023
"""

pip install researchpy

import pandas as pd
df = pd.read_csv("credit_new.csv")
df
list(df)
df["Cards"]
df["Ethnicity"]

import researchpy as rp
table, results = rp.crosstab(df['Cards'], df['Ethnicity'], test= 'chi-square')

table
results

# Chi square table values for given alpha and degrees of freedom
import scipy.stats as stats
tabvalue = stats.chi2.ppf(q = 0.95, df = 8)
tabvalue.round(4)

pvalue = 0.0395
alpha = 0.05

if pvalue < alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#=======================================================================
# confidence interval
from scipy.stats import norm
import numpy as np
import pandas as pd
df = pd.read_csv("Lungcapdata.csv")
df.shape

len(df)
df['LungCap'].mean()

# confidence interval  --> 90% confident popu mean will be lies underbelow interval
df_ci = norm.interval(0.90, loc = df['LungCap'].mean(),scale = df['LungCap'].std())
print( '90% confidence interval is:', np.round(df_ci , 4))

# confidence interval  --> 95% confident popu mean will be lies underbelow interval
df_ci = norm.interval(0.95, loc = df['LungCap'].mean(),scale = df['LungCap'].std())
print( '95% confidence interval is:', np.round(df_ci , 4))

# confidence interval  --> 99% confident popu mean will be lies underbelow interval
df_ci = norm.interval(0.99, loc = df['LungCap'].mean(),scale = df['LungCap'].std())
print( '99% confidence interval is:', np.round(df_ci , 4))






















