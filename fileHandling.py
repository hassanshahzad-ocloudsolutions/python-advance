#filehandling in python


# f = open('text.txt', 'r')
# print("Filename:", f.name)
# print("Mode:", f.mode)
# print("Is Closed?", f.closed)
# content = f.read() #reads whole file content
# onlyLine = f.readline() # read only first line
# print(content)
# f.close()


'''
if mode is set w then the content already written in file would be replaced by new content
if mode is set a+ then the new content is appended
'''

# with open('text.txt','a+') as file:
#     file.write("Python Programming is the Best")

#same as done already above

# with open("text.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("text.txt","r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        count+=1

print(count) # if read() called then 1 else readline() called then depends on number of lines