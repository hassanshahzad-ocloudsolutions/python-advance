#Context Manager

'''A context manager in Python is a construct that sets up and tears down 
resources automatically. It is typically used with the "with" statement'''

'''
The below is context manager

with open("data.txt", "r") as file:
    data = file.read()
    print(data)

when code enters "with" then
Python opens the file (__enter__ is called)

when code exits "with" then 
Python closes the file (__exit__ is called)
'''

#Custom Context Manager
class Open_File:
    def __init__(self,filename, mode):
        self.__filename = filename
        self.__mode = mode

    #dunder methods
    def __enter__(self):
        self.file = open(self.__filename, self.__mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

#another way to make custom context manager is 

from contextlib import contextmanager

#by using decorators, generators and annotators
@contextmanager
def open_file(file,mode):
    f = open(file,mode)
    yield f
    f.close()

with Open_File("text.txt",'r') as f:
    content = f.read()

print(content)
print(f.closed)

with open_file("text.txt",'r') as f:
    content2 = f.read()
print(content2)

