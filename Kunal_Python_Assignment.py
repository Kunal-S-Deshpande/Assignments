# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:07:01 2024

@author: Kunal S Deshpande
"""
###Assignment 1-Python


'''1. Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5 between 2000 to 3200 (both included), the number 
should be printed as comma separated sequence on a single line'''

Lower_Bound=2000 #Defining Lower bound
Upper_Bound=3200 #Defining Upper bound

List_of_Num=[] #Initialize list 

for i in range(Lower_Bound,Upper_Bound+1):
    if (i%7==0)&(i%5!=0): #Check of divisibility by 7 and if multiple of 5
        List_of_Num.append(str(i))#Append the numbers as string type in list 

Output=",".join(List_of_Num)#Convert list to a comma separated string
print(Output)

'''2.Write a Python program to accept the user's first and last name and then 
getting them printed in the the reverse order with a space between first name 
and last name.'''


First_Name=input("Please enter your first name:")
Last_Name=input("Please enter your Last name:") #User Input

print("Your Name in Reverse:")
print(First_Name[-1::-1]+" "+Last_Name[-1::-1]) #Display in reverse order

'''3.Write a Python program to find the volume of a sphere with diameter 12 cm'''

D=12 #Diameter of the Sphere
from math import pi
Volume=(4/3)*pi*(D/2)**3

print("Volume: "+str(Volume)+" cubic cm")
