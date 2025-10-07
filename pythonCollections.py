import collections

# List, tuple, dictionary, set built-in collection types
# Counter, namedTuple, OrderDict, defaultdict, deque inside collections module


#collections.Counter() is similar to the dictionary
a = "aaabbbbcdeffffggghh"
my_counter = collections.Counter(a) # will create a dictionary alphabet key and their count key
print(my_counter)
print(list(my_counter.elements()))
print(my_counter.most_common(4)) # returns the n top elements

names = "Hassan,Hassan,Hassan,Ali,Ali"
count_names = collections.Counter(names.split(","))
print(count_names)


'''namedTuple gives you class-like objects that are as lightweight as tuples but 
far more readable and convenient.'''

point = collections.namedtuple('Point' , 'x,y') # creates a class with attributes x and y
print(point(1,-4))

person = collections.namedtuple('Person', 'name,age,location')
print(person("Hassan",21,"Lahore"))

#orderdict same as dictionary but order is maintained

ordereddict = collections.OrderedDict() #remains same also if we do ordereddict = {}
ordereddict['a'] = 1 
ordereddict['b'] = 2
ordereddict['c'] = 3 
ordereddict['d'] = 2 

print(ordereddict)

#defaultdict, will not raise error if try to access key that is not present inside the dictionary

defaultdictionary = collections.defaultdict(int)
defaultdictionary['a']=1
defaultdictionary['b']=1
defaultdictionary['c']=3
defaultdictionary['d']=1

print(defaultdictionary['f']) #no error but 0 ass there is int set inside collections.defaultdict(int)

#deque

d = collections.deque()

d.append(1)
d.append(2)
d.append(3)
d.appendleft(0)

print(d)
