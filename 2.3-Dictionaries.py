#List, Tuple, Set, Dictionary
#           Orderded        Changeable      Duplicate
#List           /               /               /
#Tuple          /               X               /
#Set            X               X               X
#Dictionary     /               /               x
#Dictionaries are like strucks or simple class in C++

#Summary
"""
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict, "\n\n")

# Changing #######################################################################################
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()      #Gets the keys
y = car.values()    #Gets the values
z = car.items()     #Get the keys and values
print(x) #before the change
print(y) #before the change
print(z, "\n") #before the change


car["color"] = "white"  #Adds a key and value, "dict.update({key: val})" alternative
print(x) #after the change
print(y) #after the change
print(z, "\n\n") #after the change

# Removing #######################################################################################
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")   #del dict[key] - alternative
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()    #del dict - alternative
print(thisdict)

# Looping #######################################################################################
#Same with List

# Nested #######################################################################################
#Method 1
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Method 2
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}