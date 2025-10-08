#Singleton Design Pattern
'''
A Singleton Pattern ensures that only one instance of a class is created throughout the entire program —
and that same instance is used everywhere.

real world usecase in database connection, configurations, logging. 
'''


'''Synchronization is required in singleton design pattern to make thread safe usage
as in multithread environment it is possible that two threads running concurrently enters
in function and initialize __instance with their respective objects in this scenerio two
separate objects have been created
'''

'''One use case of singleton design pattern is database connection
I have an application having multiple modules login, sign up, payments etc 
each module should be connected to database via single connection else there will be much
inconsistencies
'''

from abc import ABC, abstractmethod
import threading

class DatabaseSingleton:
    __lock = threading.Lock()
    __instance = None #Parivate variable to store the instance 

    #In python there is no concept of private constructor so we have done like this.
    def __init__(self, name):
        if DatabaseSingleton.__instance != None:
            raise Exception ("Database conenction cannot be instantiated more than once...")
        else:
            self.__name = name

    @staticmethod
    def get_instance():
        DatabaseSingleton.__lock.acquire()
        if DatabaseSingleton.__instance == None:
            DatabaseSingleton.__instance = DatabaseSingleton("ocs.db")
        DatabaseSingleton.__lock.release()
 
        return DatabaseSingleton.__instance
    
    def get_data(self):
        return f'{DatabaseSingleton.__instance.__name}'
    
d1 = DatabaseSingleton.get_instance()
d2 = DatabaseSingleton.get_instance()
d3 = DatabaseSingleton.get_instance()

print(d1.get_data())
print(d2.get_data())
print(d3.get_data())

    



