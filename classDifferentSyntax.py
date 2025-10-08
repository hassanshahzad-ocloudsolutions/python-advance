#Meta Classes

def hello():
    class employee:
        def greet(self):
            print("Hello from employee class inside hello()")
    return employee

emp_class = hello()  # This returns the employee class
obj = emp_class()    # Now create an object of that class
obj.greet()

# Test = type('Test', (), {}) equivalent to below syntax
class Test:
    pass

print(Test)
print(Test())
print(type(Test))

class Foo:
    def show(self):
        print("Hi")


def add_attribute(self):
    self.z = 9

#() contains classs from which child class is inherited from, {} contains attributes
AnotherClass = type('Boo', (Foo,), {"x":5 , "add_attribute":add_attribute})
a = AnotherClass()
a.show()
a.add_attribute()
print(a.z)


