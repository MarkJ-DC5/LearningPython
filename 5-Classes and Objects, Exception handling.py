class Person:
    __personCount = 0   #global variable
    
    def __init__(self, p_name = "NA", p_age = -1):     #constructor
        #"_" - protected - accesable but should not be acces out of class
        #"__" - provate - cannot be accesed
        self.setName(p_name)
        self.__label = "NA"
        self.setAge(p_age)
        
        Person.__personCount += 1
        
    def setName(self, p_name):
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
            print("Done Checking Name Input")
            
    def getName(self):
        return self.__name
        
    def setAge(self, p_age):
        try:
            if (p_age > 0 and p_age <= 150):
                self.__age = p_age
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
            print("Done Checking Age Input")
                        
    def getAge(self):
        return self.__age
    
    def display(self):
        print("Name is", self.__name, "and age is", self.__age, self.__label, "old")
        
        
per1 = Person("Mark Jayson", 2)
per1.display()

del per1

#per1.display() - will cause an error since per1 is deleted
