#type hinting
#mypy a tool used for type hinting

#python is dynamically typed langauage so we are not aeare of the data type. We can check datatype only on runtime

def myFunction(parameter: int)->str:
    return f'{parameter} is a good number'

def otherFunction(parameter: str):
    print(parameter)

print(myFunction(10)) #program will execute smoothly as python as dynamically typed int infunction is like comment
otherFunction(myFunction(10))
#if the file is run using mypy in terminal we got error