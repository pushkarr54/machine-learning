# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:54:58 2023

@author: excel
"""

#==== FTABLE VALUE ================================
import scipy.stats as ftable
ft = ftable.f(dfn=2, dfd=33)
ft.ppf(0.95).round(4) # 5%


import pandas as pd
df = pd.read_csv("Dietplan.csv")
df

from statsmodels.formula.api import ols
anova1 = ols('calories ~ C(Dietplans)',data=df).fit()

import statsmodels.api as sm
table = sm.stats.anova_lm(anova1, type=1) # Type 1 ANOVA DataFrame
table

pvalue = 0.039441
alpha = 0.05

if pvalue < alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#==========================================================

#df = pd.read_csv("market_3.csv")
#df

#df.groupby('Region').sum()


















