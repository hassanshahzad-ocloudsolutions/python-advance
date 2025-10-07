'''Comprehension is a short and expressive way to create sequences like list, dictionaries,
tuples in a single line isntead of using for loop. Performance increases and code decreases
syntax [expression for item in iterable if condition]
'''

'''In comprehension use [] for list, {} for dictionary and sets, () for tuples'''
#List Comprehensions
def squaresWithOutComprehension(n):
    squares = []
    for i in range(1,n+1):
        squares.append(i**2)
    return squares


def squaresWithComprehension(n):
    return [i**2 for i in range (1,n+1)]

def filterEvenNumbers(n):
    return [i for i in range(1,n+1) if i%2==0]

def increaseTwoMarks(studentsMarks):
    return [i+2 for i in studentsMarks]

#Dictionaries Comprehension
'''
{key_expression: value_expression for item in iterable if condition}
'''

def buildDictionary(student,marks):
    return {i:j for i,j in zip(student,marks)}

def squaresDictionary(n):
    return {i:i**2 for i in range(1,n+1)}

#set comprehension
def uniqueCubes(numbers):
    return {number**3 for number in numbers}

print(squaresWithOutComprehension(5))
print(squaresWithComprehension(5))
print(filterEvenNumbers(10))
print(increaseTwoMarks([10,10,12,13,15]))

print(buildDictionary(["Hassan","Ali","Bilal"],[10,20,10]))
print(squaresDictionary(5))

print(uniqueCubes([2,2,2,2,3,1,3,4,5,6]))

