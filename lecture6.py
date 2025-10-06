#Queues, data structure FIFO
'''
why queues? 
Because when we have multiple threads running we should have a proper structured of getting in the data 
and getting out the data.

for example, we have list of numbers say n = [1,2,3,4,5,6,7,8,9] and three threads
t1 picks [0] ,do its processing, t2 picks [1] do its processing, t3 picks [2] do its processing now the next elements to be
picked are from [3] so for this structured order we will be using queues.
'''

'''
In python we can also create queue that use LIFO principle
'''
import queue

q = queue.Queue()
q2 = queue.LifoQueue()
q3 = queue.PriorityQueue()

numbers = [10,20,30,40,50,60,70,80,90] #This list will be shared among multiple threads

for number in numbers:
    q.put(number)

print(q.get())

for number in numbers:
    q2.put(number)

print(q2.get())

q3.put((3,"Ahmad"))
q3.put((2,"Ali"))
q3.put((1,"Hassan"))
q3.put((4, "Bilal"))

while(not q3.empty()):
    print(q3.get())





