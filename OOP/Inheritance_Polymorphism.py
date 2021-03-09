#Module
from BaseClass import Person

#Inheritance
class Student(Person):
    def __init__(self, p_name, p_age, p_studNum):
        Person.__init__(self, p_name, p_age) #prevent overiding of parent's init
        super().__init__(p_name, p_age)  #inherits all methods and properties
        self.studNum = p_studNum
    
    #Polymorphism
    def disp(self):
        self.__str__()
        print(self.studNum)

s1 = Student("Mark", 19, 2017)
print(s1)
s1.disp()