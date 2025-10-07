# Getting student marks from file
file = open('student.txt','r')

while True:
    line = file.readline()
    if not line:
        break
    line = line.strip()  # remove \n and extra spaces

    student = line.split(",")[0]
    mark1 = line.split(",")[1]
    mark2 = line.split(",")[2]
    print(f'{student} got {mark1} marks in Maths')
    print(f'{student} got {mark2} marks in Computer Science')
    print(" ")

file.close()
#append more student marks

file = open('student.txt', 'a+')
file.writelines(["Shahab,60,60\n","Bilal,80,80\n"])