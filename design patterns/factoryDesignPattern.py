#Factory Design Pattern

'''
Factory Pattern provides an interface for creating objects without specifying 
their exact class in the client code.

Instead of creating objects directly using ClassName(),
you let a factory method decide which subclass or type of object to create.

When we have to decide on runtime what particular instance we have to create'''

from abc import ABC, abstractmethod

#Interface
class IPerson(ABC):

    @abstractmethod
    def person_method():
        '''This is an interface method'''

class Student(IPerson):

    def __init__(self, name):
        self.__name = name

    def person_method(self):
        print("I am a Student")

class Teacher(IPerson):
    def __init__(self, name):
        self.__name = name

    def person_method(self):
        print("I am a Teacher")

#The main problem in factory method pattern is that it uses too much if else statements
class PersonFactory:
    @staticmethod
    def build_person(type: str,name):
        if type.capitalize() == "Student":
            return Student(name)
        elif type.capitalize() == "Teacher":
            return Teacher(name)

if __name__ == "__main__":
    choice = input("Enter Choice: ")
    name = input("Enter Name of Person: ")

    person = PersonFactory.build_person(choice,name)
    person.person_method()




