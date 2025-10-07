#Practical Example of Decorators
import random

def logged(function):
    def wrapper(*args,**kwargs):
        value = function(*args,**kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value} \n')
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

@logged
def subract(x,y):
    return x-y

@logged
def multiply(x,y):
    return x*y

l1 = [add,subract,multiply]

for i in range(15):
    func = random.choice(l1)
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print(func(x, y))
    


        