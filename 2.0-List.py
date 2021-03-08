#List, Tuple, Set, Dictionary
#           Orderded        Changeable      Duplicate
#List           /               /               /
#Tuple          /               X               /
#Set            X               X               X
#Dictionary     /               /               x

#Summary
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

# Accesing #######################################################################################
thislist = ["apple", "banana", "cherry"] #list((elem1, elem2, elem3)) can also be used
print(thislist, "\n")

thislist = ["apple", "banana", "cherry"]
print(len(thislist), "\n")

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  
print(thislist[-1])    #Negative index start at the end with index -1

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    #range -end is excluded
print(thislist[2:])
print(thislist[:5])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: #in - check if x is in list
  print("Yes, 'apple' is in the fruits list")

# Changing & Adding #######################################################################################
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  #applicable to range also
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")    #insert(loc, value) - alternative
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #add to the end of the list
print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2   #alternative
print(list3)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)   #adds y list to the x list, applicable to any iterable
print(thislist)

# Removing #######################################################################################
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")   #remove by element
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #remove by index
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  #remove the last element
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #alternative
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #alternative

# Looping #######################################################################################
thislist = ["apple", "banana", "cherry"]
for x in thislist:  #loop via element
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): #loop via index
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):    #while loop
  print(thislist[i])
  i = i + 1

# Sorting #######################################################################################
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #Alphanumerical sorting
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)   #alternative
print(thislist)

#Custom Sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Copying #######################################################################################
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
