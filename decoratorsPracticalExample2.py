#Another Practical Example
import time

def decoratorFunction(originalFunction):
    def wrapper(*args,**kwargs):
        fname = originalFunction.__name__ #Dunder Method
        beforeTime = time.time()
        value = originalFunction(*args,**kwargs) # actual function execution
        afterTime = time.time()
        print(f'{fname} toook {(afterTime-beforeTime)*1000} ms to execute! ')
        return value
    
    return wrapper

@decoratorFunction
def myFunction(x):
    result = 1
    for i in range(1,x):
        result*=i
    return result

myFunction(100000)