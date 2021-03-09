class Person:
    __personCount = 0   #global variable
    
    def __init__(self, p_name = "NA", p_age = -1):     #constructor
        # Encapsulation
        # "_" - protected - accesable but should not be acces out of class, use for child only
        # "__" - private - cannot be accesed
        self.setName(p_name)
        self.__label = "NA"
        self.setAge(p_age)
        
        Person.__personCount += 1
        
    def setName(self, p_name):
        print("=========================================Setting Name:")
        
        #Exception Handling
        try:
            if p_name != "":
                self.__name = p_name
            else:
                raise Exception("Invalid Input")
        except:
            print("Invalid Name!")
            print("Name set to NA")
        else:
            print("Name is Valid")
        finally:
            print("Done Checking Name Input \n")
        
        
    def getName(self):
        return self.__name
        
    def setAge(self, p_age):
        print("=========================================Setting Age")
        
        #Exception Handling
        try:
            if (p_age > 0 and p_age <= 150):
                self._age = p_age
                if p_age != 1:
                    self.__label = "years"
                else:
                    self.__label = "year"
            else:
                raise Exception("Invalid Input")
        except:
            print("Invalid Age!")
            print("Age set to -1")
        else:
            print("Age is Valid")
        finally:
            print("Done Checking Age Input \n")
                        
    def getAge(self):
        return self._age
    
    def display(self):
        print("Name is", self.__name, "and age is", self.__age, self.__label, "old")
        
    #Overiding Method
    def __str__(self):
        return self.__name + " " + str(self._age)
        
    def dispAll(p_persons):
        for person in p_persons:
            print(person)
           
    __repr__ = __str__  #print list in the formatted by __str__ function
    
    #Operator Overload
    #Arithmetic
    # __add__
    # __sub__
    # __mul__
    # __pow__
    # __truediv__ - /
    # __floordiv__ - //
    # __mod__ - %
    #Comparison
    # __lt__
    # __le__
    # __eq__
    # __ne__ 
    # __gt__ 
    # __ge__  
        
persons = [Person("Mark Jayson", 19), Person("Francis", 7)]
Person.dispAll(persons)
print(persons)
del persons
#Person.dispAll(persons) - will cause an error since per1 is deleted
