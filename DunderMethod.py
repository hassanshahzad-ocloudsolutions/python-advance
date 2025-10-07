
#Magic Methods/Dunder(Double Underscore) Methods

'''
Magic Methods are not called manually directly using dot but we can.

def __init__(self,name,age,location), the constructor is also a dunder method
def __del__(self), the destructor is also a dunder method

'''

class Vector:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f'X coordinate {self.__x} and Y Coordinates {self.__y}'
    
    def __add__(self,other):
        return Vector(self.__x+other.__x , self.__y+other.__y)
    
    def __sub__(self,other):
        return Vector(self.__x-other.__x , self.__y-other.__y)
    
    def __mul__(self,other):
        return Vector(self.__x*other.__x , self.__y*other.__y)
    

    
    def __truediv__(self,other):
        return Vector(self.__x//other.__x , self.__y//other.__y)
    
    def __call__(self):
        print("I was Called....")

    def __pow__(self,other):
        return Vector(self.__x**other.__x , self.__y**other.__y)
    
    def __eq__(self,other):
        return self.__x == other.__x and self.__y == other.__y

    def __neg__(self):
        return Vector(-self.__x , -self.__y)
    

v1 = Vector(2,3)
v2 = Vector(5,6)
v3 = Vector(2,3)

print(v1) #dunder method called behind the scene we can also manually call like below
print(v1.__str__())

print(v1+v2)
print(v1.__add__(v2))

print(v1-v2)
print(v1/v2)
print(v1.__mul__(v2))
print(v1**v2)
print(v1==v3)
print(-v1)
v1()
        
        


