
'''Argument Parsing means reading and handling command-line arguments that a
 user passes when running your Python script.
 
 Important concept when dealing with system programming, network programming'''

#Argument vectors

import sys
import getopt

#argv means argument vector

print(sys.argv[0]) #is the script/file name like (python3 myProgram.py in this argv[0] is myProgram.py)
print(sys.argv) # will print a list containing all runtime command line arguments.

fileName = sys.argv[1]
message = sys.argv[2]

with open (fileName,'w+') as f:
    f.write(message)


#Optional Arguments

opts, args = getopt.getopt(sys.argv[1:], "f:m:" , ['filename=', 'message='])

print(opts)
print(args)