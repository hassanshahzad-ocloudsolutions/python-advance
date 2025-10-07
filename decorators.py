#Decorators

'''
A decorator in Python is a function that modifies the behavior of another function (or class) — 
without permanently changing its code.
It is a higher-order function, meaning:
It takes a function as input, Adds extra functionality, And returns a new function.

Some Real World Applications

Logging and Auditing, Authentication, Timming and Performance Monitoring, Input Validation

'''

def myDecorator(originalFunction):
    def wrapperFunction():
        print("I am decorating your function")
        originalFunction()
        print("I have decorated your function")
    
    return wrapperFunction

@myDecorator #must annotate with the decorator which has to do decoration
def greet():
    print("Hello world....")


def anotherDecorator(originalFunction):
    def anotherWrapperFunction(*args):
        print("I am decorating your function")
        return originalFunction(*args)
    
    return anotherWrapperFunction

@anotherDecorator
def helloName(fname,lname):
    return f'Hello {fname} {lname}'

print(helloName("Hassan","Shahzad"))
