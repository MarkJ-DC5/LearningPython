#List, Tuple, Set, Dictionary
#           Orderded        Changeable      Duplicate
#List           /               /               /
#Tuple          /               X               /
#Set            X               X               X
#Dictionary     /               /               x

#Summary
#To many just google it, you probably won't even use it
#https://www.w3schools.com/python/python_sets_methods.asp

thisset = {"apple", "banana", "cherry"}
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #keeps element that exist on both set, counter part - x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)   #returns element that exist on both set, counter part - z = x.symmetric_difference(y)
print(z)