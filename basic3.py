"""
Created on Mon Mar 20 13:20:15 2023
"""
# control structures

#-------------------------------------------------
score = 50

if score > 60:
    print("You are Qualified")
else:
    print("You are not Qualified")
#-------------------------------------------------

score = 70
Edu = 'Btech'

if score > 60 and Edu == 'Btech':
    print("You are Qualified")
else:
    print("You are not Qualified")
#-------------------------------------------------

score = 50
Edu = 'Btech' # single equal --> assignment operator
              # == --> it is comparing
              
if score > 60 and (Edu == 'Btech' or Edu == 'Bcom'):
    print("You are Qualified")
else:
    print("You are not Qualified")

#----------------------------------------------------
# if - elif- else
score = 70
Edu = 'Bcom'

if score > 60 and Edu == 'Btech':
    print("You can apply for Data scientist")
elif score > 60 and Edu == 'Bcom':
    print("You can apply for Jr. Analyst")
else:
    print("Better luck next time")
#----------------------------------------------------
# Nested if 

status = 'Indian'
Gender = 'Female'
age = 22

if (status == 'Indian'):
    if (Gender == 'Male'):
        if (age > 21):
            print("You are qualified for army")
        else:
            print("Thanks for your interest, try next year")
    elif (Gender == 'Female'):        
        if (age > 21):
            print("You are qualified for airforce")
        else:
            print("Thanks for your interest, try next year")
else:
    print("You are invalid criteria")
#----------------------------------------------------

            
           

            
            
            
            
    








    












