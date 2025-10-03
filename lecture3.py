#Multi-Threading

#Thread, a light weight process that shares the same memory and resources of the parent process. 
#It is the smallest unit of execution within a process
#helps in speeding up our programs by executing multiple tasks at the same time.

#The below example is showin concurrency
import threading

def helloworld():
    for i in range(10):
        print("Hello World")


def goodMorning():
    for i in range(10):
        print("Good Morning")

t1 = threading.Thread(target=helloworld)
t2 = threading.Thread(target=goodMorning)

#we created two threads each for the function we defined earlier. These two threads are running concurrently. This is multithreading
t1.start()
t2.start()

#Multithreading helps in acheiving concurrency(Many tasks appear to run simultaneously) and parallelism(Many tasks are actually running simultaneously)






