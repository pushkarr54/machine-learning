"""
Created on Wed Mar 29 13:39:50 2023
"""

from scipy.stats import binom
bi = binom(n=5, p=0.6) # n, p

# case 1
# exactly for 3 P(X = 3)
z1 = bi.pmf(3)  # r = event
z1.round(3)

# P(X = 4)

# case 2
bi.pmf(0)+bi.pmf(1)+bi.pmf(2)
bi.cdf(2) # <=2
# There is 31% chance that atmost 2 people will get 
# approval for the credit card

# case 3 --> P(X>=3)
z2 = 1 - bi.cdf(2)
z2

# Q2
bi = binom(n=250, p=0.7) # n, p

# p(X>=160)
z2 = 1 - bi.cdf(159)
z2
















