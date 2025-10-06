#synchronizing the threads (managing multiple threads that are accessing the shared resource ie concepts of locking, semaphore will be discussed)


#Locking Concept
# with lock, automaticaly handles acquiring and releasing the lock

import threading
import time

x = 8192
lock = threading.Lock()

def double ():
     #This function will double the shared resource ie x

     #access the x that is not part of this function but global ie global x

     global x, lock
     lock.acquire() #will acquire a lock ie lock the resource if it is free else will wait for other thread to release the resource
     while(x<8192*2):
          x*=2
          print(x)
          time.sleep(1)
     print("Maximum Value Reached")
     lock.release() #release the lock to be acquire by other threads


def halve():
     #This function will half the shared resource

     global x
     lock.acquire() #will acquire a lock ie lock the resource if it is free else will wait for other thread to release the resource
     while(x>1):
          x/=2
          print(x)
          time.sleep(1)
     print("Minimum Value Reached")
     lock.release()


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)



t1.start()
t2.start()
#Without Locking we will never reach any of the end either maximum or minimum as both threads will be running concurrently    
#output without synchronization            
'''4096
8192
16384
8192
16384
8192
16384
'''

'''If each thread works with its own local variables (no shared/global data),
there’s no need for synchronization — no interference is possible.'''