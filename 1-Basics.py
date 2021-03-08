#Source 
#https://www.w3schools.com/python/default.asp

#Declaring Variables
firstName = "Mark Jayson"
lastName = "Dela Cruz"
age = 10
height = 177.8
isTall = True

#Printing Variables
print(firstName)
print(firstName + " " + lastName) #only one data type when using "+"
print(firstName, lastName) #multiple data type can be used 

#Casting
#str(integer)
#int(string)
#float(string)

#Arithmetic Operation
"""
-
+
*
/
%
// - rounded off quotient
** power
"""

#Getting User Input (with casting, arithmetic)
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = num1 // num2
print(num3)
