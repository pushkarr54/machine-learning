# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:21:27 2023

@author: excel
"""

# lists  --> we can many values and different data types in one object

L1 = []

L1 = [10,20,30,40,50,60,72.3,'cat',True]
L4 = L1
L4

len(L1)

# access the value
L1[0]
L1[3]
L1[7] = 75 # modify the value
L1

L1[-1]
L1[-2]

L1.pop() # by default last value will be removed
L1

L1.pop(6) # if we pass number inside brackets, it will removes that position value
L1

L1.append(80) # added at the last
L1
sum(L1)
avg = sum(L1)/len(L1)
avg

L2 = [3,5,7,9, [2,4,6,8],11,13]
L2[0]

L2[4][0]
L2[4][1]
L2[4][2]

sum(L2[4])


L3 = [45,23,65,14,15,77,19,24]
L3
L3.sort() # ascending order
L3

L3.sort(reverse=True) # descending order
L3

2 * L3

#-----------------------------------------------------
# Tuples --> once you assign anyvalue, we cannot modified 
# we cannot remove, we cannot add
T1 = ()

T1 = (10,20,30,40,50,60)
T1

T1[0]

T1[0] = 12

T2 = list(T1)
T2

#-----------------------------------------------------
# dictionary  ---> keys and values

d1 = {'Hyd' : 1 , 'Banglore': 2, 'Pune': 3}

d1.keys()
d1.values()

d2 = {'ID': [1,2,3,4], 'Salary': [10000,20000,25000,30000],
      'Exp': [2,4,6,8]}

d2
d2.keys()
d2.values()

d2['ID']
#-----------------------------------------------------
















