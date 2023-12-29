"""
Created on Fri Mar 17 12:57:03 2023
"""

# fn + F9

# F9

x = 10

x1 = 2
x1
type(x1)

age = 34.6
age
type(age)

education = "Btech"
type(education)

exam = True
type(exam)

#======================================================
# operators

"""
# Arithematic

+ : Addition
- : Deduction
* : Multiplication
/ : Division
// : integer division or floor division
% : Modulus - return remainder -> it works better when num > den
** : power
"""

x1 = 10
x2 = 20

x1 + x2
x1 - x2
x1 * x2
x1 / x2

x3 = 23
x4 = 5

x3 / x4
x3 // x4
x3 % x4
x4 ** 2

z1 = 24
z2 = 28
z3 = 32
# calculate the average
z4 = (z1 + z2 +z3)/3
z4

#==========================================
height = 1.75
weight = 75

BMI = weight/(height ** 2)
BMI

###############################################################################
"""
# Comparison/Relational operators - Returns boolean values

== : equal-to operator
!= : Not-Equal-to operator
> : Greater than
>= : Greater than or equal to
< : Less than
<= : Less than or equal to
"""
###############################################################################
g1 = 78
g2 = 75

g1 == g2
g1 != g2

g1 > g2
g1 < g2


###############################################################################
"""
# Logical Operators - used along with relational expressions

and : returns True if both operands are True
or  : returns True if any one of the operands are True
not : opposite of the logical operator
"""
###############################################################################

age = 16
height = 165

# army --> age>21 and height 168

age >= 21 and height >= 168

age >= 21 or height >= 168

age >= 21 or height >= 168

age < 21
not(age > 21)







def RecurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * RecurFactorial(num - 1)



output = RecurFactorial(int(input("Enter any number: ")))
print("Factorial : ", output)














