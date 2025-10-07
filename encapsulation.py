
#Encapsulation, data hiding

'''Python does not have true access modifiers like private, protected, or public in Java/C++.
But it achieves encapsulation using naming conventions.'''

class Person:
    count = 0 # any variable declared inside class but outside the methods is declared as static
    def __init__(self, name, age, location):
        self.__name = name
        self.__age = age
        self.__location = location
        Person.count+=1
    
    @property #lets you turn a method into a read-only attribute, so you can access it like a variable
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age
    
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self,location):
        self.__location = location
    
    @staticmethod
    def getTotalCount():
        return Person.count


p1 = Person("Hassan",21,"Lahore")
p2 = Person("Ali",18,"Lahore")
p3 = Person("Bilal",20,"Lahore")
p1.age = 22
print(p1.name) #due to @property decorator now calling function like attribute
print(p1.age)
print(Person.getTotalCount())