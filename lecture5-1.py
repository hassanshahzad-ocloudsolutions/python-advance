#Events Threads

#Events is something that can be triggered and in response we have to do something

import threading
'''An Event is a simple signaling mechanism between threads.
It lets one thread wait for another thread to send a signal that “something has happened.”'''

event = threading.Event() #This object can be triggered

def myFunction():
    print("Waiting for event to be triggered!")
    event.wait() #code will stuck here and waiting for event to be triggered
    print("Performing action xyz now....Reaction of event")

t1 = threading.Thread(target=myFunction)
t1.start()

x = input('Do you want to trigger the event? (y/n)')

if( x.lower() == 'y'):
    event.set() #triggers the event

elif(x.lower()=='y'):
    pass
