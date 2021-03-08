# Functions #######################################################################################

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Unknown number of Argument
def my_function1(*kids):
  print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")

#Keyword
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Default
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passig List
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Returning
def my_function(x):
  return 5 * x          #multiple items can be return as tuple, unpack later

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda #######################################################################################
#lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6))