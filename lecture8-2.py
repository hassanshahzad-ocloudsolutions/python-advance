
#OOP with DB
import sqlite3

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()


class Person:

    def __init__(self,id_number, fname,lname,age,location):
        self.__id = id_number
        self.__fname = fname
        self.__lname = lname
        self.__age = age
        self.__location = location

    @staticmethod
    def load_person(id_number):
        global cursor
        cursor.execute("SELECT * FROM Persons WHERE id = ?", (id_number,))
        results = cursor.fetchone()
        return Person(id_number, results[1], results[2], results[3],results[4])
    
    @staticmethod
    def putPerson(fname,lname,age,location):
         cursor.execute("""
        INSERT INTO Persons (first_name, last_name, age, location)
        VALUES (?, ?, ?, ?)
    """, (fname, lname, age, location)) #Parameterized Query-Prevents SQL Injection

    @staticmethod
    def deletePerson(id):
        cursor.execute("DELETE FROM Persons WHERE id =?", (id,))

    def getDetails(self):
        print(f'{self.__fname} {self.__lname} {self.__age} {self.__location}')

try: 
    p1 = Person.load_person(1)
    p2 = Person.load_person(10)
    p1.getDetails()
    p2.getDetails()

    Person.putPerson("Hassan","Daud",22,"Lahore")
    p3 = Person.load_person(27)
    p3.getDetails()

    cursor.execute('SELECT count(*) FROM Persons')
    print(cursor.fetchall())

    Person.deletePerson(24)
    cursor.execute('SELECT count(*) FROM Persons')
    print(cursor.fetchall())


except Exception as e:
    print(e)

finally:
    connection.close()

        