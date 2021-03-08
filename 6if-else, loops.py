# IF-else statements #######################################################################################
#and, or
#pass for no action
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# While Loops #######################################################################################
i = 1
while i < 6:
    print(i)
    if i == 3:
        continue
    elif i == 5:
        break
    i += 1
else:
    print("i is no longer less than 6")
    
# For Loops #######################################################################################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for x in range(2, 30, 3):   #range(start, end, increment)
  print(x)
else:
  print("Finally finished!")
