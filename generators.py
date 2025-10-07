#Generators one line, use for efficient memory usage

'''Generators are special iterators in Python that allow you to generate values one at a time — 
on the fly, instead of creating and storing the entire list in memory. They are a memory-efficient way 
to produce a sequence of results.'''

''' sequence from 1 to 9 Million take cube. One way to do is initialize the list [1,2,3,4.....9M] or
    iterate a for loop like for i in rang(9000000)
    We will use generators for this. Generators have lazy execution
'''


'''Generators are useful when
You are reading a massive file line-by-line.
You are streaming data from a web API.
You are processing logs, video frames, or sensor data in real time.
'''

def myGenerator(n):
    for x in range(1,n):
        yield x**3 #way of returning a value works same as return keyword does

def infiniteSequence():
    result = 1
    while True:
        yield result
        result*=5

values = myGenerator(9000000)
print(next(values)) #next is the keyword for getting next value from generator

for x in values:
    print(x)

values2 = infiniteSequence()


for i in range(100):
    print(next(values))

