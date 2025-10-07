#A mini project show casing use of generators

def read_log_file(filename):
    with open(filename,'r') as f:
        for line in f:
            yield line.strip() # this will yield line by line not whole file at once

def findErrors(filename):
    count = 0
    for line in read_log_file(filename):
        if "ERROR" in line:
            count+=1
    
    return count

print("Total ERROR lines:", findErrors("finderror.txt"))
        