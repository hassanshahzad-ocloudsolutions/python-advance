#Semaphore

import threading
import time

semaphore = threading.BoundedSemaphore(value=2) #specifies the maximum number of threads that can acquire (enter) the semaphore at the same time.

#BoundedSemaphore raises an error if there are more releases than acquire.

'''The Difference between lock and semaphore is lock only allows one thread to enter into critical section
while semaphore allows multiple threads to enter into critical section at one time'''

def access(thread_number):
    print(f'{thread_number} trying to access the resource.')
    semaphore.acquire()
    print(f'{thread_number} granted access to resource.')
    time.sleep(5) #granted access for 5 seconds
    print(f'{thread_number} is releasing the resource.')
    semaphore.release()


for thread in range(11):
    t = threading.Thread(target=access , args=(thread,))  #args take the arguments that has to be passed to the function set in target.
    t.start()
    time.sleep(1)


'''Semaphore makes sense in this example
Suppose you have a web server with 100 threads,
but your database can handle only 10 connections at a time.'''