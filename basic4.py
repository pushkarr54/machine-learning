"""
Created on Tue Mar 21 12:09:51 2023

FOR LOOP

"""

range(1,10) # start , end, jump

# print 1-10
for i in range(1,11):
    print(i)

# even numbers    
for i in range(0,11,2):
    print(i)

# odd numbers
for i in range(1,11,2):
    print(i)

for i in range(0,11,3):
    print(i)

#==============================================
age = [22,25,23,21,32,26,27,25,30,19]

for i in age:
    print(i)
    
for i in age:
    if i > 25:
        print(i)

k1 = []
k2 = []
for i in age:
    if i > 25:
        k1.append(i)
    else:
        k2.append(i)

print(k1)
print(k2)
#==============================================
salary = [10000,25000,15000,18000,34000,45000,60000]
updatesalary = []

#10000 * 10/100

for i in salary:
     j = i * 10/100
     updatesalary.append(i + j)

print(updatesalary)

#==============================================

# FUNCTIONS  --> SET OF INSTRUCTIONS  --> a RESUSABLE code

# pre-defined functions, user-defined functions

# square function

def f1(x):
    return x ** 2

f1(5)
f1(1225)
f1(-14)

# 2x square + 3x + 1
def f2(x):
    return 2 * (x **2) + (3*x) + 1

f2(5)

def f3(x,y):
    return (2 * x) + (3*y) + 1

f3(3,4)

#--------------------------------------------------
def f4(x,y,z):
    return (x+y+z)/3

f4(4,6,10)

# many functions  ---> one file ---> one module
# several modules ---> one library
# several libraries ---> one package
# several packages --> one frame work

#--------------------------------------------------------------
# NUMPY, PANDAS, MATPLOTLIB, SEABORN, SCIPY, STATSMODELS
# SCIKIT-LEARN --> MACHINE LEARNING
# NLTK , SPACY
# TENSORFLOW, PYTORCH, KERAS
#--------------------------------------------------------------
































































