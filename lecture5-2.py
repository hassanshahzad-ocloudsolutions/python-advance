#Generally showing in code how event is a signalling mechanism


import threading
import time

event = threading.Event()

def functionForThread1():
    print("Function1 called")
    event.wait() # waiting that someones trigger this event
    print("Signal Received")

def functionForThread2():
    print("Function2 called")
    print("Function2 doing some work")
    event.set() # triggers the event that is being waiting in function1
    print("Function2 Ended")

t1 = threading.Thread(target=functionForThread1)
t2 = threading.Thread(target=functionForThread2)

t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("All threads done!") # the main thread will wait untill both threads t1 and t2 have completed their execution due to .join()

