#Recursion, a function calling itself again and again must have a base condition to avoid stack overflowing

def factorial(n):
    if n<1:
        return 1
    
    return n*factorial(n-1)


def fibonacci(n):
    if n==1 or n==0:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)

print(factorial(5))
print(fibonacci(5))

