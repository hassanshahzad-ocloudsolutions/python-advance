#Proxy Design Pattern

'''Similar to decorator we discussed before
The Proxy Pattern provides a substitute or placeholder for another object to 
control access to it.
'''

from abc import ABC, abstractmethod

class IPerson(ABC):

    @abstractmethod
    def person_method():
        pass

class Person(IPerson):
    def person_method(self):
        print("I am a person")

class proxyPerson(IPerson): #middle man that will help in interacting with the Person

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am proxy functionality")
        self.person.person_method()


p1 = proxyPerson()
p1.person_method()