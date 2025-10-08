'''
A meta class is a class that defines how a class behaves.

Just like a class defines how objects behave,
a metaclass defines how classes behave.

In python, class creates objects. Class even itself is a object 

Purpose of metaclass, To control or modify how classes are created
    
'''

#a class to be a meta class must be inherited by type
class Meta(type):
    #it is called before __init__ to create object, __init__ initializes the values
    #metaclass can modifies the attributes and functions of the class it is ruling at

    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name,item in attrs.items():
            if name.startswith("__"):
                a[name] = item
            else: 
                a[name.upper()] = item
        print(a)
        

class Dog(metaclass = Meta):
    x = 5
    y = 8

    def hello():
        print("Hi, it is a dog")


class Cat(metaclass = Meta):
    x = 5
    y = 8

    def hello():
        print("Hi, it is a cat")

