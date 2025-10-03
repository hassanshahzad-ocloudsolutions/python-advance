#classes concepts

class Person:
    totalCount = 0 #class variable associated with class ie same for all objects similar to static variables.
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        Person.totalCount+=1
    
    def showDetails(self):
        return f'{self.__name} is {self.__age} years old'
    
    def __str__(self): # will help in prinitn whole object as print(obj)
        return "name: {}, Age: {}".format(self.__name,self.__age)


p1 = Person("Hassan Shahzad" , 21 )
p2 = Person("Ali Ahmad" , 24)
print(p1)
print(Person.totalCount)