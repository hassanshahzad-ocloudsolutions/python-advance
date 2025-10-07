
def myFunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    
    print(kwargs["KEYONE"])
    print(kwargs["KEYTWO"])


a = "hey"
b = True
c = 19
d = "Wow"
e = "Test"
f = 7

myFunction(a,b,c,KEYONE=e,KEYTWO=f)