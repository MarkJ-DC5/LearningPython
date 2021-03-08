#List, Tuple, Set, Dictionary
#           Orderded        Changeable      Duplicate
#List           /               /               /
#Tuple          /               X               /
#Set            X               X               X
#Dictionary     /               /               x

#Summary
"""
Some function from list is applicable
count()     Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
"""

# Tuple #######################################################################################
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Accesing #######################################################################################
#Same with List

# Changing, Adding, Removing #######################################################################################
#Not Allowed

# Unpacking #######################################################################################
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits #tropic will be a list containing the element before red = cherry
print(green)
print(tropic)
print(red)

# Looping #######################################################################################
#Same with List

# Joining and Multiply #######################################################################################
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

